import json
import tempfile
from unittest.mock import patch

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import SimpleTestCase, TestCase, override_settings
from django.urls import reverse

from accounts.models import User
from prep.management.commands.reindex_course_topics import Command as ReindexCourseTopicsCommand
from prep.models import (
    PrepContentCache,
    PrepCourse,
    PrepCourseEnrollment,
    PrepDocument,
    PrepDocumentVisual,
    PrepNoteGenerationGuard,
    PrepNoteRepair,
    PrepQuestion,
    PrepTopic,
    PrepTopicNotesJob,
    PrepWallet,
)
from prep.content_rules import CONTENT_MODALITIES
from services.prep_ai_router import (
    ANSWER_VALIDATION_VERSION,
    NOTE_VALIDATION_STATE,
    NOTES_CACHE_VERSION,
    _nontechnical_solution_has_proof_scaffold,
    _display_math_issues,
    _latex_syntax_issues,
    _markdown_table_issues,
    _markdown_theorem_issues,
    _note_repair_scope,
    _parse_topic_note_repair_patch,
    _note_allows_code,
    _note_completion_issues,
    call_deepseek,
    call_together_repair,
    _course_administrative_metadata_issues,
    _insert_required_visual_markers,
    _approved_course_source_context,
    _approved_course_source_references,
    _approved_visual_manifest,
    _dedupe_approved_visual_images,
    _insert_required_visual_markers,
    _normalize_approved_visual_captions,
    _note_completion_issues,
    _topic_notes_cache_signature,
    _strip_course_administrative_front_matter,
    compute_cache_key,
    generate_similar_practice_questions,
    get_published_topic_note_levels,
    get_or_generate_topic_notes,
    get_or_generate_question_solution,
    normalize_math_delimiters,
    repair_json_escaped_latex_newlines,
    robust_json_loads,
    store_cached_content,
)
from services.prep_blocks import parse_markdown_to_blocks


class ReindexCourseTopicReportTests(SimpleTestCase):
    def test_numbered_nested_headings_are_not_reported_as_unrelated(self):
        notes = "## 1. Concepts\n### 1.1 Subtopic\n#### 1.1.1 Detail\n## 2. Applications"

        self.assertEqual(ReindexCourseTopicsCommand._heading_issues(notes), [])

    def test_unnumbered_top_level_heading_is_reported(self):
        self.assertEqual(
            ReindexCourseTopicsCommand._heading_issues("## 1. Concepts\n## Appendix"),
            ["unrelated heading: ## Appendix"],
        )


