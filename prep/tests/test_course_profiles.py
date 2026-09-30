import io
import json
import tempfile
from unittest.mock import patch

from django.contrib import admin
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.utils import timezone

from accounts.models import User
from prep.admin import PrepDocumentAdmin
from prep.models import PrepContentUpdate, PrepCourse, PrepDocument, PrepTopic
from services.prep_ai_router import get_or_generate_topic_notes, _note_allows_code, _note_completion_issues
from services.prep_ingestion import create_content_update_proposals, extract_course_study_profile


class CourseStudyProfileExtractionTests(TestCase):
    def setUp(self):
        self.course = PrepCourse.objects.create(
            code="ASC 100",
            title="Introduction to Sociology",
            slug="profile-asc-100",
            category="Computing",
        )

    def test_latex_fence_is_not_mistaken_for_a_code_block(self):
        from services.prep_ingestion import _source_capabilities

        capabilities = _source_capabilities("```\n\\documentclass{article}\n\\begin{document}\n$$x^2$$\n```")

        self.assertFalse(capabilities["code"])
        self.assertTrue(capabilities["math_notation"])

    @patch("services.prep_ingestion.requests.post")
    def test_classifier_uses_verbatim_note_evidence_and_disables_absent_capabilities(self, post):
        source = (
            "Sociology studies social institutions, social stratification, and social change. "
            "Students compare theoretical perspectives using examples from East African communities."
        )
        quote = "Sociology studies social institutions, social stratification, and social change."
        post.return_value.status_code = 200
        post.return_value.json.return_value = {
            "choices": [{"message": {"content": json.dumps({
                "subject_family": "social_science",
                "confidence": 0.98,
                "evidence_quotes": [quote],
                "capabilities": {
                    "code": False,
                    "math_notation": False,
                    "chemical_equations": False,
                },
            })}}],
        }

        profile = extract_course_study_profile(self.course, source)

        self.assertEqual(profile["subject_family"], "social_science")
        self.assertEqual(profile["category"], "Social Sciences")
        self.assertEqual(profile["evidence_quotes"], [quote])
        self.assertEqual(profile["capabilities"], {
            "code": False,
            "math_notation": False,
            "chemical_equations": False,
        })
        self.assertEqual(len(profile["note_structure"]), 5)

    @patch("services.prep_ingestion.requests.post")
    def test_source_detected_math_and_code_override_classifier_false_negatives(self, post):
        source = (
            "R programming lecture notes explain estimation with this implementation.\n"
            "```R\nfit <- lm(y ~ x)\n```\n"
            "The coefficient is estimated as $\\hat{\\beta}_1 = S_{xy}/S_{xx}$ using the sample."
        )
        post.return_value.status_code = 200
        post.return_value.json.return_value = {
            "choices": [{"message": {"content": json.dumps({
                "subject_family": "statistics",
                "confidence": 0.98,
                "evidence_quotes": ["R programming lecture notes explain estimation"],
                "capabilities": {"code": False, "math_notation": False, "chemical_equations": False},
            })}}],
        }

        profile = extract_course_study_profile(self.course, source)

        self.assertEqual(profile["capabilities"], {
            "code": True,
            "math_notation": True,
            "chemical_equations": False,
        })

    @patch("services.prep_ingestion.requests.post")
    def test_rejects_classifier_evidence_not_found_in_uploaded_notes(self, post):
        post.return_value.status_code = 200
        post.return_value.json.return_value = {
            "choices": [{"message": {"content": json.dumps({
                "subject_family": "computing",
                "confidence": 1,
                "evidence_quotes": ["Python programming and statistical computation"],
                "capabilities": {"code": True, "math_notation": True},
            })}}],
        }

        self.assertIsNone(extract_course_study_profile(self.course, "Sociology covers families and institutions." * 10))

    @override_settings(MEDIA_ROOT="")
    def test_exam_document_cannot_create_a_course_profile_proposal(self):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            exam = PrepDocument.objects.create(
                course=self.course,
                doc_type="Final Examination Paper",
                academic_year="2025/2026",
                topic_name="Full Syllabus",
                file=SimpleUploadedFile("exam.pdf", b"%PDF exam"),
                extracted_text="Sociology question paper source text long enough to process." * 4,
                stage="stage_3",
            )
            proposal = {
                "subject_family": "social_science",
                "category": "Social Sciences",
                "source_document_id": str(exam.pk),
                "source_sha256": "a" * 64,
                "confidence": 0.99,
                "evidence_quotes": ["Sociology question paper source text"],
                "capabilities": {"code": False, "math_notation": False, "chemical_equations": False},
                "note_structure": ["One", "Two", "Three", "Four", "Five"],
            }

            updates = create_content_update_proposals(
                self.course,
                exam,
                [],
                course_profile=proposal,
            )

        self.assertEqual(updates, [])
        self.assertFalse(PrepContentUpdate.objects.filter(document=exam, update_type="course_profile").exists())


