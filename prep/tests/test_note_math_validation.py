import json
from unittest.mock import patch

from django.test import SimpleTestCase, TestCase, override_settings
from django.urls import reverse

from accounts.models import User
from prep.models import (
    PrepContentCache,
    PrepCourse,
    PrepDocument,
    PrepNoteGenerationGuard,
    PrepNoteRepair,
    PrepQuestion,
    PrepTopic,
    PrepWallet,
)
from services.prep_ai_router import (
    NOTE_VALIDATION_STATE,
    NOTES_CACHE_VERSION,
    _nontechnical_solution_has_proof_scaffold,
    _display_math_issues,
    _latex_syntax_issues,
    _markdown_theorem_issues,
    _note_allows_code,
    _note_completion_issues,
    _approved_course_source_context,
    _note_completion_issues,
    _topic_notes_cache_signature,
    compute_cache_key,
    generate_similar_practice_questions,
    get_published_topic_note_levels,
    get_or_generate_topic_notes,
    get_or_generate_question_solution,
    normalize_math_delimiters,
    repair_json_escaped_latex_newlines,
    robust_json_loads,
)


class NoteMathValidationTests(TestCase):
    def test_repairs_json_decoded_notin_only_inside_math(self):
        source = "For $b \notin (a, b)$, continue.\nOutside prose stays unchanged."
        repaired = repair_json_escaped_latex_newlines(source)

        self.assertEqual(repaired, "For $b \\notin (a, b)$, continue.\nOutside prose stays unchanged.")

    def test_valid_display_math_is_accepted(self):
        content = """## 1. One

Text.

## 2. Two

Text.

## 3. Three

Text.

## 4. Four

Text.

## 5. Five

This final section has enough explanatory material to meet the completion threshold. It explains the
result, gives a useful exam reminder, and ends the notes with substantial instructional content.

$$
\\left\\lvert a_m-a_n\\right\\rvert \\leq \\varepsilon
$$
"""
        self.assertEqual(_display_math_issues(content), [])
        self.assertEqual(_note_completion_issues(content, "Sequences"), [])

    def test_split_right_delimiter_is_rejected(self):
        content = """$$
\\lvert a_m-a_n \\rvert = \\left\\lvert x-y \\right

\\right\\rvert
$$"""
        issues = _display_math_issues(content)
        self.assertTrue(any("blank structural break" in issue for issue in issues))
        self.assertTrue(any("split \\left or \\right delimiter" in issue for issue in issues))

    def test_unmatched_left_right_is_rejected(self):
        issues = _display_math_issues("$$\\left( x + y$$")
        self.assertTrue(any("unmatched \\left/\\right" in issue for issue in issues))

    def test_unmatched_grouping_and_inline_math_are_rejected(self):
        issues = _latex_syntax_issues("A broken inline expression $x + 1 and $$\\frac{1}{2$$")
        self.assertIn("unmatched inline-math delimiter", issues)
        self.assertTrue(any("unmatched braces" in issue for issue in issues))

    def test_balanced_latex_grouping_is_accepted(self):
        content = """The identity $x^2 + y^2$ is useful.

$$
\\sqrt[2]{x^2 + y^2} = \\left\\lvert z \\right\\rvert
$$"""
        self.assertEqual(_latex_syntax_issues(content), [])

    def test_half_open_interval_notation_is_not_rejected_as_unbalanced(self):
        content = r"""$$
[a, b) = \\{x \\in \\mathbb{R} : a \\leq x < b\\}
$$
$$
(-\\infty, b] = \\{x \\in \\mathbb{R} : x \\leq b\\}
$$"""

        self.assertEqual(_latex_syntax_issues(content), [])

    def test_nested_latex_environments_must_be_inside_display_math(self):
        equation = """\\begin{aligned}
c_k &= \\begin{cases} [a_k, c_k], & \\text{if } f(a_k) f(c_k) < 0, \\\\
[c_k, b_k], & \\text{if } f(c_k) f(b_k) < 0.
\\end{cases}
\\end{aligned}"""

        issues = _latex_syntax_issues(equation)

        self.assertIn("LaTeX environment aligned is outside display math", issues)
        self.assertIn("LaTeX environment cases is outside display math", issues)
        self.assertEqual(_latex_syntax_issues(f"$$\n{equation}\n$$"), [])

    def test_code_block_dollar_signs_are_not_math_validation_errors(self):
        content = """```R
result <- frame$column
$$ not mathematical output
```"""
        self.assertEqual(_display_math_issues(content), [])
        self.assertEqual(_note_completion_issues(content, "Sequences"), [
            "missing section ## 1.",
            "missing section ## 2.",
            "missing section ## 3.",
            "missing section ## 4.",
            "missing section ## 5.",
        ])

    def test_rejects_split_theorem_title_that_looks_like_a_list_item(self):
        content = "> **Theorem 3.5 (Invariance of Sufficiency Under One\n-to-One Transformations):** If T is sufficient."

        self.assertTrue(any("theorem blockquote title is split" in issue for issue in _markdown_theorem_issues(content)))

    def test_non_computing_topics_reject_code_but_computing_topics_allow_it(self):
        code_notes = "## 1. Confidence\n\nText.\n\n```R\nmean(c(1, 2, 3))\n```"
        statistics_course = PrepCourse(category="Statistics")
        computing_course = PrepCourse(category="Computing")
        programming_statistics_course = PrepCourse(
            category="Statistics",
            title="Programming Language for Statistics 1",
        )

        self.assertFalse(_note_allows_code(statistics_course, "Confidence Intervals", "Statistical estimation"))
        self.assertTrue(_note_allows_code(computing_course, "R Programming", "Statistical programming"))
        self.assertTrue(_note_allows_code(programming_statistics_course, "Course Overview", "Uses R"))
        self.assertTrue(any("code block is not allowed" in issue for issue in _note_completion_issues(
            code_notes,
            "Confidence Intervals",
            allow_code=False,
        )))
        self.assertNotIn("code block is not allowed", _note_completion_issues(
            code_notes,
            "R Programming",
            allow_code=True,
        ))

    def test_normalize_math_delimiters_preserves_infimum_and_infinity_commands(self):
        self.assertEqual(
            normalize_math_delimiters("The infimum is $\\inf S$; limits may tend to $\\infty$."),
            "The infimum is $\\inf S$; limits may tend to $\\infty$.",
        )

    def test_json_parser_preserves_square_brackets_inside_latex_strings(self):
        repair = {
            "old_block": r"\\begin{cases} [a_k, c_k] \\end{cases}",
            "new_block": r"$$\\begin{cases} [a_k, c_k] \\end{cases}$$",
        }

        self.assertEqual(robust_json_loads(json.dumps(repair)), repair)

    @patch("services.prep_ai_router.route_math_request")
    def test_social_science_question_solution_uses_explanatory_template(self, mock_route):
        course = PrepCourse.objects.create(
            code="ASC 100",
            title="Introduction to Sociology",
            slug="asc-100",
            category="Social Sciences",
            study_profile={
                "subject_family": "social_science",
                "capabilities": {"code": False, "math_notation": False, "chemical_equations": False},
            },
            study_profile_version=1,
        )
        topic = PrepTopic.objects.create(
            course=course,
            title="Social Organisation",
            slug="social-organisation",
            order=1,
        )
        question = PrepQuestion.objects.create(
            topic=topic,
            question_type="authentic",
            number=1,
            marks=15,
            topic_label="Social Organisation",
            question_latex="(a) What is social organisation?\n\n(b) With examples, describe the five forms of social organisation.",
            solution_latex="",
            verification_status="verified",
        )
        mock_route.return_value = {
            "success": True,
            "content": "### Definition\n\nSocial organisation is the patterned relationship between people in society.",
            "model_used": "deepseek-chat",
            "usage": {"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30},
        }

        get_or_generate_question_solution(
            question.question_latex,
            course.code,
            topic_label=question.topic_label,
            question_obj=question,
        )

        prompt = mock_route.call_args[0][0]
        self.assertIn("Key Concept / Definition", prompt)
        self.assertNotIn("Problem Statement & Given Conditions", prompt)
        self.assertNotIn("Q.E.D.", prompt)
        self.assertEqual(mock_route.call_args.kwargs["is_complex_proof"], False)

    def test_legacy_proof_scaffold_is_detected_for_nontechnical_answer_cleanup(self):
        self.assertTrue(_nontechnical_solution_has_proof_scaffold(
            "## 2. Step-by-Step Rigorous Proof / Derivation\n\nThe explanation follows."
        ))
        self.assertTrue(_nontechnical_solution_has_proof_scaffold("### 2. Proof and Derivation"))
        self.assertFalse(_nontechnical_solution_has_proof_scaffold(
            "## Explanation and Analysis\n\nSocial organisation describes patterned relationships."
        ))

    def test_nontechnical_notes_reject_mathematical_proof_scaffold(self):
        profile = {
            "subject_family": "social_science",
            "note_structure": ["One", "Two", "Three", "Four", "Five"],
        }
        content = "## 1. One\n\n## 2. Step-by-Step Rigorous Proof / Derivation\n\n" + ("Explanation. " * 30)

        issues = _note_completion_issues(content, "Social Organisation", study_profile=profile)

        self.assertIn("mathematical proof scaffold is not allowed for this subject family", issues)

    @patch("services.prep_ai_router.route_math_request")
    def test_nontechnical_proof_response_is_rejected_before_storage(self, mock_route):
        course = PrepCourse.objects.create(
            code="SOC 100",
            title="Sociology",
            slug="soc-100-proof-rejection",
            category="Social Sciences",
            study_profile={
                "subject_family": "social_science",
                "capabilities": {"code": False, "math_notation": False, "chemical_equations": False},
            },
            study_profile_version=1,
        )
        topic = PrepTopic.objects.create(course=course, title="Social Organisation", slug="social-organisation-rejection")
        question = PrepQuestion.objects.create(
            topic=topic,
            question_type="authentic",
            number=1,
            marks=10,
            question_latex="Explain social organisation.",
            solution_latex="",
        )
        mock_route.return_value = {
            "success": True,
            "content": "## 2. Step-by-Step Rigorous Proof / Derivation\n\nInvalid answer.",
            "model_used": "test-model",
            "usage": {},
        }

        result = get_or_generate_question_solution(
            question.question_latex,
            course.code,
            topic_label=topic.title,
            question_obj=question,
        )

        question.refresh_from_db()
        self.assertEqual(result["solution"], "")
        self.assertIn("proof format", result["error"])
        self.assertEqual(question.solution_latex, "")
        self.assertFalse(PrepContentCache.objects.filter(course=course, content_type="solution_derivation").exists())

    @patch("services.prep_ai_router.route_math_request")
    def test_nontechnical_proof_cache_is_ignored(self, mock_route):
        course = PrepCourse.objects.create(
            code="SOC 101",
            title="Sociology",
            slug="soc-101-proof-cache",
            study_profile={
                "subject_family": "social_science",
                "capabilities": {"code": False, "math_notation": False, "chemical_equations": False},
            },
            study_profile_version=1,
        )
        question = "Explain social organisation."
        cache_key = compute_cache_key(
            "solution", course.code, question[:50], "profile-v1", "explanatory-v1"
        )
        PrepContentCache.objects.create(
            cache_key=cache_key,
            content_type="solution_derivation",
            prompt_hash="legacy-proof-answer",
            payload={"solution": "### 2. Proof and Derivation", "model": "old-model"},
            course=course,
        )
        mock_route.return_value = {
            "success": True,
            "content": "## Explanation and Analysis\n\nA clear, source-grounded answer.",
            "model_used": "test-model",
            "usage": {},
        }

        result = get_or_generate_question_solution(question, course.code, topic_label="Social Organisation")

        self.assertFalse(result["cached"])
        self.assertIn("Explanation and Analysis", result["solution"])
        mock_route.assert_called_once()


class InvalidCachedNoteRecoveryTests(TestCase):
    valid_notes = """## 1. One

Text.

## 2. Two

Text.

## 3. Three

Text.

## 4. Four

Text.

## 5. Five

This final section has enough explanatory material to meet the completion threshold. It explains the
result, gives a useful exam reminder, and ends the notes with substantial instructional content.

$$
\\left\\lvert a_m-a_n\\right\\rvert \\leq \\varepsilon
$$
"""

    def setUp(self):
        self.user = User.objects.create_user(
            username="note_validation_user",
            email="note-validation@example.test",
            password="Valid123",
        )
        self.course = PrepCourse.objects.create(
            code="VAL 101",
            title="Validation Testing",
            slug="validation-testing",
        )
        self.topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Sequences",
            slug="sequences",
        )

    @patch("services.prep_ai_router.route_math_request")
    def test_revalidated_legacy_cache_clears_stale_review_guard(self, generation_request):
        signature = _topic_notes_cache_signature(
            self.course, self.topic, self.topic.title, self.topic.subtopics
        )
        cache_key = compute_cache_key(
            "notes", NOTES_CACHE_VERSION, self.course.code, self.topic.title, "level_2", signature
        )
        cache = PrepContentCache.objects.create(
            cache_key=cache_key,
            content_type="topic_notes",
            prompt_hash="legacy-valid-intervals",
            payload={"content": self.valid_notes, "level": "level_2"},
            course=self.course,
            topic=self.topic,
        )
        guard = PrepNoteGenerationGuard.objects.create(
            topic=self.topic,
            level="level_2",
            source_signature=signature,
            failed_attempts=2,
            status="needs_review",
            last_error="old validator rejected valid interval brackets",
        )
        repair = PrepNoteRepair.objects.create(
            topic=self.topic,
            level="level_2",
            source_signature=signature,
            cache_key=cache_key,
            original_content=self.valid_notes,
            current_content=self.valid_notes,
            validation_issues=["old unmatched interval bracket error"],
            attempts=3,
            status="needs_review",
            last_error="old validator rejected valid interval brackets",
        )

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertEqual(result["notes"].strip(), self.valid_notes.strip())
        self.assertTrue(result["cached"])
        self.assertFalse(PrepNoteGenerationGuard.objects.filter(pk=guard.pk).exists())
        repair.refresh_from_db()
        self.assertEqual(repair.status, "validated")
        self.assertEqual(repair.validation_issues, [])
        cache.refresh_from_db()
        self.assertEqual(cache.payload["validation_state"], NOTE_VALIDATION_STATE)
        generation_request.assert_not_called()

    @patch("services.prep_ai_router.call_together_repair")
    @override_settings(TOGETHER_REPAIR_MODEL="configured-targeted-repair-model")
    def test_invalid_cache_is_replaced_and_marked_as_free_recovery(self, repair_request):
        signature = _topic_notes_cache_signature(
            self.course, self.topic, self.topic.title, self.topic.subtopics
        )
        cache_key = compute_cache_key(
            "notes", NOTES_CACHE_VERSION, self.course.code, self.topic.title, "level_2", signature
        )
        broken_block = "$$\n\\left\\lvert a_m-a_n\\right\n\n\\right\\rvert\n$$"
        broken_notes = self.valid_notes.replace(
            "$$\n\\left\\lvert a_m-a_n\\right\\rvert \\leq \\varepsilon\n$$",
            broken_block,
        )
        PrepContentCache.objects.create(
            cache_key=cache_key,
            content_type="topic_notes",
            prompt_hash="old",
            payload={"content": broken_notes},
            course=self.course,
            topic=self.topic,
        )
        repair_request.return_value = {
            "success": True,
            "content": json.dumps({"old_block": broken_block, "new_block": "$$\n\\left\\lvert a_m-a_n\\right\\rvert \\leq \\varepsilon\n$$"}),
            "usage": {"total_tokens": 0},
        }

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertFalse(result["cached"])
        self.assertTrue(result["regenerated_from_invalid_cache"])
        self.assertEqual(
            PrepContentCache.objects.get(cache_key=cache_key).payload["content"].strip(), self.valid_notes.strip()
        )
        self.assertEqual(
            repair_request.call_args.kwargs["model"],
            "configured-targeted-repair-model",
        )
        repair_source = repair_request.call_args.args[0][1]["content"]
        self.assertIn("## 5. Five", repair_source)
        self.assertNotIn("## 1. One", repair_source)
        self.assertNotIn("## 4. Four", repair_source)

    @patch("services.prep_ai_router.call_together_repair")
    @override_settings(TOGETHER_REPAIR_MODEL="configured-targeted-repair-model")
    def test_screenshot_nested_environment_is_sent_to_configured_targeted_repair(self, repair_request):
        signature = _topic_notes_cache_signature(
            self.course, self.topic, self.topic.title, self.topic.subtopics
        )
        cache_key = compute_cache_key(
            "notes", NOTES_CACHE_VERSION, self.course.code, self.topic.title, "level_2", signature
        )
        valid_equation = "$$\n\\left\\lvert a_m-a_n\\right\\rvert \\leq \\varepsilon\n$$"
        slash = chr(92)
        broken_block = (
            slash + "begin{aligned}\n"
            + "c_k &= " + slash + "begin{cases} [a_k, c_k], & "
            + slash + "text{if } f(a_k) f(c_k) < 0, " + slash + slash + "\n"
            + "[c_k, b_k], & " + slash + "text{if } f(c_k) f(b_k) < 0.\n"
            + slash + "end{cases}\n"
            + slash + "end{aligned}"
        )
        corrected_block = "$$\n" + broken_block + "\n$$"
        broken_notes = self.valid_notes.replace(valid_equation, broken_block)
        PrepContentCache.objects.create(
            cache_key=cache_key,
            content_type="topic_notes",
            prompt_hash="nested-environment",
            payload={"content": broken_notes, "level": "level_2"},
            course=self.course,
            topic=self.topic,
        )
        repair_request.return_value = {
            "success": True,
            "content": json.dumps({"old_block": broken_block, "new_block": corrected_block}),
            "usage": {"total_tokens": 0},
        }

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertEqual(repair_request.call_count, 1, repair_request.call_args_list)
        self.assertTrue(result.get("repaired"), result)
        self.assertEqual(result["notes"], self.valid_notes.replace(valid_equation, corrected_block))
        repair_request.assert_called_once()
        self.assertEqual(repair_request.call_args.kwargs["model"], "configured-targeted-repair-model")
        repair_source = repair_request.call_args.args[0][1]["content"]
        self.assertIn("LaTeX environment aligned is outside display math", repair_source)
        self.assertIn(broken_block, repair_source)
        self.assertNotIn("## 1. One", repair_source)
        saved_payload = PrepContentCache.objects.get(cache_key=cache_key).payload
        self.assertEqual(saved_payload["content"], result["notes"])
        self.assertEqual(saved_payload["validation_state"], NOTE_VALIDATION_STATE)

    @patch("services.prep_ai_router.call_together_repair")
    @patch("services.prep_ai_router.route_math_request")
    def test_fresh_invalid_notes_use_targeted_repair_before_review_lock(self, route_request, repair_request):
        broken_block = "$$\n\\left\\lvert a_m-a_n\\right\n\n\\right\\rvert\n$$"
        broken_notes = self.valid_notes.replace(
            "$$\n\\left\\lvert a_m-a_n\\right\\rvert \\leq \\varepsilon\n$$",
            broken_block,
        )
        route_request.return_value = {
            "success": True,
            "content": broken_notes,
            "model_used": "test-notes-model",
            "usage": {},
        }
        repair_request.return_value = {
            "success": True,
            "content": json.dumps({
                "old_block": broken_block,
                "new_block": "$$\n\\left\\lvert a_m-a_n\\right\\rvert \\leq \\varepsilon\n$$",
            }),
            "usage": {},
        }

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_1",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertTrue(result.get("repaired"), result)
        self.assertEqual(result["notes"].strip(), self.valid_notes.strip())
        repair_request.assert_called_once()
        self.assertFalse(PrepContentCache.objects.get(topic=self.topic).payload.get("validation_state") is None)

    @patch("services.prep_ai_router.call_deepseek")
    @patch("services.prep_ai_router.route_math_request")
    def test_missing_sections_use_bounded_continuation_before_targeted_repair(
        self,
        route_request,
        continuation_request,
    ):
        truncated_notes = self.valid_notes.split("## 4.", 1)[0].rstrip()
        route_request.return_value = {
            "success": True,
            "content": truncated_notes,
            "model_used": "test-notes-model",
            "usage": {},
        }
        continuation_request.return_value = {
            "success": True,
            "content": "## 4." + self.valid_notes.split("## 4.", 1)[1],
            "usage": {},
        }

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_1",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertFalse(result.get("validation_failed", False))
        self.assertEqual(result["notes"].strip(), self.valid_notes.strip())
        continuation_request.assert_called_once()

    @patch("services.prep_ai_router.call_together_repair")
    @patch("services.prep_ai_router.route_math_request")
    def test_cached_missing_sections_use_regeneration_not_block_repair(
        self,
        route_request,
        repair_request,
    ):
        signature = _topic_notes_cache_signature(
            self.course, self.topic, self.topic.title, self.topic.subtopics
        )
        cache_key = compute_cache_key(
            "notes", NOTES_CACHE_VERSION, self.course.code, self.topic.title, "level_2", signature
        )
        truncated_notes = self.valid_notes.split("## 4.", 1)[0].rstrip()
        PrepContentCache.objects.create(
            cache_key=cache_key,
            content_type="topic_notes",
            prompt_hash="truncated",
            payload={"content": truncated_notes, "level": "level_2"},
            course=self.course,
            topic=self.topic,
        )
        route_request.return_value = {
            "success": True,
            "content": "## 4." + self.valid_notes.split("## 4.", 1)[1],
            "model_used": "test-notes-model",
            "usage": {},
        }

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertTrue(route_request.called, route_request.call_args_list)
        self.assertTrue(result.get("repaired"), result)
        self.assertEqual(result["notes"].strip(), self.valid_notes.strip())
        route_request.assert_called_once()
        repair_request.assert_not_called()

    @patch("services.email_service.send_prep_note_generation_failure_email", return_value=True)
    @patch("services.prep_ai_router.call_together_repair")
    @patch("services.prep_ai_router.route_math_request")
    def test_three_failed_targeted_repairs_store_notes_and_notify_admin(
        self,
        route_request,
        repair_request,
        send_failure_email,
    ):
        broken_block = "$$\n\\left\\lvert a_m-a_n\\right\n\n\\right\\rvert\n$$"
        route_request.return_value = {
            "success": True,
            "content": self.valid_notes.replace(
                "$$\n\\left\\lvert a_m-a_n\\right\\rvert \\leq \\varepsilon\n$$",
                broken_block,
            ),
            "model_used": "test-notes-model",
            "usage": {},
        }
        repair_request.return_value = {"success": False, "error": "repair unavailable"}

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_1",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        guard = PrepNoteGenerationGuard.objects.get(topic=self.topic, level="level_1")
        cache = PrepContentCache.objects.get(topic=self.topic, content_type="topic_notes")
        self.assertTrue(result["validation_failed"])
        self.assertEqual(repair_request.call_count, 3)
        self.assertEqual(guard.status, "needs_review")
        self.assertEqual(guard.failed_attempts, 1)
        self.assertTrue(cache.payload["content"])
        self.assertIsNone(cache.payload.get("validation_state"))
        send_failure_email.assert_called_once_with(guard)

    @patch("services.prep_ai_router.route_math_request")
    def test_missing_level_one_and_three_use_the_same_validated_generation_path(self, route_request):
        route_request.return_value = {
            "success": True,
            "content": self.valid_notes,
            "model_used": "test-notes-model",
            "usage": {},
        }

        for level in ("level_1", "level_3"):
            result = get_or_generate_topic_notes(
                self.course.code,
                self.topic.title,
                level=level,
                course_obj=self.course,
                topic_obj=self.topic,
            )

            self.assertEqual(result["level"], level)
            self.assertTrue(result["notes"])
            self.assertFalse(result.get("validation_failed", False))

        self.assertEqual(route_request.call_count, 2)

    def test_cache_only_read_keeps_invalid_entry_for_free_recovery(self):
        signature = _topic_notes_cache_signature(
            self.course, self.topic, self.topic.title, self.topic.subtopics
        )
        cache_key = compute_cache_key(
            "notes", NOTES_CACHE_VERSION, self.course.code, self.topic.title, "level_2", signature
        )
        PrepContentCache.objects.create(
            cache_key=cache_key,
            content_type="topic_notes",
            prompt_hash="old",
            payload={"content": "$$\\left( x \\right\n\n\\right)$$"},
            course=self.course,
            topic=self.topic,
        )

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
            generate_if_missing=False,
        )

        self.assertTrue(result["regenerated_from_invalid_cache"])
        self.assertTrue(PrepContentCache.objects.filter(cache_key=cache_key).exists())

    @patch("prep.views.get_or_generate_topic_notes")
    def test_invalid_cache_recovery_does_not_deduct_student_credits(self, generate_notes):
        wallet = PrepWallet.get_or_create_wallet(self.user)
        before = wallet.credits_balance
        generate_notes.return_value = {
            "notes": self.valid_notes,
            "cached": False,
            "regenerated_from_invalid_cache": True,
            "level": "level_2",
            "model": "test-model",
            "usage": {"total_tokens": 100},
        }
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("prep:api_topic_notes"),
            data='{ "topic_id": "%s", "level": "level_2" }' % self.topic.id,
            content_type="application/json",
        )

        wallet.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["credits_deducted"], 0)
        self.assertEqual(wallet.credits_balance, before)

    @patch("prep.views.get_available_credits", return_value=100)
    @patch("prep.views.get_or_generate_question_solution")
    def test_stale_proof_solution_is_not_returned_for_social_science(self, generate_solution, _credits):
        self.course.study_profile = {
            "subject_family": "social_science",
            "capabilities": {"code": False, "math_notation": False, "chemical_equations": False},
        }
        self.course.save(update_fields=["study_profile"])
        question = PrepQuestion.objects.create(
            topic=self.topic,
            question_type="authentic",
            number=1,
            marks=10,
            topic_label=self.topic.title,
            question_latex="Explain social organisation.",
            solution_latex="## 2. Step-by-Step Rigorous Proof / Derivation\n\nLegacy answer.",
            verification_status="verified",
        )
        generate_solution.return_value = {
            "solution": "## Explanation and Analysis\n\nA source-grounded answer.",
            "cached": True,
            "model": "test-model",
        }
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("prep:api_solve_question"),
            data=json.dumps({"question_id": question.id}),
            content_type="application/json",
        )

        question.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Explanation and Analysis", response.json()["solution"])
        self.assertNotIn("Step-by-Step Rigorous Proof", response.json()["solution"])
        self.assertEqual(question.solution_latex, "")
        generate_solution.assert_called_once()

    @patch("prep.views.get_or_generate_topic_notes")
    def test_rejected_note_generation_is_not_reported_as_a_server_error(self, generate_notes):
        generate_notes.return_value = {
            "notes": "",
            "error": "The notes generation was incomplete. Please retry.",
            "validation_failed": True,
        }
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("prep:api_topic_notes"),
            data='{ "topic_id": "%s", "level": "level_2" }' % self.topic.id,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 422)

    @patch("services.prep_ai_router.route_math_request")
    def test_failed_solution_generation_returns_an_error_without_placeholder(self, route_request):
        route_request.return_value = {"success": False, "error": "Provider unavailable"}

        result = get_or_generate_question_solution(
            "Define strong consistency.",
            self.course.code,
            self.topic.title,
        )

        self.assertEqual(result["solution"], "")
        self.assertEqual(result["error"], "Provider unavailable")

    @patch("services.prep_ai_router.route_math_request")
    def test_prior_valid_shared_notes_are_served_when_the_current_generation_fails(self, route_request):
        PrepContentCache.objects.create(
            cache_key="notes:legacy:validation-testing:sequences:level_2",
            content_type="topic_notes",
            prompt_hash="previous-version",
            payload={
                "content": self.valid_notes,
                "level": "level_2",
                "model": "previous-model",
            },
            course=self.course,
            topic=self.topic,
        )
        route_request.return_value = {"success": False, "error": "Provider unavailable"}

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertTrue(result["cached"])
        self.assertTrue(result["stale"])
        self.assertEqual(result["notes"], self.valid_notes.strip())

    def test_validated_shared_note_is_not_revalidated_for_later_students(self):
        cache = PrepContentCache.objects.create(
            cache_key="notes:published:validation-testing:sequences:level_2",
            content_type="topic_notes",
            prompt_hash="published-version",
            payload={
                "content": self.valid_notes,
                "level": "level_2",
                "model": "test-model",
            },
            course=self.course,
            topic=self.topic,
        )

        first_read = get_published_topic_note_levels(self.topic)
        cache.refresh_from_db()
        self.assertEqual(first_read["level_2"], self.valid_notes.strip())
        self.assertEqual(cache.payload["validation_state"], NOTE_VALIDATION_STATE)

        second_read = get_published_topic_note_levels(self.topic)
        self.assertEqual(second_read["level_2"], self.valid_notes.strip())

    def test_approved_coursework_source_is_available_to_note_generation(self):
        PrepDocument.objects.create(
            course=self.course,
            topic_name="Full Syllabus",
            extracted_text="Approved R example: mean(c(1, 2, 3))",
            stage="stage_3",
        )

        source = _approved_course_source_context(self.course, "Sequences")

        self.assertIn("Approved R example", source)

    def test_examination_papers_are_not_note_generation_sources(self):
        PrepDocument.objects.create(
            course=self.course,
            doc_type="Final Examination Paper",
            topic_name="Full Syllabus",
            extracted_text="Exam-only formula: $x^2 + y^2 = z^2$",
            stage="stage_3",
        )

        self.assertEqual(_approved_course_source_context(self.course, "Sequences"), "")

    def test_published_note_preserves_infimum_without_ai_generation(self):
        invalid_inf = self.valid_notes.replace("a_m-a_n", "a_m-a_n \\inf")
        PrepContentCache.objects.create(
            cache_key="notes:published:validation-testing:sequences:invalid-inf",
            content_type="topic_notes",
            prompt_hash="published-version",
            payload={
                "content": invalid_inf,
                "level": "level_2",
                "validation_state": NOTE_VALIDATION_STATE,
            },
            course=self.course,
            topic=self.topic,
        )

        published = get_published_topic_note_levels(self.topic)

        self.assertIn("\\inf", published["level_2"])

    def test_published_note_bypasses_signature_changes_from_other_topics(self):
        PrepContentCache.objects.create(
            cache_key="notes:published:validation-testing:sequences:level_2:old-signature",
            content_type="topic_notes",
            prompt_hash="old-signature",
            payload={
                "content": self.valid_notes,
                "level": "level_2",
                "validation_state": NOTE_VALIDATION_STATE,
            },
            course=self.course,
            topic=self.topic,
        )
        PrepTopic.objects.create(
            course=self.course,
            order=2,
            title="Later Approved Topic",
            slug="later-approved-topic",
        )

        with patch("services.prep_ai_router.route_math_request") as generation:
            result = get_or_generate_topic_notes(
                self.course.code,
                self.topic.title,
                level="level_2",
                course_obj=self.course,
                topic_obj=self.topic,
            )

        self.assertTrue(result["cached"])
        self.assertEqual(result["notes"], self.valid_notes.strip())
        generation.assert_not_called()

    def test_topic_source_update_invalidates_only_its_own_published_notes(self):
        other_topic = PrepTopic.objects.create(
            course=self.course,
            order=2,
            title="Limits",
            slug="limits",
        )
        own_cache = PrepContentCache.objects.create(
            cache_key="notes:source-change:sequences",
            content_type="topic_notes",
            prompt_hash="source-change",
            payload={"content": self.valid_notes, "level": "level_2", "validation_state": NOTE_VALIDATION_STATE},
            course=self.course,
            topic=self.topic,
        )
        other_cache = PrepContentCache.objects.create(
            cache_key="notes:source-change:limits",
            content_type="topic_notes",
            prompt_hash="source-change",
            payload={"content": self.valid_notes, "level": "level_2", "validation_state": NOTE_VALIDATION_STATE},
            course=self.course,
            topic=other_topic,
        )

        self.topic.summary = "Approved additional source material."
        self.topic.save(update_fields=["summary"])

        self.assertFalse(PrepContentCache.objects.filter(pk=own_cache.pk).exists())
        self.assertTrue(PrepContentCache.objects.filter(pk=other_cache.pk).exists())