class NoteMathValidationTests(TestCase):
    def test_server_placement_replaces_a_model_figure_in_the_wrong_section(self):
        crop_url = "/media/approved-equilibrium.jpg"
        content = (
            "## 1. Demand\n\nDemand slopes downward as price rises.\n\n"
            f"![Equilibrium graph]({crop_url})\n\n"
            "## 2. Equilibrium\n\nThe market clears when quantity demanded equals quantity supplied."
        )
        marker = "[[VISUAL:equilibrium-figure]]"
        manifest = [{
            "id": "equilibrium-figure",
            "marker": marker,
            "crop_url": crop_url,
            "required": True,
            "auto_match_terms": ["equilibrium", "market clears"],
            "caption": "Equilibrium graph",
            "labels": [],
            "context_before": "At equilibrium the market clears.",
            "context_after": "Quantity demanded equals quantity supplied.",
        }]

        placed = _insert_required_visual_markers(content, manifest)
        image_position = placed.index(marker)
        demand_heading = placed.index("## 1. Demand")
        equilibrium_heading = placed.index("## 2. Equilibrium")

        self.assertEqual(placed.count(marker), 1)
        self.assertNotIn(crop_url, placed)
        self.assertGreater(image_position, equilibrium_heading)
        self.assertGreater(equilibrium_heading, demand_heading)

    @patch("services.prep_ai_router.requests.post")
    @override_settings(DEEPSEEK_API="test-key")
    def test_empty_deepseek_completion_is_reported_with_finish_details(self, post):
        post.return_value.status_code = 200
        post.return_value.json.return_value = {
            "id": "completion-test-123",
            "choices": [{
                "message": {"content": "", "reasoning_content": "internal only"},
                "finish_reason": "stop",
            }],
            "usage": {"prompt_tokens": 30, "completion_tokens": 0, "total_tokens": 30},
        }

        result = call_deepseek(
            [{"role": "user", "content": "Write notes."}],
            model="deepseek-flash",
            auto_continue=False,
            thinking_enabled=False,
        )

        self.assertFalse(result["success"])
        self.assertTrue(result["empty_response"])
        self.assertEqual(result["finish_reason"], "stop")
        self.assertEqual(result["response_id"], "completion-test-123")
        self.assertIn("reasoning_content_present=True", result["error"])
        self.assertEqual(result["usage"]["completion_tokens"], 0)
        self.assertEqual(post.call_args.kwargs["json"]["thinking"], {"type": "disabled"})

    @patch("services.prep_ai_router.requests.post")
    @override_settings(TOGETHERAI_API="test-key")
    def test_empty_together_repair_completion_is_not_reported_as_success(self, post):
        post.return_value.status_code = 200
        post.return_value.text = ""
        post.return_value.json.return_value = {
            "choices": [{
                "message": {"content": "", "reasoning_content": "reasoning only"},
                "finish_reason": "length",
            }],
            "usage": {"prompt_tokens": 20, "completion_tokens": 5, "total_tokens": 25},
        }

        result = call_together_repair(
            [{"role": "user", "content": "Return an old_block/new_block patch."}],
            model="test-repair-model",
        )

        self.assertFalse(result["success"])
        self.assertIn("empty final content", result["error"])
        self.assertIn("reasoning_content_present=True", result["error"])
        self.assertEqual(result["usage"]["total_tokens"], 25)
        self.assertEqual(
            post.call_args.kwargs["json"]["response_format"],
            {"type": "json_object"},
        )

    @patch("services.prep_ai_router.requests.post")
    @override_settings(TOGETHERAI_API="test-key")
    def test_together_repair_retries_without_json_mode_when_model_rejects_it(self, post):
        rejected = type("Response", (), {
            "status_code": 400,
            "text": "response_format is not supported",
        })()
        success = type("Response", (), {
            "status_code": 200,
            "text": "",
            "json": lambda self: {
                "choices": [{"message": {"content": '{"old_block":"bad","new_block":"fixed"}'}}],
                "usage": {},
            },
        })()
        post.side_effect = [rejected, success]

        result = call_together_repair(
            [{"role": "user", "content": "Return an old_block/new_block patch."}],
            model="custom-repair-model",
        )

        self.assertTrue(result["success"], result)
        self.assertEqual(post.call_count, 2)
        self.assertNotIn("response_format", post.call_args.kwargs["json"])

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

    def test_tikz_and_center_environments_are_not_misclassified_as_math(self):
        diagram = (
            "\\begin{center}\n\\begin{tikzpicture}\n"
            "\\draw (0,0) -- (1,1);\n"
            "\\end{tikzpicture}\n\\end{center}"
        )

        self.assertEqual(_latex_syntax_issues(diagram), [])

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

    def test_notes_reject_unknown_code_languages(self):
        issues = _note_completion_issues(
            "```madeuplang\nrun something\n```",
            "Sequences",
            allow_code=True,
        )

        self.assertIn("code block 1 uses unknown language 'madeuplang'", issues)

    def test_mermaid_diagram_is_not_treated_as_programming_code(self):
        content = "```mermaid\nflowchart TD\n  Start --> Finish\n```"
        source_references = [{"document_id": "approved-doc", "page_number": 12, "visuals": []}]

        issues = _note_completion_issues(
            content,
            "Sequences",
            allow_code=False,
            source_references=source_references,
        )

        self.assertNotIn("code block is not allowed for this topic", issues)
        self.assertFalse(any("unknown language" in issue for issue in issues))

    def test_embedded_figure_must_link_to_an_approved_crop(self):
        content = "![Demand graph](invented-graph.svg)"
        source_references = [{
            "document_id": "approved-doc",
            "page_number": 12,
            "visuals": [{"visual_type": "graph", "crop": "approved-page-12.jpg"}],
        }]

        issues = _note_completion_issues(
            content,
            "Sequences",
            source_references=source_references,
        )

        self.assertIn("embedded figure does not reference an approved source crop", issues)

    def test_missing_visual_references_are_flagged_for_repair_across_disciplines(self):
        examples = [
            ("Economics", "As shown in the graph, quantity demanded exceeds quantity supplied."),
            ("Physics", "As illustrated in the diagram above, the force points toward the plate."),
            ("Chemistry", "Refer to the figure below for the reaction pathway."),
        ]
        for discipline, content in examples:
            with self.subTest(discipline=discipline):
                issues = _note_completion_issues(content, "Visual Concepts")
                self.assertIn("notes refer to a figure that is not included nearby", issues)

    def test_course_front_matter_is_removed_without_removing_subject_content(self):
        source = (
            "--- Page 1 ---\nCourse code: ASC 100\nLecturer: Dr Example\n"
            "University: Example University\nDownloaded by learner@example.test\n\n"
            "--- Page 2 ---\nWhat is sociology?\n"
            "A university can be studied as a social institution."
        )

        cleaned = _strip_course_administrative_front_matter(source)

        self.assertNotIn("Dr Example", cleaned)
        self.assertNotIn("Example University", cleaned)
        self.assertNotIn("Downloaded by", cleaned)
        self.assertIn("What is sociology?", cleaned)
        self.assertIn("A university can be studied as a social institution.", cleaned)

    def test_course_administration_is_rejected_but_subject_discussion_is_allowed(self):
        self.assertTrue(_course_administrative_metadata_issues(
            "The course is taught by Dr Example at Example University."
        ))
        self.assertEqual(
            _course_administrative_metadata_issues(
                "Universities are social institutions that can be studied sociologically."
            ),
            [],
        )

    def test_visual_reference_with_nearby_figure_is_allowed(self):
        content = "As shown in the graph, the curve rises.\n\n![Approved graph](/media/approved-graph.jpg)"

        issues = _note_completion_issues(content, "Visual Concepts")

        self.assertNotIn("notes refer to a figure that is not included nearby", issues)

    def test_raw_html_image_is_rejected(self):
        sections = [
            f"## {index}. Section {index}\n\nThis section contains grounded explanatory material for students."
            for index in range(1, 5)
        ]
        sections.append(
            "## 5. Final Review\n\n"
            + '<img src="/media/invented/diagram.png">\n\n'
            + "The final review gives a source-grounded recap, explains a common misconception, "
            + "and reminds students to check their interpretation against the assigned topic."
        )
        content = "\n\n".join(sections)

        issues = _note_completion_issues(content, "Sequences")

        self.assertIn("raw HTML visual markup is not allowed; use an approved visual marker", issues)

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

    def test_escaped_pipe_in_math_table_cell_is_not_split_or_truncated(self):
        markdown = "| Expression | Meaning |\n| --- | --- |\n| $a \\| b$ | One expression cell |"

        blocks = parse_markdown_to_blocks(markdown)

        self.assertEqual(_markdown_table_issues(markdown), [])
        self.assertEqual(blocks[0]["headers"], ["Expression", "Meaning"])
        self.assertEqual(blocks[0]["rows"], [["$a \\| b$", "One expression cell"]])

    def test_json_parser_preserves_square_brackets_inside_latex_strings(self):
        repair = {
            "old_block": r"\\begin{cases} [a_k, c_k] \\end{cases}",
            "new_block": r"$$\\begin{cases} [a_k, c_k] \\end{cases}$$",
        }

        self.assertEqual(robust_json_loads(json.dumps(repair)), repair)

    @patch("services.prep_ai_router.route_math_request")
    def test_generation_pipeline_handles_notes_for_multiple_syllabus_courses(self, route_request):
        course_cases = [
            (
                "ASC 100",
                "INTRODUCTION TO  SOCIOLOGY",
                "Social Sciences",
                "Social Structure",
                "Institutions, roles, relationships, and the organization of social life",
            ),
            (
                "EET 100",
                "Macroeconomic Theory",
                "Other",
                "Theory of the consumer",
                "Preferences, constraints, and the choices consumers make",
            ),
            (
                "SMA 300",
                "Real Analysis I",
                "Mathematics",
                "Sequences",
                "Convergence, boundedness, subsequences, and Cauchy criteria",
            ),
            (
                "SST 301",
                "Programming Language for Statistics 1",
                "Computing",
                "Matrices in R",
                "Matrix creation, indexing, arithmetic, and data manipulation",
            ),
            (
                "SST 305",
                "Theory of Estimation",
                "Statistics",
                "Properties of Estimators",
                "Unbiasedness, consistency, efficiency, and sufficiency",
            ),
        ]
        headings = (
            "Core Concepts",
            "Definitions and Scope",
            "Key Properties",
            "Worked Applications",
            "Exam Review",
        )
        expected_notes = []
        for code, title, category, topic_title, focus in course_cases:
            note = "\n\n".join(
                f"## {index}. {heading}\n\n"
                f"{topic_title} in {title} concerns {focus}. "
                "Explain each idea in the approved course scope, connect it to an appropriate example, "
                "and state how learners should interpret the result."
                for index, heading in enumerate(headings, start=1)
            )
            expected_notes.append(note)
        route_request.side_effect = [
            {
                "success": True,
                "content": note,
                "model_used": "test-notes-model",
                "usage": {"total_tokens": 12},
            }
            for note in expected_notes
        ]

        for (code, title, category, topic_title, _focus), expected in zip(course_cases, expected_notes):
            course = PrepCourse.objects.create(
                code=code,
                title=title,
                slug=code.lower().replace(" ", "-"),
                category=category,
            )
            topic = PrepTopic.objects.create(
                course=course,
                order=1,
                title=topic_title,
                slug=topic_title.lower().replace(" ", "-"),
            )

            result = get_or_generate_topic_notes(
                course.code,
                topic.title,
                level="level_2",
                course_obj=course,
                topic_obj=topic,
            )

            self.assertEqual(result.get("notes"), expected, result)
            self.assertFalse(result.get("error"), result)
            cached = PrepContentCache.objects.get(topic=topic, content_type="topic_notes")
            self.assertEqual(cached.payload["validation_state"], NOTE_VALIDATION_STATE)

        self.assertEqual(route_request.call_count, len(course_cases))

    def test_note_repair_parser_accepts_fenced_json_after_a_short_preamble(self):
        repair = {"old_block": "broken equation", "new_block": "corrected equation"}
        response = "Patch:\n```json\n" + json.dumps(repair) + "\n```"

        self.assertEqual(_parse_topic_note_repair_patch(response), repair)

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
            "solution", course.code, question[:50], "profile-v1", "topic-content-rules-v0", "explanatory-v1"
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
    def test_empty_repair_response_is_retried_with_explicit_json_feedback(self, repair_request):
        signature = _topic_notes_cache_signature(
            self.course, self.topic, self.topic.title, self.topic.subtopics
        )
        cache_key = compute_cache_key(
            "notes", NOTES_CACHE_VERSION, self.course.code, self.topic.title, "level_2", signature
        )
        valid_equation = "$$\n\\left\\lvert a_m-a_n\\right\\rvert \\leq \\varepsilon\n$$"
        broken_block = "$$\n\\left\\lvert a_m-a_n\\right\n\n\\right\\rvert\n$$"
        broken_notes = self.valid_notes.replace(valid_equation, broken_block)
        PrepContentCache.objects.create(
            cache_key=cache_key,
            content_type="topic_notes",
            prompt_hash="empty-repair-response",
            payload={"content": broken_notes, "level": "level_2"},
            course=self.course,
            topic=self.topic,
        )
        repair_request.side_effect = [
            {
                "success": False,
                "error": "Together repair returned empty final content (finish_reason=length).",
                "usage": {"total_tokens": 5},
            },
            {
                "success": True,
                "content": (
                    "```json\n"
                    + json.dumps({"old_block": broken_block, "new_block": valid_equation})
                    + "\n```"
                ),
                "usage": {"total_tokens": 8},
            },
        ]

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertTrue(result.get("repaired"), result)
        self.assertEqual(result["notes"].strip(), self.valid_notes.strip())
        self.assertEqual(repair_request.call_count, 2)
        self.assertIn("previous response was rejected", repair_request.call_args_list[1].args[0][1]["content"])
        self.assertEqual(result["usage"]["total_tokens"], 13)

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
            "usage": {"prompt_tokens": 80, "completion_tokens": 20, "total_tokens": 100},
        }
        repair_request.return_value = {
            "success": True,
            "content": json.dumps({
                "old_block": broken_block,
                "new_block": "$$\n\\left\\lvert a_m-a_n\\right\\rvert \\leq \\varepsilon\n$$",
            }),
            "usage": {"prompt_tokens": 10, "completion_tokens": 15, "total_tokens": 25},
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
        self.assertEqual(result["usage"]["total_tokens"], 125)
        repair_request.assert_called_once()
        prompt = route_request.call_args.args[0]
        self.assertIn("Teach as if explaining the idea to a child for the first time", prompt)
        self.assertIn("Use familiar everyday words, short sentences, and one new idea at a time", prompt)
        self.assertIn("give its meaning immediately in plain words", prompt)
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

    @patch("services.prep_ai_router.call_together_repair", return_value={"success": False, "error": "repair unavailable"})
    @patch("services.prep_ai_router.route_math_request")
    def test_unrepaired_missing_figure_wording_does_not_block_self_contained_notes(
        self,
        route_request,
        repair_request,
    ):
        self_contained_notes = self.valid_notes.replace(
            "## 3. Three\n\nText.",
            "## 3. Three\n\nAs shown in the graph, the quantity rises. The relationship is explained here in text.",
        )
        route_request.return_value = {
            "success": True,
            "content": self_contained_notes,
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

        self.assertEqual(result["notes"].strip(), self_contained_notes.strip())
        self.assertTrue(result.get("validation_failed") is not True)
        self.assertEqual(repair_request.call_count, 3)
        cache = PrepContentCache.objects.get(topic=self.topic, content_type="topic_notes")
        self.assertEqual(cache.payload.get("validation_state"), NOTE_VALIDATION_STATE)
        self.assertFalse(PrepNoteGenerationGuard.objects.filter(topic=self.topic, level="level_2").exists())

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
        PrepCourseEnrollment.objects.get_or_create(user=self.user, course=self.course)
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

    @patch("prep.views.get_or_generate_topic_notes")
    def test_active_trial_queues_missing_level_two_notes_without_blocking_web_request(self, generate_notes):
        PrepCourseEnrollment.objects.get_or_create(user=self.user, course=self.course)
        wallet = PrepWallet.get_or_create_wallet(self.user)
        wallet.credit_grants.update(remaining_credits=0)
        wallet.credits_balance = 0
        wallet.save(update_fields=["credits_balance"])
        generate_notes.side_effect = [
            {"notes": "", "generation_required": True, "cached": False},
            {
                "notes": self.valid_notes,
                "cached": False,
                "level": "level_2",
                "model": "test-model",
                "usage": {"total_tokens": 1500},
            },
        ]
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("prep:api_topic_notes"),
            data=json.dumps({"topic_id": self.topic.pk, "level": "level_2"}),
            content_type="application/json",
        )

        wallet.refresh_from_db()
        self.assertEqual(response.status_code, 202)
        self.assertTrue(response.json()["pending"])
        self.assertTrue(
            PrepTopicNotesJob.objects.filter(
                topic=self.topic,
                level="level_2",
                status="pending",
            ).exists()
        )
        self.assertEqual(wallet.credits_balance, 0)
        self.assertEqual(generate_notes.call_count, 1)

    @patch("prep.views.get_or_generate_topic_notes")
    def test_missing_topic_notes_are_queued_and_pending_jobs_are_pollable(self, note_service):
        PrepCourseEnrollment.objects.get_or_create(user=self.user, course=self.course)
        note_service.return_value = {
            "notes": "",
            "generation_required": True,
            "cached": False,
        }
        self.client.force_login(self.user)

        request_data = {"topic_id": self.topic.pk, "level": "level_1"}
        response = self.client.post(
            reverse("prep:api_topic_notes"),
            data=json.dumps(request_data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 202)
        self.assertTrue(response.json()["pending"])
        job_id = response.json()["job_id"]
        poll_response = self.client.post(
            reverse("prep:api_topic_notes"),
            data=json.dumps({**request_data, "job_id": job_id}),
            content_type="application/json",
        )

        self.assertEqual(poll_response.status_code, 202)
        self.assertEqual(poll_response.json()["status"], "pending")
        self.assertEqual(note_service.call_count, 1)

    def test_failed_topic_notes_job_returns_safe_json_error(self):
        PrepCourseEnrollment.objects.get_or_create(user=self.user, course=self.course)
        job = PrepTopicNotesJob.objects.create(
            topic=self.topic,
            level="level_1",
            source_signature="a" * 64,
            status="failed",
            last_error="Provider returned a private internal error.",
        )
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("prep:api_topic_notes"),
            data=json.dumps({
                "topic_id": self.topic.pk,
                "level": "level_1",
                "job_id": job.pk,
            }),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 502)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(
            response.json()["error"],
            "Notes could not be prepared right now. Please retry in a moment.",
        )
        self.assertNotIn("private internal error", response.content.decode("utf-8"))

    @patch(
        "services.prep_ai_router.get_published_topic_note_levels",
        return_value={"level_1": valid_notes},
    )
    def test_completed_topic_notes_job_returns_published_notes_as_json(self, published_notes):
        PrepCourseEnrollment.objects.get_or_create(user=self.user, course=self.course)
        job = PrepTopicNotesJob.objects.create(
            topic=self.topic,
            level="level_1",
            source_signature="c" * 64,
            status="complete",
        )
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("prep:api_topic_notes"),
            data=json.dumps({
                "topic_id": self.topic.pk,
                "level": "level_1",
                "job_id": job.pk,
            }),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertTrue(response.json()["success"])
        self.assertEqual(response.json()["notes"], self.valid_notes)
        published_notes.assert_called_once()

    @patch("services.prep_ai_router.route_math_request")
    @patch("prep.views.get_available_credits", return_value=100)
    def test_stale_proof_solution_is_not_returned_for_social_science(self, _credits, route_request):
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
        route_request.return_value = {
            "success": True,
            "content": "## Explanation and Analysis\n\nA source-grounded answer that explains the concept clearly without a proof scaffold.",
            "model_used": "test-model",
            "usage": {"total_tokens": 10},
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
        question.refresh_from_db()
        self.assertIn("Explanation and Analysis", question.solution_latex)
        self.assertNotIn("Step-by-Step Rigorous Proof", question.solution_latex)
        route_request.assert_called_once()

    @patch("prep.views.get_or_generate_question_solution")
    def test_pending_question_with_stored_solution_is_blocked_before_api_cache_return(self, generate_solution):
        question = PrepQuestion.objects.create(
            topic=self.topic,
            question_type="authentic",
            number=8,
            marks=10,
            topic_label=self.topic.title,
            question_latex="Pending source question.",
            solution_latex="Stale solution must not be shown.",
            verification_status="pending",
        )
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("prep:api_solve_question"),
            data=json.dumps({"question_id": question.id}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 409)
        self.assertIn("pending tutor review", response.json()["error"])
        self.assertNotIn("solution", response.json())
        generate_solution.assert_not_called()

    @patch("services.prep_ai_router.route_math_request")
    def test_service_does_not_answer_flagged_question_object(self, route_request):
        question = PrepQuestion.objects.create(
            topic=self.topic,
            question_type="authentic",
            number=9,
            marks=5,
            topic_label=self.topic.title,
            question_latex="Unreadable source question.",
            verification_status="flagged",
        )

        result = get_or_generate_question_solution(
            question.question_latex,
            self.course.code,
            topic_label=self.topic.title,
            question_obj=question,
        )

        self.assertEqual(result["solution"], "")
        self.assertIn("pending tutor review", result["error"])
        route_request.assert_not_called()

    @patch("services.prep_ai_router.route_math_request")
    def test_answer_cache_tracks_approved_source_and_rejects_invalid_cached_figure(self, route_request):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            source = PrepDocument.objects.create(
                course=self.course,
                doc_type="Lecture Notes",
                topic_name=self.topic.title,
                file=SimpleUploadedFile("sequence-answer-notes.pdf", b"source PDF"),
                extracted_text="--- Page 8 ---\nA bounded monotone sequence converges to a finite limit.",
                file_sha256="9" * 64,
                stage="stage_3",
            )
            question = PrepQuestion.objects.create(
                paper=None,
                topic=self.topic,
                source_document=source,
                source_page_number=8,
                question_type="authentic",
                number=10,
                marks=6,
                topic_label=self.topic.title,
                question_latex="Explain why a bounded monotone sequence converges.",
                verification_status="auto_validated",
            )
            answer = "A bounded monotone sequence converges because its terms approach the supremum or infimum of its range."
            route_request.side_effect = [
                {"success": True, "content": answer, "model_used": "test-model", "usage": {"total_tokens": 10}},
                {"success": True, "content": answer + " The source's hypotheses must still be checked.", "model_used": "test-model", "usage": {"total_tokens": 12}},
                {"success": True, "content": answer, "model_used": "test-model", "usage": {"total_tokens": 10}},
            ]

            with patch("services.prep_ai_router.store_cached_content", wraps=store_cached_content) as cache_writer:
                first = get_or_generate_question_solution(
                    question.question_latex,
                    self.course.code,
                    topic_label=self.topic.title,
                    question_obj=question,
                )
            self.assertTrue(first.get("solution"), first)
            cache_writer.assert_called_once()
            cache_rows = list(PrepContentCache.objects.filter(content_type="solution_derivation").values(
                "cache_key", "course_id", "topic_id", "payload"
            ))
            self.assertTrue(cache_rows, {"cache_writer_call": str(cache_writer.call_args), "course_id": str(self.course.pk)})
            first_cache = PrepContentCache.objects.get(content_type="solution_derivation", course=self.course)

            self.assertEqual(first["solution"], answer)
            self.assertEqual(first_cache.payload["answer_validation_version"], ANSWER_VALIDATION_VERSION)
            self.assertEqual(first_cache.payload["source_references"][0]["document_id"], str(source.pk))
            self.assertEqual(first_cache.payload["source_references"][0]["page_number"], 8)
            self.assertIn("question type authentic", route_request.call_args_list[0].args[0])
            self.assertIn("Page 8", route_request.call_args_list[0].args[0])

            source.extracted_text = "--- Page 8 ---\nThe source now describes an alternating sequence and a different limit argument."
            source.save(update_fields=["extracted_text"])
            question.solution_latex = ""
            question.save(update_fields=["solution_latex"])
            second = get_or_generate_question_solution(
                question.question_latex,
                self.course.code,
                topic_label=self.topic.title,
                question_obj=question,
            )
            self.assertFalse(second["cached"])
            self.assertEqual(route_request.call_count, 2)

            second_cache = PrepContentCache.objects.exclude(pk=first_cache.pk).get(
                content_type="solution_derivation",
                course=self.course,
            )
            second_cache.payload["solution"] = "![Unapproved answer figure](/media/fake/plot.png)"
            second_cache.save(update_fields=["payload"])
            question.solution_latex = ""
            question.save(update_fields=["solution_latex"])

            third = get_or_generate_question_solution(
                question.question_latex,
                self.course.code,
                topic_label=self.topic.title,
                question_obj=question,
            )

            self.assertEqual(third["solution"], answer)
            self.assertNotIn("Unapproved answer figure", third["solution"])
            self.assertFalse(third["cached"])
            self.assertEqual(route_request.call_count, 3)

    @patch("prep.views.get_or_generate_topic_notes")
    def test_rejected_note_generation_is_not_reported_as_a_server_error(self, generate_notes):
        generate_notes.return_value = {
            "notes": "",
            "error": "The notes generation was incomplete. Please retry.",
            "validation_failed": True,
        }
        PrepCourseEnrollment.objects.get_or_create(user=self.user, course=self.course)
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("prep:api_topic_notes"),
            data='{ "topic_id": "%s", "level": "level_2" }' % self.topic.id,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 422)

    @patch("prep.views.get_or_generate_topic_notes", side_effect=RuntimeError("provider output failed"))
    def test_unexpected_notes_api_failure_returns_json_and_logs_internal_exception(self, generate_notes):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("prep:api_topic_notes"),
            data=json.dumps({
                "course_code": self.course.code,
                "topic_title": "Sequences",
                "level": "level_2",
            }),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(response.json()["success"], False)
        self.assertIn("server error", response.json()["error"])
        self.assertNotIn("provider output failed", response.content.decode("utf-8"))
        generate_notes.assert_called_once()

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
        self.assertEqual(cache.payload["source_references"], [])
        self.assertTrue(cache.payload["source_signature"])

        second_read = get_published_topic_note_levels(self.topic)
        self.assertEqual(second_read["level_2"], self.valid_notes.strip())

    def test_legacy_note_is_refreshed_with_required_visual_before_publication(self):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            source = PrepDocument.objects.create(
                course=self.course,
                topic_name="Full syllabus",
                file=SimpleUploadedFile("sequence-source.pdf", b"pdf"),
                extracted_text="--- Page 1 ---\nSequence convergence is illustrated by the source graph.",
                stage="stage_3",
            )
            visual = PrepDocumentVisual.objects.create(
                document=source,
                candidate_key="c3" * 32,
                page_number=1,
                bbox=[10, 20, 210, 160],
                crop=SimpleUploadedFile("sequence.jpg", b"sequence", content_type="image/jpeg"),
                context_crop=SimpleUploadedFile("sequence-context.jpg", b"context", content_type="image/jpeg"),
                visual_type="graph",
                status="approved",
                extracted_content={
                    "auto_topic": self.topic.title,
                    "auto_decision": "approved_high_confidence",
                    "auto_match_terms": ["sequence", "convergence"],
                    "context_after": "Sequence convergence is illustrated by the source graph.",
                },
            )
            legacy_content = self.valid_notes.replace(
                "## 1. One\n\nText.",
                "## 1. One\n\nSequence convergence is illustrated by the source graph.",
            )
            cache = PrepContentCache.objects.create(
                cache_key="notes:legacy:validation-testing:sequences:level_2",
                content_type="topic_notes",
                prompt_hash="legacy-without-visual-routing",
                payload={"content": legacy_content, "level": "level_2"},
                course=self.course,
                topic=self.topic,
            )

            published = get_published_topic_note_levels(self.topic)

            cache.refresh_from_db()
            self.assertIn(f"]({visual.crop.url})", published["level_2"])
            self.assertEqual(cache.payload["validation_state"], NOTE_VALIDATION_STATE)
            self.assertEqual(
                str(visual.pk),
                cache.payload["source_references"][0]["visuals"][0]["visual_id"],
            )

    def test_topic_rule_change_unpublishes_notes_from_the_previous_rule_version(self):
        PrepContentCache.objects.create(
            cache_key="notes:published:validation-testing:sequences:topic-rules-v0",
            content_type="topic_notes",
            prompt_hash="published-before-topic-rule-change",
            payload={
                "content": self.valid_notes,
                "level": "level_2",
                "validation_state": NOTE_VALIDATION_STATE,
                "source_signature": _topic_notes_cache_signature(
                    self.course,
                    self.topic,
                    self.topic.title,
                    self.topic.subtopics,
                ),
                "study_profile_version": self.course.study_profile_version,
                "topic_content_rules_version": self.topic.content_rules_version,
            },
            course=self.course,
            topic=self.topic,
        )
        self.assertIn("level_2", get_published_topic_note_levels(self.topic, validated_only=True))

        self.topic.content_rules = {
            "schema_version": 1,
            "modalities": {
                "graphs": {
                    "policy": "disallowed",
                    "rationale": "Graphs are not part of this topic's approved source.",
                },
            },
        }
        self.topic.save(update_fields=["content_rules"])
        self.topic.refresh_from_db()

        self.assertEqual(self.topic.content_rules_version, 1)
        self.assertEqual(get_published_topic_note_levels(self.topic, validated_only=True), {})

    def test_old_validated_visual_routing_cache_is_not_published(self):
        for version, signature in (
            ("validated-v3-source-modalities", "old-routing-signature"),
            (NOTE_VALIDATION_STATE, "old-routing-signature"),
        ):
            PrepContentCache.objects.create(
                cache_key=f"notes:published:validation-testing:sequences:{version}",
                content_type="topic_notes",
                prompt_hash=version,
                payload={
                    "content": self.valid_notes,
                    "level": "level_2",
                    "validation_state": version,
                    "source_signature": signature,
                    "study_profile_version": self.course.study_profile_version,
                    "topic_content_rules_version": self.topic.content_rules_version,
                },
                course=self.course,
                topic=self.topic,
            )

        self.assertEqual(get_published_topic_note_levels(self.topic), {})

    def test_currently_marked_cache_with_blank_figure_map_is_not_published(self):
        malformed = (
            self.valid_notes
            + "\n\n### Figure Recall Map\n\n"
            + "| Figure marker | Concept |\n|---|---|\n|  | Demand curve |\n\n"
            + "The figures ( and ) illustrate demand shifts."
        )
        PrepContentCache.objects.create(
            cache_key="notes:published:validation-testing:sequences:malformed-figure-map",
            content_type="topic_notes",
            prompt_hash="current-but-malformed",
            payload={
                "content": malformed,
                "level": "level_2",
                "validation_state": NOTE_VALIDATION_STATE,
                "source_signature": _topic_notes_cache_signature(
                    self.course,
                    self.topic,
                    self.topic.title,
                    self.topic.subtopics,
                ),
                "study_profile_version": self.course.study_profile_version,
                "topic_content_rules_version": self.topic.content_rules_version,
            },
            course=self.course,
            topic=self.topic,
        )

        self.assertEqual(get_published_topic_note_levels(self.topic), {})

    def test_note_validation_requires_every_high_confidence_source_visual(self):
        references = [{"visuals": [{
            "visual_id": str(index),
            "crop_url": f"/media/figure-{index}.jpg",
            "auto_topic": self.topic.title,
            "auto_decision": "approved_high_confidence",
        } for index in range(1, 8)]}]

        issues = _note_completion_issues(
            self.valid_notes,
            self.topic.title,
            source_references=references,
        )

        self.assertTrue(any(issue.startswith("required approved source visual missing:") for issue in issues), issues)
        manifest = _approved_visual_manifest(references)
        self.assertEqual(len(manifest), 7)
        self.assertTrue(all(visual["required"] for visual in manifest))

    def test_note_validation_rejects_blank_figure_markers_and_placeholders(self):
        content = (
            self.valid_notes
            + "\n\n### Figure Recall Map\n\n"
            + "| Figure marker | Concept |\n|---|---|\n|  | Demand curve |\n\n"
            + "The two demand figures ( and ) illustrate the shifts."
        )

        issues = _note_completion_issues(content, "Sequences")

        self.assertTrue(any(issue.startswith("figure marker table row has no figure") for issue in issues), issues)
        self.assertIn("figure summary contains empty reference placeholders", issues)

    def test_note_validation_accepts_source_image_in_figure_marker_table(self):
        image_url = "/media/ppf.jpg"
        content = (
            self.valid_notes
            + f"\n\n| Figure marker | Concept |\n|---|---|\n| ![PPF]({image_url}) | Production possibility frontier |"
        )
        references = [{"visuals": [{"crop_url": image_url}]}]

        issues = _note_completion_issues(content, "Sequences", source_references=references)

        self.assertFalse(any(issue.startswith("figure marker table row has no figure") for issue in issues), issues)

    def test_approved_coursework_source_is_available_to_note_generation(self):
        PrepDocument.objects.create(
            course=self.course,
            topic_name="Full Syllabus",
            extracted_text="Approved R example: mean(c(1, 2, 3))",
            stage="stage_3",
        )

        source = _approved_course_source_context(self.course, "Sequences")

        self.assertIn("Approved R example", source)

    @patch("services.prep_ai_router._repair_invalid_note_cache", return_value=None)
    @patch("services.prep_ai_router.route_math_request")
    def test_all_levels_reject_topic_disallowed_graphs_before_validation_cache(self, route_request, _repair):
        course_rules = {
            "schema_version": 1,
            "modalities": {
                modality: {"policy": "allowed", "evidence_required": True}
                for modality in CONTENT_MODALITIES
            },
        }
        course_rules["modalities"]["text"]["policy"] = "required"
        self.course.study_profile = {
            "subject_family": "statistics",
            "capabilities": {"code": False, "math_notation": True, "chemical_equations": False},
            "content_rules": course_rules,
        }
        self.course.study_profile_version = 1
        self.course.save(update_fields=["study_profile", "study_profile_version"])
        self.topic.content_rules = {
            "schema_version": 1,
            "modalities": {
                "graphs": {
                    "policy": "disallowed",
                    "rationale": "The approved topic source does not support generated graphs.",
                },
            },
        }
        self.topic.save(update_fields=["content_rules"])
        invalid_notes = self.valid_notes.replace(
            "This final section has enough explanatory material",
            "![Unsupported graph](generated-graph.svg)\n\n"
            "This final section has enough explanatory material",
        )
        route_request.return_value = {
            "success": True,
            "content": invalid_notes,
            "model_used": "test-notes-model",
            "usage": {},
        }

        for level in ("level_1", "level_2", "level_3"):
            result = get_or_generate_topic_notes(
                self.course.code,
                self.topic.title,
                level=level,
                course_obj=self.course,
                topic_obj=self.topic,
            )

            self.assertTrue(result.get("validation_failed"), result)
            self.assertEqual(result.get("notes"), "")

        self.assertEqual(route_request.call_count, 3)
        for cache in PrepContentCache.objects.filter(topic=self.topic, content_type="topic_notes"):
            self.assertNotEqual(cache.payload.get("validation_state"), NOTE_VALIDATION_STATE)

    @patch("services.prep_ai_router._repair_invalid_note_cache", return_value=None)
    @patch("services.prep_ai_router.route_math_request")
    def test_all_levels_reject_sociology_proof_scaffolds_before_validation_cache(self, route_request, _repair):
        self.course.study_profile = {
            "subject_family": "social_science",
            "capabilities": {"code": False, "math_notation": False, "chemical_equations": False},
            "note_structure": ["One", "Two", "Three", "Four", "Five"],
        }
        self.course.study_profile_version = 1
        self.course.save(update_fields=["study_profile", "study_profile_version"])
        invalid_notes = self.valid_notes.replace(
            "## 2. Two",
            "## 2. Step-by-Step Rigorous Proof / Derivation",
        )
        route_request.return_value = {
            "success": True,
            "content": invalid_notes,
            "model_used": "test-notes-model",
            "usage": {},
        }

        for level in ("level_1", "level_2", "level_3"):
            result = get_or_generate_topic_notes(
                self.course.code,
                self.topic.title,
                level=level,
                course_obj=self.course,
                topic_obj=self.topic,
            )

            self.assertTrue(result.get("validation_failed"), result)
            self.assertEqual(result.get("notes"), "")

        self.assertEqual(route_request.call_count, 3)
        for cache in PrepContentCache.objects.filter(topic=self.topic, content_type="topic_notes"):
            self.assertNotEqual(cache.payload.get("validation_state"), NOTE_VALIDATION_STATE)

    @patch("services.prep_ai_router.route_math_request")
    def test_invalid_approved_rules_stop_note_generation_before_model_call(self, route_request):
        self.course.study_profile = {
            "subject_family": "statistics",
            "capabilities": {"code": True, "math_notation": True},
            "content_rules": {"schema_version": 99, "modalities": {}},
        }
        self.course.study_profile_version = 1
        self.course.save(update_fields=["study_profile", "study_profile_version"])

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertTrue(result.get("validation_failed"), result)
        self.assertEqual(result.get("notes"), "")
        route_request.assert_not_called()

    @patch("services.prep_ai_router.route_math_request")
    def test_generated_note_cache_keeps_approved_page_and_figure_references(self, route_request):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            signature_before_source = _topic_notes_cache_signature(
                self.course, self.topic, self.topic.title, self.topic.subtopics
            )
            source = PrepDocument.objects.create(
                course=self.course,
                topic_name="Sequences",
                file=SimpleUploadedFile("sequence-notes.pdf", b"pdf"),
                extracted_text=(
                    "--- Page 4 ---\nSequences are bounded and convergent. "
                    "An approved sequence graph illustrates the limit."
                ),
                file_sha256="d" * 64,
                stage="stage_3",
            )
            visual = PrepDocumentVisual.objects.create(
                document=source,
                candidate_key="e" * 64,
                page_number=4,
                bbox=[20, 30, 200, 240],
                crop="prep/visual-crops/sequence-page-4.jpg",
                visual_type="graph",
                status="approved",
                extracted_content={
                    "caption": "Sequence limit illustration",
                    "auto_topic": self.topic.title,
                    "auto_decision": "approved_high_confidence",
                    "auto_match_terms": ["sequence", "convergence"],
                    "context_after": "The sequence graph illustrates convergence.",
                },
            )
            route_request.return_value = {
                "success": True,
                "content": self.valid_notes.replace(
                    "## 1. One\n\nText.",
                    "## 1. One\n\nThe sequence graph illustrates convergence.",
                ),
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

            signature_after_source = _topic_notes_cache_signature(
                self.course, self.topic, self.topic.title, self.topic.subtopics
            )
            cache = PrepContentCache.objects.get(topic=self.topic, content_type="topic_notes")
            references = cache.payload["source_references"]
            self.assertTrue(result["notes"], result)
            self.assertNotEqual(signature_before_source, signature_after_source)
            self.assertEqual(references[0]["document_id"], str(source.pk))
            self.assertEqual(references[0]["source_sha256"], "d" * 64)
            self.assertEqual(references[0]["page_number"], 4)
            self.assertEqual(references[0]["visuals"][0]["visual_id"], str(visual.pk))
            self.assertEqual(references[0]["visuals"][0]["crop"], visual.crop.name)
            self.assertEqual(references[0]["visuals"][0]["crop_url"], visual.crop.url)

    @patch("services.prep_ai_router.route_math_request")
    def test_approved_visual_marker_resolves_to_crop_url_before_cache(self, route_request):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            source = PrepDocument.objects.create(
                course=self.course,
                topic_name="Sequences",
                file=SimpleUploadedFile("sequence-figure.pdf", b"pdf"),
                extracted_text=(
                    "--- Page 4 ---\n2: Other Topic\n"
                    "Sequences have terms that approach a limit; Figure 2 shows the source graph."
                ),
                file_sha256="f" * 64,
                stage="stage_3",
            )
            PrepTopic.objects.create(
                course=self.course,
                order=2,
                title="Other Topic",
                slug="other-topic",
            )
            visual = PrepDocumentVisual.objects.create(
                document=source,
                candidate_key="f1" * 32,
                page_number=4,
                bbox=[10, 20, 210, 160],
                crop=SimpleUploadedFile("sequence-plot.jpg", b"approved-crop", content_type="image/jpeg"),
                visual_type="graph",
                labels=["n", "a_n"],
                extracted_content={
                    "caption": "Sequence terms",
                    "context_before": "Sequence terms approach a finite limit.",
                    "auto_topic": self.topic.title,
                    "auto_decision": "tutor_approved",
                    "auto_match_method": "tutor_review",
                },
                status="approved",
                reviewed_topic=self.topic,
                reviewed_by=self.user,
                reviewed_at=self.user.date_joined,
            )
            unapproved_visual = PrepDocumentVisual.objects.create(
                document=source,
                candidate_key="f2" * 32,
                page_number=4,
                bbox=[15, 25, 215, 165],
                crop=SimpleUploadedFile("unreviewed-plot.jpg", b"unreviewed-crop", content_type="image/jpeg"),
                visual_type="graph",
                labels=["wrong", "labels"],
                status="needs_review",
            )
            marker = f"[[VISUAL:{visual.pk}]]"
            generated = self.valid_notes.replace(
                "## 3. Three",
                f"{marker}\n\n## 3. Three\n\nSequence terms approach a finite limit.",
            )
            route_request.return_value = {
                "success": True,
                "content": generated,
                "model_used": "test-model",
                "usage": {},
            }

            result = get_or_generate_topic_notes(
                self.course.code,
                self.topic.title,
                level="level_2",
                course_obj=self.course,
                topic_obj=self.topic,
            )

            cache = PrepContentCache.objects.get(topic=self.topic, content_type="topic_notes")
            prompt = route_request.call_args.args[0]
            self.assertIn(f"]({visual.crop.url})", result["notes"])
            self.assertNotIn("[[VISUAL:", result["notes"])
            self.assertIn(marker, prompt)
            self.assertNotIn(f"[[VISUAL:{unapproved_visual.pk}]]", prompt)
            self.assertEqual(cache.payload["validation_state"], NOTE_VALIDATION_STATE)
            self.assertEqual(cache.payload["source_references"][0]["visuals"][0]["visual_id"], str(visual.pk))

    def test_topic_assigned_visual_includes_page_without_topic_title_keyword(self):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            source = PrepDocument.objects.create(
                course=self.course,
                topic_name="Full syllabus",
                file=SimpleUploadedFile("source-pages.pdf", b"pdf"),
                extracted_text=(
                    "--- Page 2 ---\nThe course introduces sequences.\n\n"
                    "--- Page 4 ---\nThe PPF illustrates scarcity and opportunity cost."
                ),
                file_sha256="a" * 64,
                stage="stage_3",
            )
            visual = PrepDocumentVisual.objects.create(
                document=source,
                candidate_key="a1" * 32,
                page_number=4,
                bbox=[10, 20, 210, 160],
                crop=SimpleUploadedFile("ppf.jpg", b"ppf-crop", content_type="image/jpeg"),
                context_crop=SimpleUploadedFile("ppf-context.jpg", b"page-context", content_type="image/jpeg"),
                visual_type="graph",
                status="approved",
                extracted_content={
                    "auto_topic": self.topic.title,
                    "auto_decision": "approved_high_confidence",
                    "auto_match_terms": ["opportunity", "cost"],
                    "context_before": "The straight PPF illustrates constant opportunity cost.",
                    "context_after": "Beans and maize production possibilities.",
                },
            )

            references = _approved_course_source_references(self.course, self.topic.title)

            self.assertIn(4, [reference["page_number"] for reference in references])
            figure = next(
                item for reference in references for item in reference["visuals"]
                if item["visual_id"] == str(visual.pk)
            )
            self.assertEqual(figure["auto_topic"], self.topic.title)
            self.assertEqual(figure["context_before"], "The straight PPF illustrates constant opportunity cost.")
            self.assertTrue(figure["context_crop_url"])

    def test_visual_from_next_pdf_topic_section_is_excluded(self):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            other_topic = PrepTopic.objects.create(
                course=self.course,
                order=2,
                title="Other Topic",
                slug="other-topic",
            )
            source = PrepDocument.objects.create(
                course=self.course,
                topic_name="Full syllabus",
                file=SimpleUploadedFile("sectioned-source.pdf", b"pdf"),
                extracted_text=(
                    "--- Page 1 ---\n1: Sequences\nA sequence graph appears here.\n\n"
                    "--- Page 2 ---\nTopic 2: Other Topic\nA second topic figure appears here."
                ),
                stage="stage_3",
            )
            visual = PrepDocumentVisual.objects.create(
                document=source,
                candidate_key="b2" * 32,
                page_number=2,
                bbox=[10, 20, 210, 160],
                crop=SimpleUploadedFile("other-topic.jpg", b"other-topic", content_type="image/jpeg"),
                visual_type="graph",
                status="approved",
                extracted_content={
                    "auto_topic": self.topic.title,
                    "auto_decision": "approved_high_confidence",
                },
            )

            references = _approved_course_source_references(self.course, self.topic.title)

            self.assertNotIn(2, [reference["page_number"] for reference in references])
            self.assertNotIn(
                str(visual.pk),
                [item["visual_id"] for reference in references for item in reference["visuals"]],
            )
            self.assertEqual(other_topic.title, "Other Topic")

    def test_required_visual_is_inserted_after_matching_note_paragraph(self):
        notes = (
            "## 1. Concepts\n\n"
            "Scarcity means limited resources and opportunity cost is the next best alternative.\n\n"
            "## 2. Applications\n\n"
            "Economic choices affect the production of goods."
        )
        manifest = [{
            "marker": "[[VISUAL:123]]",
            "required": True,
            "auto_match_terms": ["opportunity", "cost", "scarcity"],
            "context_before": "The straight PPF illustrates opportunity cost.",
            "context_after": "Resources produce beans and maize.",
        }]

        updated = _insert_required_visual_markers(notes, manifest)

        self.assertLess(updated.index("opportunity cost"), updated.index("[[VISUAL:123]]"))
        self.assertLess(updated.index("[[VISUAL:123]]"), updated.index("## 2."))

    def test_sibling_figure_context_is_scoped_by_source_order_for_caption_and_placement(self):
        shared_context = (
            "Graph 1: The substitute-price curve slopes upward. "
            "Graph 2: The complement-price curve slopes downward."
        )
        references = [{
            "page_number": 14,
            "visuals": [
                {
                    "visual_id": "right-graph",
                    "page_number": 14,
                    "bbox": [300, 20, 500, 200],
                    "crop_url": "/media/right-graph.jpg",
                    "auto_topic": "Price theory",
                    "auto_decision": "approved_high_confidence",
                    "context_after": shared_context,
                },
                {
                    "visual_id": "left-graph",
                    "page_number": 14,
                    "bbox": [20, 20, 220, 200],
                    "crop_url": "/media/left-graph.jpg",
                    "auto_topic": "Price theory",
                    "auto_decision": "approved_high_confidence",
                    "context_after": shared_context,
                },
            ],
        }]
        manifest = _approved_visual_manifest(references)
        captions = {visual["id"]: visual["caption"].lower() for visual in manifest}
        notes = (
            "## 1. Substitutes\n\nA fall in the price of a substitute reduces demand.\n\n"
            "## 2. Complements\n\nA fall in the price of a complement raises demand."
        )

        placed = _insert_required_visual_markers(notes, manifest)

        self.assertIn("substitute-price", captions["left-graph"])
        self.assertIn("complement-price", captions["right-graph"])
        self.assertLess(placed.index("[[VISUAL:left-graph]]"), placed.index("## 2. Complements"))
        self.assertGreater(placed.index("[[VISUAL:right-graph]]"), placed.index("## 2. Complements"))

    def test_approved_visual_is_not_duplicated_in_one_note_level(self):
        image = "![PPF](https://example.test/ppf.jpg)"
        notes = f"Explanation one.\n\n{image}\n\nExplanation two.\n\n{image}"
        references = [{"visuals": [{"crop_url": "https://example.test/ppf.jpg"}]}]

        deduplicated = _dedupe_approved_visual_images(notes, references)

        self.assertEqual(deduplicated.count(image), 1)

    def test_approved_visual_caption_uses_neighboring_source_evidence(self):
        image = "![Unclassified (source page 4)](/media/ppf.jpg)"
        references = [{"visuals": [{
            "crop_url": "/media/ppf.jpg",
            "caption": "The slope of the PPF is marginal rate of transformation (MRT).",
        }]}]

        updated = _normalize_approved_visual_captions(image, references)

        self.assertEqual(
            updated,
            "![The slope of the PPF is marginal rate of transformation (MRT).](/media/ppf.jpg)",
        )

    def test_approved_visual_caption_falls_back_to_neighboring_text(self):
        image = "![Unclassified (source page 4)](/media/ppf.jpg)"
        references = [{"visuals": [{
            "crop_url": "/media/ppf.jpg",
            "context_after": "The straight PPF represents constant opportunity cost.",
        }]}]

        updated = _normalize_approved_visual_captions(image, references)

        self.assertEqual(
            updated,
            "![The straight PPF represents constant opportunity cost.](/media/ppf.jpg)",
        )

    def test_approved_visual_caption_ignores_download_footer(self):
        image = "![Unclassified (source page 23)](/media/equilibrium.jpg)"
        references = [{"visuals": [{
            "crop_url": "/media/equilibrium.jpg",
            "visual_type": "graph",
            "context_after": "Downloaded by Student Example (student@example.test)",
            "context_before": "The equilibrium graph shows excess demand when price rises above equilibrium.",
        }]}]

        updated = _normalize_approved_visual_captions(image, references)

        self.assertEqual(
            updated,
            "![The equilibrium graph shows excess demand when price rises above equilibrium.](/media/equilibrium.jpg)",
        )

    def test_approved_visual_caption_uses_generic_type_when_context_is_only_a_footer(self):
        image = "![Downloaded by Student Example (source page 23)](/media/graph.jpg)"
        references = [{"visuals": [{
            "crop_url": "/media/graph.jpg",
            "visual_type": "graph",
            "context_after": "Downloaded by Student Example (student@example.test)",
            "context_before": "lOMoARcPSD|12345",
        }]}]

        updated = _normalize_approved_visual_captions(image, references)

        self.assertEqual(updated, "![Graph](/media/graph.jpg)")

    @patch("services.prep_ai_router._repair_invalid_note_cache", return_value=None)
    @patch("services.prep_ai_router.route_math_request")
    def test_unapproved_visual_marker_returns_no_publishable_notes(self, route_request, _repair):
        invalid_notes = self.valid_notes.replace("## 3. Three", "[[VISUAL:999999]]\n\n## 3. Three")
        route_request.return_value = {
            "success": True,
            "content": invalid_notes,
            "model_used": "test-model",
            "usage": {},
        }

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertTrue(result.get("validation_failed"), result)
        self.assertEqual(result.get("notes"), "")
        self.assertIn("NO APPROVED SOURCE FIGURE IS AVAILABLE", route_request.call_args.args[0])
        self.assertNotIn("Text-only visual walkthrough:", route_request.call_args.args[0])
        self.assertIn("without labeling it as a walkthrough", route_request.call_args.args[0])
        self.assertIn("UNIVERSAL VISUAL AND NOTATION REQUIREMENTS (all disciplines)", route_request.call_args.args[0])
        self.assertIn("Define every variable, symbol, abbreviation, and unit", route_request.call_args.args[0])
        self.assertIn("explain each supported relationship or direction", route_request.call_args.args[0])
        self.assertIn("NON-STUDY ADMINISTRATIVE DETAILS POLICY (all disciplines)", route_request.call_args.args[0])
        self.assertFalse(PrepContentCache.objects.filter(
            topic=self.topic,
            content_type="topic_notes",
            payload__validation_state=NOTE_VALIDATION_STATE,
        ).exists())

    @patch("prep.views.get_or_generate_topic_notes")
    def test_review_blocked_notes_do_not_fall_through_to_generation(self, note_service):
        PrepCourseEnrollment.objects.get_or_create(user=self.user, course=self.course)
        signature = _topic_notes_cache_signature(
            self.course, self.topic, self.topic.title, self.topic.subtopics
        )
        PrepNoteGenerationGuard.objects.create(
            topic=self.topic,
            level="level_2",
            source_signature=signature,
            failed_attempts=1,
            status="needs_review",
            last_error="empty content",
        )
        note_service.return_value = {
            "notes": "",
            "blocks": [],
            "cached": False,
            "level": "level_2",
            "needs_review": True,
            "validation_failed": True,
            "error": "This note level is awaiting tutor review.",
        }
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("prep:api_topic_notes"),
            data=json.dumps({
                "topic_id": self.topic.pk,
                "course_code": self.course.code,
                "topic_title": self.topic.title,
                "level": "level_2",
            }),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 409)
        self.assertTrue(response.json()["needs_review"])
        self.assertEqual(note_service.call_count, 1)
        self.assertFalse(note_service.call_args.kwargs["generate_if_missing"])

    @patch("services.prep_ai_router._repair_invalid_note_cache")
    @patch("services.prep_ai_router.route_math_request")
    def test_stale_review_guard_allows_retry_when_no_repair_was_recorded(self, route_request, repair):
        signature = _topic_notes_cache_signature(
            self.course, self.topic, self.topic.title, self.topic.subtopics
        )
        cache_key = compute_cache_key(
            "notes", NOTES_CACHE_VERSION, self.course.code, self.topic.title, "level_2", signature
        )
        PrepContentCache.objects.create(
            cache_key=cache_key,
            content_type="topic_notes",
            prompt_hash="empty-invalid-note",
            payload={"content": "", "level": "level_2"},
            course=self.course,
            topic=self.topic,
        )
        guard = PrepNoteGenerationGuard.objects.create(
            topic=self.topic,
            level="level_2",
            source_signature=signature,
            failed_attempts=1,
            status="needs_review",
            last_error="empty content",
        )
        route_request.return_value = {
            "success": True,
            "content": self.valid_notes,
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

        self.assertEqual(result["notes"].strip(), self.valid_notes.strip())
        self.assertFalse(result.get("cached"))
        self.assertFalse(PrepNoteGenerationGuard.objects.filter(pk=guard.pk).exists())
        repair.assert_not_called()
        route_request.assert_called_once()

    def test_figure_reference_issue_is_scoped_to_its_note_section(self):
        notes = self.valid_notes.replace(
            "## 3. Three\n\nText.",
            "## 3. Three\n\nAs shown in the graph, the quantity increases.",
        )

        prefix, repair_scope, suffix = _note_repair_scope(notes, self.topic.title)

        self.assertIn("As shown in the graph", repair_scope)
        self.assertNotIn("## 1. One", repair_scope)
        self.assertNotIn("## 4. Four", repair_scope)
        self.assertIn("## 1. One", prefix)
        self.assertIn("## 4. Four", suffix)

    def test_admin_retry_action_reopens_the_matching_note_repair(self):
        signature = _topic_notes_cache_signature(
            self.course, self.topic, self.topic.title, self.topic.subtopics
        )
        guard = PrepNoteGenerationGuard.objects.create(
            topic=self.topic,
            level="level_2",
            source_signature=signature,
            failed_attempts=1,
            status="needs_review",
            last_error="empty content",
        )
        repair = PrepNoteRepair.objects.create(
            topic=self.topic,
            level="level_2",
            source_signature=signature,
            cache_key="notes:retry-action-test",
            original_content="partial notes",
            current_content="partial notes",
            validation_issues=["missing section ## 2."],
            attempts=3,
            status="needs_review",
            last_error="repair exhausted",
        )
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save(update_fields=["is_staff", "is_superuser"])
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("admin:prep_prepnotegenerationguard_changelist"),
            {
                "action": "reset_generation_guards",
                "_selected_action": [str(guard.pk)],
                "index": "0",
            },
        )

        self.assertEqual(response.status_code, 302)
        guard.refresh_from_db()
        repair.refresh_from_db()
        self.assertEqual(guard.status, "open")
        self.assertEqual(guard.failed_attempts, 0)
        self.assertEqual(repair.status, "open")
        self.assertEqual(repair.attempts, 0)
        self.assertEqual(repair.current_content, "partial notes")

    @patch("services.prep_ai_router._repair_invalid_note_cache")
    @patch("services.prep_ai_router.route_math_request")
    def test_empty_cached_note_uses_one_provider_retry_and_validates_replacement(self, route_request, repair):
        signature = _topic_notes_cache_signature(
            self.course, self.topic, self.topic.title, self.topic.subtopics
        )
        cache_key = compute_cache_key(
            "notes", NOTES_CACHE_VERSION, self.course.code, self.topic.title, "level_2", signature
        )
        PrepContentCache.objects.create(
            cache_key=cache_key,
            content_type="topic_notes",
            prompt_hash="empty-note-cache",
            payload={"content": "", "level": "level_2"},
            course=self.course,
            topic=self.topic,
        )
        route_request.side_effect = [
            {
                "success": False,
                "empty_response": True,
                "finish_reason": "stop",
                "response_id": "empty-first-attempt",
                "error": "DeepSeek returned empty assistant content (finish_reason=stop).",
                "usage": {"prompt_tokens": 10, "completion_tokens": 0, "total_tokens": 10},
            },
            {
                "success": True,
                "content": self.valid_notes,
                "model_used": "test-model",
                "usage": {"prompt_tokens": 10, "completion_tokens": 100, "total_tokens": 110},
            },
        ]

        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertEqual(result["notes"], self.valid_notes.strip())
        self.assertTrue(result["regenerated_from_invalid_cache"])
        self.assertEqual(route_request.call_count, 2)
        self.assertEqual(result["usage"]["total_tokens"], 120)
        repair.assert_not_called()
        self.assertTrue(all(call.kwargs["thinking_enabled"] is False for call in route_request.call_args_list))
        cached = PrepContentCache.objects.get(cache_key=cache_key)
        self.assertEqual(cached.payload["content"], self.valid_notes.strip())
        self.assertEqual(cached.payload["validation_state"], NOTE_VALIDATION_STATE)

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
                "source_signature": _topic_notes_cache_signature(
                    self.course,
                    self.topic,
                    self.topic.title,
                    self.topic.subtopics,
                ),
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
                "source_signature": _topic_notes_cache_signature(
                    self.course,
                    self.topic,
                    self.topic.title,
                    self.topic.subtopics,
                ),
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

    @patch("services.prep_ai_router.route_math_request")
    def test_variant_metadata_links_to_verified_source_and_rule_versions(self, route_request):
        source = PrepQuestion.objects.create(
            topic=self.topic,
            question_type="authentic",
            verification_status="verified",
            number=9,
            marks=5,
            topic_label=self.topic.title,
            question_latex="Explain the monotone sequence convergence theorem.",
            solution_latex="Use the theorem hypotheses and conclude convergence.",
        )
        route_request.return_value = {
            "success": True,
            "content": json.dumps([{
                "number": 1,
                "marks": 5,
                "topic_label": "Sequence properties",
                "question_latex": "Compare two monotone sequences and state the convergence condition.",
                "solution_latex": "Check monotonicity and boundedness, then apply the convergence theorem.",
                "hint": "Start with the two defining hypotheses.",
            }]),
            "model_used": "test-model",
            "usage": {},
        }

        result = generate_similar_practice_questions(
            self.course.code,
            self.topic.title,
            question_count=1,
            topic_obj=self.topic,
            course_obj=self.course,
        )

        variant = PrepQuestion.objects.get(topic=self.topic, question_type="generated")
        self.assertTrue(result["success"], result)
        self.assertEqual(variant.verification_status, "verified")
        self.assertEqual(variant.reconstruction_metadata["variant_status"], "validated")
        self.assertEqual(variant.reconstruction_metadata["source_question_ids"], [str(source.pk)])
        self.assertEqual(variant.reconstruction_metadata["source_course_code"], self.course.code)
        self.assertIn("validation_version", variant.reconstruction_metadata)
        self.assertTrue(variant.reconstruction_metadata["source_signature"])

    @patch("services.prep_ai_router.route_math_request")
    def test_exact_duplicate_of_verified_source_is_not_saved(self, route_request):
        source_text = "Explain the monotone sequence convergence theorem."
        PrepQuestion.objects.create(
            topic=self.topic,
            question_type="authentic",
            verification_status="verified",
            number=9,
            marks=5,
            topic_label=self.topic.title,
            question_latex=source_text,
            solution_latex="Use the theorem hypotheses and conclude convergence.",
        )
        route_request.return_value = {
            "success": True,
            "content": json.dumps([{
                "number": 1,
                "marks": 5,
                "topic_label": "Sequence properties",
                "question_latex": source_text,
                "solution_latex": "Use the theorem hypotheses and conclude convergence.",
                "hint": "Use the stated theorem.",
            }]),
            "model_used": "test-model",
            "usage": {},
        }

        result = generate_similar_practice_questions(
            self.course.code,
            self.topic.title,
            question_count=1,
            topic_obj=self.topic,
            course_obj=self.course,
        )

        self.assertFalse(result["success"])
        self.assertIn("failed source, modality, or answer validation", result["error"])
        self.assertFalse(PrepQuestion.objects.filter(topic=self.topic, question_type="generated").exists())

    @patch("services.prep_ai_router.route_math_request")
    def test_practice_prompt_uses_only_verified_question_samples(self, route_request):
        PrepQuestion.objects.create(
            topic=self.topic,
            question_type="authentic",
            number=1,
            marks=5,
            topic_label=self.topic.title,
            question_latex="VERIFIED_SAMPLE_MARKER: source-approved sequence question.",
            verification_status="verified",
        )
        PrepQuestion.objects.create(
            topic=self.topic,
            question_type="authentic",
            number=2,
            marks=5,
            topic_label=self.topic.title,
            question_latex="PENDING_SAMPLE_MARKER: unreviewed extraction.",
            verification_status="pending",
        )
        route_request.return_value = {
            "success": True,
            "content": json.dumps([{
                "number": 1,
                "marks": 5,
                "topic_label": "Sequence properties",
                "question_latex": "Explain one property of a verified sequence.",
                "solution_latex": "Use the definition and justify the conclusion with a complete explanation.",
                "hint": "Start from the definition.",
            }]),
            "model_used": "test-model",
            "usage": {},
        }

        result = generate_similar_practice_questions(
            self.course.code,
            self.topic.title,
            question_count=1,
            authentic_samples=["CALLER_SUPPLIED_UNVERIFIED_MARKER"],
            topic_obj=self.topic,
            course_obj=self.course,
        )

        prompt = route_request.call_args.args[0]
        self.assertTrue(result["success"], result)
        self.assertIn("VERIFIED_SAMPLE_MARKER", prompt)
        self.assertNotIn("PENDING_SAMPLE_MARKER", prompt)
        self.assertNotIn("CALLER_SUPPLIED_UNVERIFIED_MARKER", prompt)

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
            question_latex="Find the value of $x$ and explain how it follows from the equation.",
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

    @patch("services.prep_ai_router.get_or_generate_topic_notes")
    def test_topic_page_displays_auto_validated_and_reconstructed_but_hides_pending(self, generate_notes):
        generate_notes.return_value = {"notes": "## 1. Valid Notes", "cached": True}
        original = PrepQuestion.objects.create(
            topic=self.topic,
            question_type="authentic",
            verification_status="flagged",
            number=1,
            marks=5,
            question_latex="FLAGGED_ORIGINAL_MARKER",
        )
        PrepQuestion.objects.create(
            topic=self.topic,
            question_type="authentic",
            verification_status="auto_validated",
            number=2,
            marks=5,
            question_latex="AUTO_VALIDATED_SOURCE_MARKER",
        )
        PrepQuestion.objects.create(
            topic=self.topic,
            question_type="adapted",
            verification_status="reconstructed",
            reconstructed_from=original,
            number=1,
            marks=5,
            topic_label="Reconstructed from Question 1",
            question_latex="AUTO_RECONSTRUCTED_MARKER",
            reconstruction_metadata={"review_status": "auto_validated", "model_confidence": 0.93},
        )
        PrepQuestion.objects.create(
            topic=self.topic,
            question_type="adapted",
            verification_status="pending",
            number=3,
            marks=5,
            question_latex="PENDING_ADAPTATION_MARKER",
        )

        response = self.client.get(reverse("prep:topic_study", kwargs={"topic_id": self.topic.id}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "AUTO_VALIDATED_SOURCE_MARKER")
        self.assertContains(response, "AUTO_RECONSTRUCTED_MARKER")
        self.assertContains(response, "ADAPTED PAST QUESTION")
        self.assertNotContains(response, "FLAGGED_ORIGINAL_MARKER")
        self.assertNotContains(response, "PENDING_ADAPTATION_MARKER")

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
