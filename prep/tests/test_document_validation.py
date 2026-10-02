from types import SimpleNamespace
import tempfile
from unittest.mock import patch

from django.contrib.admin.sites import AdminSite
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, SimpleTestCase, TestCase, override_settings

from prep.document_validation import build_document_validation_report
from prep.content_rules import CONTENT_MODALITIES
from prep.admin import PrepDocumentAdmin
from prep.models import PrepCourse, PrepDocument, PrepDocumentVisual, PrepPaper
from accounts.models import User


def allowed_rules():
    return {
        "schema_version": 1,
        "modalities": {
            modality: {"policy": "allowed", "evidence_required": True}
            for modality in CONTENT_MODALITIES
        },
    }


def source_document():
    return SimpleNamespace(pk="doc-123", file_sha256="a" * 64)


def visual_candidate(
    *,
    visual_type="graph",
    page_number=2,
    status="inspected",
    axes=None,
    units=None,
):
    axis_data = axes if axes is not None else {"x_label": "Time", "y_label": "Distance"}
    if units is not None:
        axis_data["units"] = units
    return SimpleNamespace(
        pk=19,
        page_number=page_number,
        bbox=[10, 20, 300, 400],
        crop=SimpleNamespace(name="prep/visual-crops/page-2.jpg"),
        visual_type=visual_type,
        status=status,
        extracted_content={"axes": axis_data},
    )


class DocumentValidationReportTests(SimpleTestCase):
    def test_missing_approved_rules_are_reviewed_not_guessed(self):
        document = source_document()
        document.course = SimpleNamespace(category="Social Sciences")

        report = build_document_validation_report(document, "A text-only page.")

        self.assertEqual(report["status"], "needs_review")
        self.assertEqual(report["rules_status"], "missing")
        self.assertIn("approved_content_rules_missing", {issue["code"] for issue in report["issues"]})

    def test_unclosed_equation_is_reported_with_page_provenance(self):
        report = build_document_validation_report(
            source_document(),
            "--- Page 4 ---\n$$\\frac{1}{2}\n",
            course_rules=allowed_rules(),
        )

        issue = next(issue for issue in report["issues"] if issue["modality"] == "equations")
        self.assertEqual(issue["provenance"]["document_id"], "doc-123")
        self.assertEqual(issue["provenance"]["page_number"], 4)

    def test_unmatched_inline_math_is_reported(self):
        report = build_document_validation_report(
            source_document(),
            "--- Page 11 ---\nAn incomplete expression $x + 1 remains open.",
            course_rules=allowed_rules(),
        )

        self.assertTrue(any("unmatched inline-math delimiter" in issue["message"] for issue in report["issues"]))

    def test_empty_extraction_cannot_pass_validation(self):
        report = build_document_validation_report(
            source_document(), "", course_rules=allowed_rules()
        )

        self.assertEqual(report["status"], "needs_review")
        self.assertIn("empty_extraction", {issue["code"] for issue in report["issues"]})

    def test_unknown_ocr_replacement_character_is_reported_not_repaired(self):
        source = "--- Page 9 ---\nAn uncertain symbol \ufffd remains unresolved."

        report = build_document_validation_report(
            source_document(), source, course_rules=allowed_rules()
        )

        issue = next(issue for issue in report["issues"] if issue["code"] == "unreadable_replacement_character")
        self.assertEqual(issue["provenance"]["page_number"], 9)
        self.assertEqual(source.splitlines()[1], "An uncertain symbol \ufffd remains unresolved.")

    def test_unclosed_code_fence_is_reported_with_code_modality(self):
        report = build_document_validation_report(
            source_document(),
            "--- Page 10 ---\n```python\nprint('unfinished')",
            course_rules=allowed_rules(),
        )

        issue = next(issue for issue in report["issues"] if "fenced code block" in issue["message"])
        self.assertEqual(issue["modality"], "code")
        self.assertEqual(issue["provenance"]["page_number"], 10)

    def test_tikz_diagram_is_not_detected_as_equation_content(self):
        report = build_document_validation_report(
            source_document(),
            "--- Page 8 ---\n\\begin{center}\\begin{tikzpicture}\\draw (0,0) -- (1,1);\\end{tikzpicture}\\end{center}",
            course_rules=allowed_rules(),
        )

        self.assertNotIn("equations", report["detected_modalities"])
        self.assertIn("arrow_diagrams", report["detected_modalities"])
        self.assertIn("diagram_markup_unlinked", {issue["code"] for issue in report["issues"]})

    def test_known_chemical_equation_is_detected_without_balancing_or_rewriting(self):
        source = "--- Page 3 ---\n2H2 + O2 -> 2H2O"

        report = build_document_validation_report(
            source_document(), source, course_rules=allowed_rules()
        )

        self.assertIn("chemical_equations", report["detected_modalities"])
        self.assertEqual(report["issues"], [])

    def test_incomplete_chemical_reaction_is_routed_to_review(self):
        report = build_document_validation_report(
            source_document(),
            "--- Page 5 ---\nH2 + O2 ->",
            course_rules=allowed_rules(),
        )

        issue = next(issue for issue in report["issues"] if issue["code"] == "malformed_chemical_equation")
        self.assertEqual(issue["provenance"]["page_number"], 5)

    def test_unknown_code_language_is_reported(self):
        report = build_document_validation_report(
            source_document(),
            "--- Page 2 ---\n```mysterylang\nprint(1)\n```",
            course_rules=allowed_rules(),
        )

        self.assertIn("code", report["detected_modalities"])
        self.assertIn("code_language_unknown", {issue["code"] for issue in report["issues"]})

    def test_structurally_invalid_table_is_reported(self):
        report = build_document_validation_report(
            source_document(),
            "--- Page 6 ---\n| A | B |\n| --- | --- |\n| 1 | 2 | 3 |",
            course_rules=allowed_rules(),
        )

        self.assertIn("tables", report["detected_modalities"])
        issue = next(issue for issue in report["issues"] if issue["code"] == "malformed_markdown_table")
        self.assertEqual(issue["provenance"]["page_number"], 6)

    def test_visual_reference_without_a_crop_is_reported(self):
        report = build_document_validation_report(
            source_document(),
            "--- Page 7 ---\nSee Figure 2 for the process.",
            course_rules=allowed_rules(),
        )

        issue = next(issue for issue in report["issues"] if issue["code"] == "visual_reference_unlinked")
        self.assertEqual(issue["provenance"]["page_number"], 7)

    def test_graph_axes_and_malformed_units_keep_crop_provenance(self):
        candidate = visual_candidate(units=[1, 2])

        report = build_document_validation_report(
            source_document(),
            "--- Page 2 ---\nFigure 1: motion graph.",
            visual_candidates=[candidate],
            course_rules=allowed_rules(),
        )

        issue = next(issue for issue in report["issues"] if issue["code"] == "graph_units_malformed")
        self.assertEqual(issue["provenance"]["visual_candidate_id"], "19")
        self.assertEqual(issue["provenance"]["bbox"], [10, 20, 300, 400])
        self.assertEqual(issue["provenance"]["crop"], "prep/visual-crops/page-2.jpg")

    def test_source_transcribed_graph_units_are_accepted_unchanged(self):
        units = {"x": "s", "y": "m"}
        candidate = visual_candidate(units=units)
        candidate.extracted_content["axes"]["units"] = units

        report = build_document_validation_report(
            source_document(),
            "--- Page 2 ---\nFigure 1: distance over time.",
            visual_candidates=[candidate],
            course_rules=allowed_rules(),
        )

        self.assertNotIn("graph_units_malformed", {issue["code"] for issue in report["issues"]})
        self.assertEqual(candidate.extracted_content["axes"]["units"], units)

    def test_graph_without_axis_labels_is_not_reconstructed_as_fully_valid(self):
        candidate = visual_candidate(axes={})

        report = build_document_validation_report(
            source_document(),
            "--- Page 2 ---\nA graph is shown.",
            visual_candidates=[candidate],
            course_rules=allowed_rules(),
        )

        self.assertIn("graph_axis_labels_missing", {issue["code"] for issue in report["issues"]})
        self.assertEqual(report["status"], "needs_review")

    def test_low_confidence_visual_is_routed_to_review(self):
        candidate = visual_candidate(status="needs_review")
        candidate.confidence = 0.42
        candidate.extracted_content["confidence"] = 0.42

        report = build_document_validation_report(
            source_document(),
            "--- Page 2 ---\nGraph under review.",
            visual_candidates=[candidate],
            course_rules=allowed_rules(),
        )

        self.assertEqual(report["status"], "needs_review")
        self.assertIn("visual_classification_unresolved", {issue["code"] for issue in report["issues"]})

    def test_approved_disallowed_modality_is_an_error_with_source_location(self):
        rules = allowed_rules()
        rules["modalities"]["graphs"] = {
            "policy": "disallowed",
            "rationale": "This approved topic has no graph instruction.",
        }
        candidate = visual_candidate()

        report = build_document_validation_report(
            source_document(),
            "--- Page 2 ---\nGraph of distance over time.",
            visual_candidates=[candidate],
            course_rules=rules,
        )

        issue = next(issue for issue in report["issues"] if issue["code"] == "modality_disallowed")
        self.assertEqual(issue["severity"], "error")
        self.assertEqual(issue["modality"], "graphs")
        self.assertEqual(issue["provenance"]["page_number"], 2)
        self.assertEqual(report["rules_status"], "valid")