class SharedPracticeQuestionTests(TestCase):
    def setUp(self):
        self.course = PrepCourse.objects.create(
            code="PRA 101",
            title="Practice Sharing",
            slug="practice-sharing",
        )
        self.topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Sequences",
            slug="practice-sequences",
        )

    @patch("services.prep_ai_router.route_math_request")
    def test_complete_valid_practice_set_is_saved_once_and_reused_globally(self, route_request):
        route_request.return_value = {
            "success": True,
            "content": json.dumps([
                {
                    "number": 1,
                    "marks": 5,
                    "topic_label": "Arithmetic sequences",
                    "question_latex": "Find the next term of $1, 3, 5, \ldots$.",
                    "solution_latex": "The common difference is $2$, so the next term is $7$.",
                    "hint": "Find the common difference.",
                },
                {
                    "number": 2,
                    "marks": 5,
                    "topic_label": "Geometric sequences",
                    "question_latex": "Find the next term of $2, 6, 18, \ldots$.",
                    "solution_latex": "The common ratio is $3$, so the next term is $54$.",
                    "hint": "Find the common ratio.",
                },
            ]),
            "model_used": "test-model",
            "usage": {"total_tokens": 10},
        }

        first = generate_similar_practice_questions(
            self.course.code,
            self.topic.title,
            question_count=2,
            topic_obj=self.topic,
            course_obj=self.course,
        )
        second = generate_similar_practice_questions(
            self.course.code,
            self.topic.title,
            question_count=2,
            topic_obj=self.topic,
            course_obj=self.course,
        )

        self.assertTrue(first["success"])
        self.assertEqual(first["fresh_generated_count"], 2)
        self.assertEqual(
            PrepQuestion.objects.filter(topic=self.topic, question_type="generated").count(), 2
        )
        self.assertTrue(second["success"])
        self.assertTrue(second["cached"])
        self.assertEqual(second["fresh_generated_count"], 0)
        route_request.assert_called_once()

    @patch("services.prep_ai_router.call_deepseek")
    @patch("services.prep_ai_router.route_math_request")
    def test_incomplete_practice_set_is_not_saved(self, route_request, continue_request):
        route_request.return_value = {
            "success": True,
            "content": json.dumps([
                {
                    "number": 1,
                    "marks": 5,
                    "topic_label": "Arithmetic sequences",
                    "question_latex": "Find the next term of $1, 3, 5, \ldots$.",
                    "solution_latex": "The common difference is $2$.",
                },
            ]),
            "model_used": "test-model",
            "usage": {"total_tokens": 10},
        }
        continue_request.return_value = {"success": False, "error": "Provider unavailable"}

        result = generate_similar_practice_questions(
            self.course.code,
            self.topic.title,
            question_count=2,
            topic_obj=self.topic,
            course_obj=self.course,
        )

        self.assertFalse(result["success"])
        self.assertIn("did not pass validation", result["error"])
        self.assertFalse(PrepQuestion.objects.filter(topic=self.topic, question_type="generated").exists())
        continue_request.assert_called_once()


class TopicStudyQuestionRenderingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="topic_render_user",
            email="topic-render@example.test",
            password="Valid123",
        )
        self.client.force_login(self.user)
        self.course = PrepCourse.objects.create(
            code="TOP 101",
            title="Topic Rendering",
            slug="topic-rendering",
        )
        self.topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Generated Only",
            slug="generated-only",
        )
        PrepQuestion.objects.create(
            topic=self.topic,
            question_type="generated",
            verification_status="verified",
            number=1,
            marks=5,
            question_latex="Find $x$.",
            solution_latex="$x = 1$.",
        )

    @patch("services.prep_ai_router.get_or_generate_topic_notes")
    def test_topic_page_renders_generated_questions_without_authentic_questions(self, generate_notes):
        generate_notes.return_value = {"notes": "## 1. Valid Notes", "cached": True}

        response = self.client.get(
            reverse("prep:topic_study", kwargs={"topic_id": self.topic.id}) + "?tab=notes"
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Find")

    @patch("services.prep_ai_router.call_deepseek")
    @patch("services.prep_ai_router.route_math_request")
    def test_invalid_practice_set_is_corrected_before_it_is_saved(self, route_request, continue_request):
        PrepQuestion.objects.filter(
            topic=self.topic,
            question_type="generated",
        ).delete()
        incomplete_set = [
            {
                "number": 1,
                "marks": 5,
                "topic_label": "Arithmetic sequences",
                "question_latex": "Find the next term of $1, 3, 5, \\ldots$.",
                "solution_latex": "The common difference is $2$.",
            },
        ]
        corrected_set = incomplete_set + [
            {
                "number": 2,
                "marks": 5,
                "topic_label": "Geometric sequences",
                "question_latex": "Find the next term of $2, 6, 18, \\ldots$.",
                "solution_latex": "The common ratio is $3$, so the next term is $54$.",
            },
        ]
        route_request.return_value = {
            "success": True,
            "content": json.dumps(incomplete_set),
            "model_used": "test-model",
            "usage": {"total_tokens": 10},
        }
        continue_request.return_value = {
            "success": True,
            "content": json.dumps(corrected_set),
            "usage": {"total_tokens": 10},
        }

        result = generate_similar_practice_questions(
            self.course.code,
            self.topic.title,
            question_count=2,
            topic_obj=self.topic,
            course_obj=self.course,
        )

        self.assertTrue(result["success"])
        self.assertEqual(result["fresh_generated_count"], 2)
        self.assertEqual(
            PrepQuestion.objects.filter(topic=self.topic, question_type="generated").count(), 2
        )
        continue_request.assert_called_once()
