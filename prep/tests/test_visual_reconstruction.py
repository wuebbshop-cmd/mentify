from types import SimpleNamespace
import tempfile
from io import StringIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import SimpleTestCase, TestCase, override_settings

from prep.models import PrepCourse, PrepDocument, PrepDocumentVisual
from prep.visual_reconstruction import (
    build_visual_reconstruction_spec,
    store_visual_reconstruction_proposal,
)


def visual_candidate(*, visual_type="graph", content=None, **overrides):
    document = SimpleNamespace(pk=42, file_sha256="source-sha256")
    candidate = SimpleNamespace(
        pk=7,
        document=document,
        page_number=12,
        bbox=[10, 20, 300, 400],
        crop=SimpleNamespace(name="prep/visual-crops/page-12.jpg"),
        visual_type=visual_type,
        labels=[],
        extracted_content=content or {},
        confidence=0.95,
        status="approved",
    )
    for name, value in overrides.items():
        setattr(candidate, name, value)
    return candidate


class VisualReconstructionPolicyTests(SimpleTestCase):
    def test_unapproved_visual_is_never_reconstructed(self):
        candidate = visual_candidate(status="inspected")

        result = build_visual_reconstruction_spec(candidate)

        self.assertEqual(result["status"], "blocked")
        self.assertIsNone(result["spec"])
        self.assertEqual(result["source"]["source_page_number"], 12)

    def test_quantitative_graph_preserves_only_source_values_and_provenance(self):
        candidate = visual_candidate(content={
            "visual_type": "graph",
            "visible_labels": ["Price", "Quantity"],
            "axes": {"x_label": "Quantity", "y_label": "Price", "units": None},
            "data_points": [{"x": 3, "y": 7}],
            "relationships": ["Source curve passes through the printed point (3, 7)."],
            "uncertainties": [],
            "confidence": 0.95,
        })

        result = build_visual_reconstruction_spec(candidate)

        self.assertEqual(result["status"], "ready")
        self.assertEqual(result["spec"]["representation"], "labelled_graph")
        self.assertEqual(result["spec"]["numeric_values"], [{"x": 3, "y": 7}])
        self.assertEqual(result["spec"]["axes"]["x_label"], "Quantity")
        self.assertFalse(result["spec"]["source_exact"])
        self.assertTrue(result["spec"]["requires_source_crop_link"])
        self.assertEqual(result["source"]["source_file_sha256"], "source-sha256")

    def test_qualitative_graph_is_allowed_without_numeric_values(self):
        candidate = visual_candidate(content={
            "visual_type": "graph",
            "visible_labels": ["D", "Price", "Output"],
            "axes": {"x": "Output", "y": "Price"},
            "visible_numeric_values": [],
            "qualitative_relationships": ["D slopes downward as output increases."],
            "uncertainties": [],
            "confidence": 0.9,
        })

        result = build_visual_reconstruction_spec(candidate)

        self.assertEqual(result["status"], "ready")
        self.assertEqual(result["spec"]["representation"], "qualitative_graph")
        self.assertEqual(result["spec"]["numeric_values"], [])
        self.assertTrue(result["spec"]["schematic"])
        self.assertFalse(result["spec"]["source_exact"])

    def test_kinked_demand_graph_uses_source_relationships_without_numeric_values(self):
        source_context = (
            "The demand curve has a kink. Marginal revenue is discontinuous at the output "
            "corresponding to the kink; segment DR is the upper demand portion, and the "
            "segment from S is the lower portion."
        )
        candidate = visual_candidate(
            context_text=source_context,
            content={
                "visual_type": "graph",
                "visible_labels": ["D", "E", "R", "S", "MR", "Output", "P*", "Q*"],
                "axes": {"x": "Output", "y": "Price"},
                "visible_numeric_values": [],
                "qualitative_relationships": [
                    "Demand curve D has a kink at E.",
                    "Marginal revenue MR is discontinuous at the output corresponding to the kink.",
                    "Segment DR is the upper demand portion; the segment from S is the lower portion.",
                ],
                "uncertainties": [],
                "confidence": 0.95,
            },
        )

        result = build_visual_reconstruction_spec(candidate)

        self.assertEqual(result["status"], "ready")
        self.assertEqual(result["spec"]["representation"], "qualitative_graph")
        self.assertEqual(result["spec"]["numeric_values"], [])
        self.assertIn("Marginal revenue is discontinuous", result["spec"]["supporting_source_text"])
        self.assertFalse(result["spec"]["source_exact"])

    def test_ambiguous_graph_is_held_for_review(self):
        candidate = visual_candidate(content={
            "visual_type": "graph",
            "visible_labels": ["D"],
            "qualitative_relationships": ["D slopes downward."],
            "uncertainties": ["The curve direction is unclear."],
            "confidence": 0.95,
        })

        result = build_visual_reconstruction_spec(candidate)

        self.assertEqual(result["status"], "needs_review")
        self.assertIsNone(result["spec"])
        self.assertTrue(result["source"]["source_crop"].endswith("page-12.jpg"))

    def test_lower_stored_confidence_cannot_be_overridden_by_extracted_confidence(self):
        candidate = visual_candidate(
            confidence=0.4,
            content={
                "visual_type": "graph",
                "qualitative_relationships": ["D slopes downward."],
                "uncertainties": [],
                "confidence": 0.95,
            },
        )

        result = build_visual_reconstruction_spec(candidate)

        self.assertEqual(result["status"], "needs_review")
        self.assertIsNone(result["spec"])

    def test_malformed_relationships_are_not_ignored(self):
        candidate = visual_candidate(content={
            "visual_type": "graph",
            "qualitative_relationships": {"claim": "D slopes downward."},
            "qualitative_summary": "A downward-sloping curve.",
            "uncertainties": [],
            "confidence": 0.95,
        })

        result = build_visual_reconstruction_spec(candidate)

        self.assertEqual(result["status"], "needs_review")
        self.assertIsNone(result["spec"])

    def test_diagram_arrows_require_explicit_relationship_triples(self):
        candidate = visual_candidate(
            visual_type="diagram",
            content={
                "visual_type": "diagram",
                "visible_labels": ["Start", "Stop"],
                "relationships": [["Start", "leads to", "Stop"]],
                "uncertainties": [],
                "confidence": 0.95,
            },
        )

        result = build_visual_reconstruction_spec(candidate)

        self.assertEqual(result["status"], "ready")
        self.assertEqual(result["spec"]["representation"], "arrow_diagram")
        self.assertEqual(result["spec"]["arrows"], [["Start", "leads to", "Stop"]])

    def test_prose_relationships_are_not_guessed_into_diagram_arrows(self):
        candidate = visual_candidate(
            visual_type="diagram",
            content={
                "visual_type": "diagram",
                "visible_labels": ["Start", "Stop"],
                "relationships": ["Start eventually leads to Stop."],
                "uncertainties": [],
                "confidence": 0.95,
            },
        )

        result = build_visual_reconstruction_spec(candidate)

        self.assertEqual(result["status"], "needs_review")
        self.assertIsNone(result["spec"])

    def test_table_reconstruction_requires_structured_rows(self):
        candidate = visual_candidate(
            visual_type="table",
            content={
                "visual_type": "table",
                "visible_labels": ["Substance", "Enthalpy"],
                "visible_numeric_values": [10, -5],
                "uncertainties": [],
                "confidence": 0.95,
            },
        )

        result = build_visual_reconstruction_spec(candidate)

        self.assertEqual(result["status"], "needs_review")
        self.assertIsNone(result["spec"])