class DocumentValidationPublicationGateTests(TestCase):
    @patch.object(PrepDocumentAdmin, "message_user")
    def test_disallowed_modality_cannot_be_published_or_create_a_paper(self, _message):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            user = User.objects.create_user(username="validation-reviewer", password="Pass12345")
            course = PrepCourse.objects.create(
                code="VAL 200",
                title="Validation Gate Testing",
                slug="validation-gate-testing",
                study_profile_version=1,
                study_profile={
                    "content_rules": {
                        "schema_version": 1,
                        "modalities": {
                            "graphs": {
                                "policy": "disallowed",
                                "rationale": "Approved source notes exclude graphs.",
                            },
                        },
                    },
                },
            )
            document = PrepDocument.objects.create(
                course=course,
                doc_type="Final Examination Paper",
                file=SimpleUploadedFile("restricted.pdf", b"pdf"),
                extracted_text="--- Page 1 ---\nFigure 1: Demand graph.",
                stage="stage_2",
            )
            PrepDocumentVisual.objects.create(
                document=document,
                candidate_key="c" * 64,
                page_number=1,
                bbox=[10, 20, 300, 400],
                crop="prep/visual-crops/page-1.jpg",
                visual_type="graph",
                status="candidate",
            )
            request = RequestFactory().post("/admin/prep/prepdocument/")
            request.user = user
            model_admin = PrepDocumentAdmin(PrepDocument, AdminSite())

            model_admin.approve_stage_3_publish(request, PrepDocument.objects.filter(pk=document.pk))

            document.refresh_from_db()
            self.assertEqual(document.stage, "stage_2")
            self.assertIsNone(document.reviewed_at)
            self.assertIn("Publication blocked by validation", document.tutor_review_notes)
            self.assertTrue(any(
                issue["code"] == "modality_disallowed"
                for issue in document.validation_report["issues"]
            ))
            self.assertFalse(PrepPaper.objects.filter(source_document=document).exists())