class ApprovedCourseStudyProfileTests(TestCase):
    def setUp(self):
        self.media_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.media_directory.cleanup)
        self.media_settings = override_settings(MEDIA_ROOT=self.media_directory.name)
        self.media_settings.enable()
        self.addCleanup(self.media_settings.disable)
        self.user = User.objects.create_user(
            username="profile_reviewer",
            email="profile-reviewer@example.test",
            password="Valid123",
        )
        self.course = PrepCourse.objects.create(
            code="ASC 100",
            title="Introduction to Sociology",
            slug="approved-profile-asc-100",
            category="Computing",
        )
        self.topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Social Structure",
            slug="social-structure-profile-test",
            summary="The organization of social relationships and institutions.",
            subtopics=["Social roles", "Institutions"],
        )
        self.document = PrepDocument.objects.create(
            course=self.course,
            user=self.user,
            doc_type="Lecture Notes",
            academic_year="2025/2026",
            topic_name="Full Syllabus",
            file=SimpleUploadedFile("sociology-notes.pdf", b"%PDF sociology"),
            extracted_text="Sociology notes explain social structure and institutions." * 8,
            stage="stage_3",
        )
        self.profile = {
            "schema_version": 1,
            "subject_family": "social_science",
            "category": "Social Sciences",
            "confidence": 0.98,
            "source_document_id": str(self.document.pk),
            "source_sha256": "b" * 64,
            "evidence_quotes": ["Sociology notes explain social structure and institutions."],
            "capabilities": {"code": False, "math_notation": False, "chemical_equations": False},
            "note_structure": [
                "Core Concepts and Context",
                "Theories and Key Thinkers",
                "Social Processes and Evidence",
                "Applications and Case Studies",
                "Revision Summary and Critical Questions",
            ],
        }

    def test_approved_profile_updates_category_and_version(self):
        update = PrepContentUpdate.objects.create(
            document=self.document,
            topic=None,
            update_type="course_profile",
            proposed_data=self.profile,
            rationale="Grounded profile proposal.",
        )
        model_admin = PrepDocumentAdmin(PrepDocument, admin.site)

        applied = model_admin._apply_safe_content_updates(self.document, self.user, timezone.now())

        self.course.refresh_from_db()
        update.refresh_from_db()
        self.assertEqual(applied, 1)
        self.assertEqual(self.course.category, "Social Sciences")
        self.assertEqual(self.course.study_profile_version, 1)
        self.assertEqual(self.course.study_profile["subject_family"], "social_science")
        self.assertEqual(update.status, "approved")

    @patch("services.prep_ai_router.route_math_request")
    def test_profile_controls_note_structure_and_forbids_unsupported_code_and_math(self, route_request):
        self.course.study_profile = self.profile
        self.course.study_profile_version = 1
        self.course.save(update_fields=["study_profile", "study_profile_version"])
        content = "\n\n".join(
            f"## {index}. {heading}\n\nThis section explains the approved sociology material in clear prose, with grounded examples and a concise discussion of relevant social institutions and relationships."
            for index, heading in enumerate(self.profile["note_structure"], start=1)
        )
        route_request.return_value = {
            "success": True,
            "content": content,
            "model_used": "test-model",
            "usage": {},
        }

        self.assertFalse(_note_allows_code(self.course, self.topic.title, self.topic.summary, self.topic.subtopics))
        self.assertTrue(_note_completion_issues(
            content + "\n\n$$x^2$$",
            self.topic.title,
            allow_code=False,
            allow_math=False,
            study_profile=self.profile,
        ))
        result = get_or_generate_topic_notes(
            self.course.code,
            self.topic.title,
            level="level_2",
            course_obj=self.course,
            topic_obj=self.topic,
        )

        self.assertTrue(result.get("notes"), result)
        self.assertTrue(_note_completion_issues(
            result["notes"],
            self.topic.title,
            allow_code=False,
            allow_math=False,
            study_profile=self.profile,
        ) == [])
        prompt = route_request.call_args.args[0]
        self.assertIn("## 2. Theories and Key Thinkers", prompt)
        self.assertIn("Do not include equations", prompt)
        self.assertIn("Do not include code", route_request.call_args.kwargs["system_prompt"])

    def test_computing_profile_allows_r_code_for_matrices_in_r_topic(self):
        self.course.study_profile = {
            "subject_family": "computing",
            "capabilities": {"code": True, "math_notation": True, "chemical_equations": False},
        }

        self.assertTrue(_note_allows_code(self.course, "Matrices in R"))

    @patch("services.prep_ai_router.route_math_request")
    def test_all_note_levels_respect_math_and_code_capabilities(self, route_request):
        self.course.study_profile = {
            **self.profile,
            "subject_family": "computing",
            "capabilities": {"code": True, "math_notation": True, "chemical_equations": False},
        }
        self.course.study_profile_version = 1
        self.course.save(update_fields=["study_profile", "study_profile_version"])
        self.topic.title = "Matrices in R"
        self.topic.subtopics = ["R syntax", "Matrix operations"]
        self.topic.save(update_fields=["title", "subtopics"])
        self.document.extracted_text = (
            "R programming notes. Matrix products satisfy $AB=C$.\n"
            "```R\nA <- matrix(1:4, nrow=2)\n```"
        )
        self.document.save(update_fields=["extracted_text"])
        content = "\n\n".join(
            f"## {index}. {heading}\n\nThis section explains the approved matrix material, gives a relevant worked application, and identifies how the method is used in this course."
            for index, heading in enumerate(self.course.study_profile["note_structure"], start=1)
        )
        route_request.return_value = {"success": True, "content": content, "model_used": "test-model", "usage": {}}

        prompts = []
        for level in ("level_1", "level_2", "level_3"):
            result = get_or_generate_topic_notes(
                self.course.code,
                self.topic.title,
                level=level,
                course_obj=self.course,
                topic_obj=self.topic,
            )
            self.assertTrue(result.get("notes"), result)
            prompts.append(route_request.call_args.args[0])

        self.assertEqual(route_request.call_count, 3)
        for prompt in prompts:
            self.assertIn("Include relevant source-supported equations", prompt)
            self.assertIn("Include source-supported code examples", prompt)