class VisualReconstructionPersistenceTests(TestCase):
    def create_approved_visual(self, code):
        course = PrepCourse.objects.create(
            code=code,
            title="Reconstruction Persistence Testing",
            slug=f"reconstruction-persistence-{code.lower().replace(' ', '-')}",
        )
        document = PrepDocument.objects.create(
            course=course,
            file=SimpleUploadedFile("source.pdf", b"source-pdf"),
        )
        visual = PrepDocumentVisual.objects.create(
            document=document,
            candidate_key=(code.replace(" ", "").lower() + "0" * 64)[:64],
            page_number=1,
            bbox=[0, 0, 100, 100],
            crop="prep/visual-crops/page-1.jpg",
            visual_type="graph",
            status="approved",
            confidence=0.95,
            extracted_content={
                "visual_type": "graph",
                "visible_labels": ["Price", "Quantity"],
                "qualitative_relationships": ["The source curve slopes downward."],
                "uncertainties": [],
                "confidence": 0.95,
            },
        )
        return document, visual

    def test_execution_persists_proposal_without_changing_approval_status(self):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            document, visual = self.create_approved_visual("VIS 200")
            output = StringIO()

            call_command(
                "prepare_visual_reconstructions",
                "--document-id", str(document.pk),
                "--execute",
                stdout=output,
            )

            visual.refresh_from_db()
            self.assertEqual(visual.status, "approved")
            self.assertEqual(visual.reconstruction_proposal["status"], "ready")
            self.assertEqual(visual.reconstruction_proposal["source"]["source_page_number"], 1)
            self.assertFalse(visual.reconstruction_proposal["spec"]["source_exact"])
            self.assertIn("decision=ready", output.getvalue())

    def test_management_command_is_dry_run_by_default(self):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            document, visual = self.create_approved_visual("VIS 201")
            unapproved = PrepDocumentVisual.objects.create(
                document=document,
                candidate_key="b" * 64,
                page_number=2,
                bbox=[0, 0, 100, 100],
                crop="prep/visual-crops/page-2.jpg",
                visual_type="graph",
                status="inspected",
                confidence=0.95,
                extracted_content={},
            )
            output = StringIO()

            call_command(
                "prepare_visual_reconstructions",
                "--document-id", str(document.pk),
                stdout=output,
            )

            visual.refresh_from_db()
            unapproved.refresh_from_db()
            self.assertEqual(visual.reconstruction_proposal, {})
            self.assertEqual(unapproved.reconstruction_proposal, {})
            self.assertIn("Dry run only", output.getvalue())