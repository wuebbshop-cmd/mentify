import tempfile
from io import BytesIO, StringIO
import json
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import json

import fitz
from PIL import Image
from django.contrib import admin
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import SimpleTestCase, TestCase, override_settings
from django.urls import reverse

from accounts.models import User
from prep.admin import PrepDocumentVisualAdmin
from prep.models import PrepCourse, PrepDocument, PrepDocumentVisual, PrepTopic
from services.prep_ingestion import (
    inspect_pdf_visual_candidates,
    inspect_visual_candidate_with_vision,
    _visual_source_conflicts,
    extract_scanned_ocr_together,
    extract_text_pdfplumber,
    extract_topic_candidates,
    merge_local_and_ocr_pages,
    process_prep_document,
    store_pdf_visual_candidates,
    assign_visuals_to_topics,
)
from prep.visual_matching import map_pdf_topic_sections, score_topic_context


def build_pdf(*, text="", draw_graph=False, draw_flowchart=False):
    document = fitz.open()
    page = document.new_page(width=600, height=800)
    if text:
        page.insert_text((50, 70), text)
    if draw_graph:
        page.insert_text((60, 120), "Figure 1: Demand graph")
        page.draw_line((100, 500), (100, 250), width=1.5)
        page.draw_line((100, 500), (450, 500), width=1.5)
        page.draw_line((125, 290), (420, 450), width=2)
    if draw_flowchart:
        page.insert_text((60, 120), "Flowchart for the algorithm")
        page.draw_rect(fitz.Rect(180, 220, 330, 270), width=1.5)
        page.draw_rect(fitz.Rect(180, 360, 330, 410), width=1.5)
        page.draw_line((255, 270), (255, 360), width=1.5)
    result = document.tobytes()
    document.close()
    return result


class VisualGoldSetRegressionTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        gold_path = Path(__file__).resolve().parents[4] / "Products" / "EduAI_MentifyAI" / "visual_gold_set.json"
        cls.gold_set = json.loads(gold_path.read_text(encoding="utf-8"))

    def test_reviewed_gold_set_has_five_unique_unapproved_samples(self):
        samples = self.gold_set["samples"]

        self.assertEqual(len(samples), 5)
        self.assertEqual(len({sample["id"] for sample in samples}), 5)
        self.assertEqual(self.gold_set["human_gold_approval"], "pending")
        self.assertEqual(self.gold_set["course_rules_approval"], "not_granted")

    def test_known_ode_label_error_is_flagged_using_gold_set_context(self):
        sample = next(sample for sample in self.gold_set["samples"] if sample["id"] == "ode_sma335_page149")

        conflicts = _visual_source_conflicts(
            sample["known_incorrect_model_response"],
            sample["source_context_for_conflict_test"],
            sample["reference"]["visual_type"],
        )

        self.assertTrue(any("N1" in issue and "A1" in issue for issue in conflicts), conflicts)
        self.assertTrue(any("N2" in issue and "A2" in issue for issue in conflicts), conflicts)

    def test_known_economics_omissions_are_flagged_using_gold_set_context(self):
        sample = next(sample for sample in self.gold_set["samples"] if sample["id"] == "economics_eet100_page107_kinked_demand")

        conflicts = _visual_source_conflicts(
            sample["known_incomplete_model_response"],
            sample["source_context_for_conflict_test"],
            sample["reference"]["visual_type"],
        )

        self.assertTrue(any("kink" in issue.lower() for issue in conflicts), conflicts)
        self.assertTrue(any("discontinuous marginal revenue" in issue.lower() for issue in conflicts), conflicts)


class PdfVisualCandidateTests(TestCase):
    def test_topic_extraction_prefers_syllabus_headings_over_cover_metadata_rows(self):
        text = """
| 1. Cover metadata | EET 100 |
| 2. Another cover row | Economics |

1: Introduction
• Meaning of economics
• Scarcity and choice
Topic 2: The price theory
• Theory of demand
• Theory of supply
Topic 3: Theory of the consumer
• Utility theory
Topic 4: Theory of the firm
• Production theory
Topic 5: Market structures
• Monopoly
• Oligopoly
"""

        topics = extract_topic_candidates(text)

        self.assertEqual([topic["title"] for topic in topics], [
            "Introduction",
            "The price theory",
            "Theory of the consumer",
            "Theory of the firm",
            "Market structures",
        ])
        self.assertEqual(topics[0]["subtopics"], ["Meaning of economics", "Scarcity and choice"])
        self.assertEqual(topics[-1]["subtopics"], ["Monopoly", "Oligopoly"])

    def test_visual_topic_matching_uses_specific_syllabus_evidence(self):
        topics = [
            SimpleNamespace(title="Introduction", subtopics=["Scarcity and choice", "Opportunity cost"]),
            SimpleNamespace(title="Theory of the firm", subtopics=["Production theory", "Theory of costs"]),
        ]

        matched, score, margin, evidence = score_topic_context(
            "The straight PPF illustrates constant opportunity cost in producing beans and maize.",
            topics,
        )

        self.assertIs(matched, topics[0])
        self.assertGreaterEqual(score, 6)
        self.assertGreaterEqual(margin, 3)
        self.assertIn("opportunity", evidence)
        self.assertIn("cost", evidence)

    def test_topic_section_pages_stop_at_the_next_explicit_syllabus_heading(self):
        topics = [
            SimpleNamespace(title="Introduction"),
            SimpleNamespace(title="The price theory"),
        ]
        text = (
            "--- Page 1 ---\n1: Introduction\nScarcity and choice.\n\n"
            "--- Page 2 ---\nThe introduction continues with opportunity cost.\n\n"
            "--- Page 3 ---\nTopic 2: The price theory\nDemand and supply.\n\n"
            "--- Page 4 ---\nThe introduction to equilibrium is brief."
        )

        sections, ambiguous_pages = map_pdf_topic_sections(text, topics)

        self.assertEqual(
            {page: topic.title for page, topic in sections.items()},
            {1: "Introduction", 2: "Introduction", 3: "The price theory", 4: "The price theory"},
        )
        self.assertEqual(ambiguous_pages, set())

    def test_topic_section_page_with_two_headings_is_ambiguous(self):
        topics = [SimpleNamespace(title="Introduction"), SimpleNamespace(title="The price theory")]

        sections, ambiguous_pages = map_pdf_topic_sections(
            "--- Page 1 ---\n1: Introduction\nTopic 2: The price theory",
            topics,
        )

        self.assertNotIn(1, sections)
        self.assertEqual(ambiguous_pages, {1})

    def test_contents_page_does_not_set_the_following_section_to_its_last_entry(self):
        topics = [
            SimpleNamespace(title="Introduction", subtopics=["Meaning of economics"]),
            SimpleNamespace(
                title="The price theory",
                subtopics=["Theory of demand", "Theory of supply"],
            ),
            SimpleNamespace(title="Theory of the consumer", subtopics=["Utility theory"]),
        ]
        text = (
            "--- Page 1 ---\n1: Introduction\nTopic 2: The price theory\n"
            "Topic 3: Theory of the consumer\n\n"
            "--- Page 2 ---\nTHE MEANING OF ECONOMICS.\nScarcity and choice.\n\n"
            "--- Page 3 ---\nTHE ELEMENTARY PRICE THEORY: DEMAND AND SUPPLY\n"
            "Demand and supply determine prices."
        )

        sections, ambiguous_pages = map_pdf_topic_sections(text, topics)

        self.assertEqual(ambiguous_pages, {1})
        self.assertEqual(sections[2].title, "Introduction")
        self.assertEqual(sections[3].title, "The price theory")

    def test_ambiguous_boundary_page_is_excluded_and_resets_section_state(self):
        topics = [
            SimpleNamespace(title="Theory of the consumer", subtopics=["Consumer surplus"]),
            SimpleNamespace(title="Theory of the firm", subtopics=["Theory of production", "Theory of costs"]),
        ]
        text = (
            "--- Page 1 ---\nTHE CONSUMER SURPLUS\n"
            "THE THEORY OF PRODUCTION AND COSTS\n\n"
            "--- Page 2 ---\nProduction continues with combinations of labour and capital."
        )

        sections, ambiguous_pages = map_pdf_topic_sections(text, topics)

        self.assertEqual(ambiguous_pages, {1})
        self.assertNotIn(1, sections)
        self.assertNotIn(2, sections)

    def test_topic_match_prefers_unique_oligopoly_evidence_over_shared_price_terms(self):
        topics = [
            SimpleNamespace(
                title="The price theory",
                subtopics=["Theory of demand", "Theory of supply", "Concept of equilibrium"],
            ),
            SimpleNamespace(
                title="Market structures",
                subtopics=["Monopoly", "Monopolistic competition", "Oligopoly"],
            ),
        ]

        matched, score, margin, evidence = score_topic_context(
            "Oligopolistic producers influence demand and supply; equilibrium depends on price.",
            topics,
        )

        self.assertIs(matched, topics[1])
        self.assertGreaterEqual(score, 6)
        self.assertGreaterEqual(margin, 3)
        self.assertIn("oligopoly", evidence)

    def test_pdf_text_extraction_preserves_page_boundaries(self):
        document = fitz.open()
        first_page = document.new_page()
        first_page.insert_text((40, 60), "First page source text remains separate.")
        second_page = document.new_page()
        second_page.insert_text((40, 60), "Second page source text remains separate.")
        pdf_bytes = document.tobytes()
        document.close()

        text, _, page_count = extract_text_pdfplumber(pdf_bytes)

        self.assertEqual(page_count, 2)
        self.assertIn("--- Page 1 ---", text)
        self.assertIn("--- Page 2 ---", text)
        self.assertLess(text.index("--- Page 1 ---"), text.index("--- Page 2 ---"))
        self.assertIn("First page source text", text)
        self.assertIn("Second page source text", text)

    @patch("services.prep_ingestion.render_pdf_pages_to_images", return_value=[b"jpeg-bytes"])
    @patch("services.prep_ingestion.requests.post")
    @override_settings(TOGETHERAI_API="test-key", TOGETHER_VISION_MODEL="test-vision-model")
    def test_scanned_ocr_disables_reasoning(self, post, _render):
        post.return_value.status_code = 200
        post.return_value.json.return_value = {
            "choices": [{"message": {"content": "Readable OCR text."}}],
        }

        result = extract_scanned_ocr_together(b"pdf-bytes", max_pages=1)

        self.assertIn("Readable OCR text.", result)
        self.assertEqual(post.call_args.kwargs["json"]["reasoning"], {"enabled": False})

    def test_text_only_pdf_has_page_metrics_but_no_visual_candidate(self):
        page_evidence, candidates = inspect_pdf_visual_candidates(
            build_pdf(text="A text-only lecture page with no figures or plots.")
        )

        self.assertEqual(len(page_evidence), 1)
        self.assertGreater(page_evidence[0]["text_chars"], 0)
        self.assertEqual(page_evidence[0]["candidate_region_count"], 0)
        self.assertEqual(candidates, [])

    def test_referenced_vector_graph_is_cropped_and_classified(self):
        page_evidence, candidates = inspect_pdf_visual_candidates(
            build_pdf(draw_graph=True)
        )

        self.assertEqual(page_evidence[0]["candidate_region_count"], 1)
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["visual_type"], "graph")
        self.assertEqual(candidates[0]["page_number"], 1)
        self.assertTrue(candidates[0]["crop_bytes"].startswith(b"\xff\xd8"))
        self.assertIn("vector_drawing_cluster", candidates[0]["candidate_reasons"])

    def test_vector_graph_crop_keeps_axis_labels_outside_the_strokes(self):
        document = fitz.open()
        page = document.new_page(width=600, height=800)
        page.insert_text((55, 225), "A sentence above this graph should stay outside the crop.", fontsize=12)
        page.insert_text((55, 370), "Price", fontsize=12)
        page.insert_text((300, 530), "Quantity", fontsize=12)
        page.draw_line((100, 500), (100, 250), width=1.5)
        page.draw_line((100, 500), (450, 500), width=1.5)
        page.draw_line((125, 290), (420, 450), width=2)
        pdf_bytes = document.tobytes()
        document.close()

        _, candidates = inspect_pdf_visual_candidates(pdf_bytes)
        source = fitz.open(stream=pdf_bytes, filetype="pdf")
        sentence_rect = source[0].search_for("A sentence above this graph should stay outside the crop.")[0]
        price_rect = source[0].search_for("Price")[0]
        quantity_rect = source[0].search_for("Quantity")[0]
        source.close()

        self.assertEqual(len(candidates), 1)
        x0, y0, x1, y1 = candidates[0]["bbox"]
        self.assertLessEqual(x0, price_rect.x0)
        self.assertGreaterEqual(y1, quantity_rect.y1)
        self.assertGreater(y0, sentence_rect.y1)

    def test_adjacent_vector_graph_crops_exclude_the_neighboring_graph(self):
        document = fitz.open()
        page = document.new_page(width=600, height=800)
        page.insert_text((48, 380), "Price of A", fontsize=12)
        page.insert_text((314, 380), "Price of", fontsize=12)
        page.insert_text((314, 393), "Good Z", fontsize=12)
        page.insert_text((130, 530), "Quantity A", fontsize=12)
        page.draw_line((100, 500), (100, 260), width=1.5)
        page.draw_line((100, 500), (311, 500), width=1.5)
        page.draw_line((110, 300), (300, 460), width=2)
        page.insert_text((380, 530), "Quantity B", fontsize=12)
        page.draw_line((360, 500), (360, 260), width=1.5)
        page.draw_line((350, 500), (500, 500), width=1.5)
        page.draw_line((370, 460), (490, 300), width=2)
        pdf_bytes = document.tobytes()
        document.close()

        _, candidates = inspect_pdf_visual_candidates(pdf_bytes)
        source = fitz.open(stream=pdf_bytes, filetype="pdf")
        price_a = source[0].search_for("Price of A")[0]
        price_b = source[0].search_for("Price of")[-1]
        good_z = source[0].search_for("Good Z")[0]
        source.close()

        self.assertEqual(len(candidates), 2)
        candidates.sort(key=lambda candidate: candidate["bbox"][0])
        self.assertGreater(candidates[1]["bbox"][0], 300)
        self.assertLessEqual(candidates[0]["bbox"][0], price_a.x0)
        self.assertGreaterEqual(candidates[0]["bbox"][2], price_a.x1)
        self.assertLessEqual(candidates[1]["bbox"][0], price_b.x0)
        self.assertGreaterEqual(candidates[1]["bbox"][2], good_z.x1)
        self.assertLess(candidates[0]["bbox"][2], price_b.x0)

    def test_vector_graph_crop_masks_neighbor_title_when_axis_label_extends_past_strokes(self):
        document = fitz.open()
        page = document.new_page(width=600, height=800)
        page.insert_text((275, 355), "Quantity", fontsize=12)
        page.insert_text((275, 368), "of X", fontsize=12)
        page.insert_text((314, 170), "Price of Good Z", fontsize=12)
        page.draw_line((163, 325), (163, 150), width=1.5)
        page.draw_line((163, 325), (311, 325), width=1.5)
        page.draw_line((180, 180), (300, 300), width=2)
        page.draw_line((360, 325), (360, 150), width=1.5)
        page.draw_line((360, 325), (508, 325), width=1.5)
        page.draw_line((370, 300), (495, 180), width=2)
        pdf_bytes = document.tobytes()
        document.close()

        _, candidates = inspect_pdf_visual_candidates(pdf_bytes)
        source = fitz.open(stream=pdf_bytes, filetype="pdf")
        title_rect = source[0].search_for("Price of Good Z")[0]
        source.close()
        candidates.sort(key=lambda candidate: candidate["bbox"][0])

        def dark_pixels_in_title(candidate):
            crop_rect = fitz.Rect(candidate["bbox"])
            overlap = crop_rect & title_rect
            image = Image.open(BytesIO(candidate["crop_bytes"])).convert("RGB")
            bounds = (
                max(0, int((overlap.x0 - crop_rect.x0) * 2)),
                max(0, int((overlap.y0 - crop_rect.y0) * 2)),
                min(image.width, int((overlap.x1 - crop_rect.x0) * 2)),
                min(image.height, int((overlap.y1 - crop_rect.y0) * 2)),
            )
            return sum(1 for pixel in image.crop(bounds).getdata() if min(pixel) < 200)

        self.assertEqual(len(candidates), 2)
        self.assertEqual(dark_pixels_in_title(candidates[0]), 0)
        self.assertGreater(dark_pixels_in_title(candidates[1]), 0)

    def test_flowchart_is_not_misclassified_as_a_graph(self):
        _, candidates = inspect_pdf_visual_candidates(build_pdf(draw_flowchart=True))

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["visual_type"], "diagram")

    def test_spaced_flow_chart_reference_is_not_misclassified_as_a_graph(self):
        document = fitz.open()
        page = document.new_page(width=600, height=800)
        page.insert_text((60, 120), "The flow chart is as follows")
        page.draw_rect(fitz.Rect(180, 220, 330, 270), width=1.5)
        page.draw_rect(fitz.Rect(180, 360, 330, 410), width=1.5)
        page.draw_line((255, 270), (255, 360), width=1.5)
        pdf_bytes = document.tobytes()
        document.close()

        _, candidates = inspect_pdf_visual_candidates(pdf_bytes)

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["visual_type"], "diagram")

    def test_ocr_replaces_only_weak_local_pages(self):
        local_text = (
            "--- Page 1 ---\nPoor scan\n\n"
            "--- Page 2 ---\n"
            "This page has enough selectable text to preserve the local extraction over duplicate OCR content. "
            "It contains a long explanation and multiple useful sentences."
        )
        ocr_text = (
            "--- Page 1 (Vision OCR) ---\nRecovered page one text from OCR.\n\n"
            "--- Page 2 (Vision OCR) ---\nDuplicate OCR version of page two text."
        )

        merged = merge_local_and_ocr_pages(local_text, ocr_text)

        self.assertIn("Recovered page one text from OCR", merged)
        self.assertIn("preserve the local extraction", merged)
        self.assertNotIn("Duplicate OCR version", merged)
        self.assertEqual(merged.count("--- Page 1"), 1)
        self.assertEqual(merged.count("--- Page 2"), 1)


class PdfVisualStorageTests(TestCase):
    def test_refresh_visual_crops_expands_existing_vector_crop_without_losing_assignment(self):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            document_pdf = fitz.open()
            page = document_pdf.new_page(width=600, height=800)
            page.insert_text((55, 370), "Price", fontsize=12)
            page.insert_text((300, 530), "Quantity", fontsize=12)
            page.draw_line((100, 500), (100, 250), width=1.5)
            page.draw_line((100, 500), (450, 500), width=1.5)
            page.draw_line((125, 290), (420, 450), width=2)
            pdf_bytes = document_pdf.tobytes()
            old_crop = page.get_pixmap(
                matrix=fitz.Matrix(2, 2),
                clip=fitz.Rect(90, 240, 460, 510),
                alpha=False,
            ).tobytes("jpeg")
            document_pdf.close()

            course = PrepCourse.objects.create(
                code="VIS 112",
                title="Crop Refresh Testing",
                slug="crop-refresh-testing",
            )
            source = PrepDocument.objects.create(
                course=course,
                file=SimpleUploadedFile("crop-refresh.pdf", pdf_bytes, content_type="application/pdf"),
                extracted_text="--- Page 1 ---\nA demand graph with axis labels.",
                stage="stage_3",
            )
            visual = PrepDocumentVisual.objects.create(
                document=source,
                candidate_key="a4" * 32,
                page_number=1,
                bbox=[90, 240, 460, 510],
                candidate_reasons=["vector_drawing_cluster"],
                crop=SimpleUploadedFile("demand.jpg", old_crop, content_type="image/jpeg"),
                status="approved",
                extracted_content={
                    "auto_topic": "Demand",
                    "auto_decision": "approved_high_confidence",
                },
            )
            old_name = visual.crop.name
            old_width = fitz.Pixmap(visual.crop.path).width

            call_command("refresh_visual_crops", document_id=str(source.pk), apply=True, stdout=StringIO())

            visual.refresh_from_db()
            new_width = fitz.Pixmap(visual.crop.path).width
            self.assertEqual(visual.crop.name, old_name)
            self.assertGreater(new_width, old_width)
            self.assertEqual(visual.status, "approved")
            self.assertEqual(visual.extracted_content["auto_topic"], "Demand")
            self.assertEqual(
                visual.extracted_content["crop_refinement_version"],
                "figure-sibling-label-ownership-v9",
            )

    def create_visual_candidate_for_review(self, code, title, context_text):
        pdf_bytes = build_pdf(draw_graph=True)
        course = PrepCourse.objects.create(
            code=code,
            title=title,
            slug=title.lower().replace(" ", "-"),
        )
        document = PrepDocument.objects.create(
            course=course,
            file=SimpleUploadedFile("figure.pdf", pdf_bytes, content_type="application/pdf"),
        )
        store_pdf_visual_candidates(document, pdf_bytes)
        visual = PrepDocumentVisual.objects.get(document=document)
        visual.context_text = context_text
        visual.save(update_fields=["context_text", "updated_at"])
        return visual

    def test_high_confidence_upload_match_waits_for_stage_three_source_approval(self):
        course = PrepCourse.objects.create(
            code="VIS 109",
            title="Opportunity Cost Testing",
            slug="opportunity-cost-testing",
        )
        topic = PrepTopic.objects.create(
            course=course,
            order=1,
            title="Scarcity and Choice",
            slug="scarcity-and-choice",
            subtopics=["Opportunity cost"],
        )
        document = PrepDocument.objects.create(
            course=course,
            file=SimpleUploadedFile("stage-two.pdf", build_pdf(draw_graph=True)),
            stage="stage_2",
            extracted_text=(
                "--- Page 1 ---\nThe concept of scarcity and opportunity cost. "
                "The straight PPF shows the available production choices."
            ),
        )
        visual = PrepDocumentVisual.objects.create(
            document=document,
            candidate_key="d" * 64,
            page_number=1,
            bbox=[20, 30, 200, 200],
            crop=SimpleUploadedFile("ppf.jpg", b"ppf", content_type="image/jpeg"),
            context_text="Scarcity opportunity cost straight PPF production choices",
        )

        suggestion = assign_visuals_to_topics(document, [topic])

        visual.refresh_from_db()
        self.assertEqual(suggestion["review"], 1)
        self.assertEqual(visual.status, "needs_review")
        self.assertEqual(
            visual.extracted_content["auto_decision"],
            "suggested_high_confidence_pending_source_approval",
        )

        document.stage = "stage_3"
        document.save(update_fields=["stage"])
        approved = assign_visuals_to_topics(document, [topic], allow_auto_approval=True)

        visual.refresh_from_db()
        self.assertEqual(approved["approved"], 1)
        self.assertEqual(visual.status, "approved")

    def test_ambiguous_topic_boundary_stays_in_review(self):
        course = PrepCourse.objects.create(
            code="VIS 110",
            title="Ambiguous Topic Boundary Testing",
            slug="ambiguous-topic-boundary-testing",
        )
        first_topic = PrepTopic.objects.create(
            course=course,
            order=1,
            title="Scarcity and Choice",
            slug="scarcity-and-choice",
            subtopics=["Opportunity cost"],
        )
        second_topic = PrepTopic.objects.create(
            course=course,
            order=2,
            title="Other Topic",
            slug="other-topic",
        )
        document = PrepDocument.objects.create(
            course=course,
            file=SimpleUploadedFile("ambiguous.pdf", build_pdf(draw_graph=True)),
            stage="stage_3",
            extracted_text=(
                "--- Page 1 ---\n1: Scarcity and Choice\n"
                "Topic 2: Other Topic\nA graph shows opportunity cost and production choices."
            ),
        )
        visual = PrepDocumentVisual.objects.create(
            document=document,
            candidate_key="e" * 64,
            page_number=1,
            bbox=[20, 30, 200, 200],
            crop=SimpleUploadedFile("ambiguous.jpg", b"ambiguous", content_type="image/jpeg"),
            context_text="Scarcity opportunity cost graph production choices",
        )

        result = assign_visuals_to_topics(document, [first_topic, second_topic], allow_auto_approval=True)

        visual.refresh_from_db()
        self.assertEqual(result["review"], 1)
        self.assertEqual(visual.status, "needs_review")
        self.assertEqual(visual.extracted_content["auto_decision"], "needs_review_ambiguous_section_boundary")

    def test_explicit_topic_section_overrides_keyword_match_for_visual(self):
        course = PrepCourse.objects.create(
            code="VIS 111",
            title="Section Based Assignment Testing",
            slug="section-based-assignment-testing",
        )
        first_topic = PrepTopic.objects.create(
            course=course,
            order=1,
            title="Scarcity and Choice",
            slug="scarcity-and-choice",
            subtopics=["Opportunity cost"],
        )
        second_topic = PrepTopic.objects.create(
            course=course,
            order=2,
            title="Market Structures",
            slug="market-structures",
            subtopics=["Oligopoly", "Kinked demand", "Marginal revenue", "Price discrimination"],
        )
        document = PrepDocument.objects.create(
            course=course,
            file=SimpleUploadedFile("sectioned.pdf", build_pdf(draw_graph=True)),
            stage="stage_3",
            extracted_text=(
                "--- Page 1 ---\n1: Scarcity and Choice\n"
                "An oligopoly graph shows a kinked demand curve, marginal revenue, and price discrimination."
            ),
        )
        visual = PrepDocumentVisual.objects.create(
            document=document,
            candidate_key="f" * 64,
            page_number=1,
            bbox=[20, 30, 200, 200],
            crop=SimpleUploadedFile("section-figure.jpg", b"section", content_type="image/jpeg"),
            context_text="oligopoly kinked demand marginal revenue price discrimination",
        )

        result = assign_visuals_to_topics(document, [first_topic, second_topic], allow_auto_approval=True)

        visual.refresh_from_db()
        self.assertEqual(result["review"], 1)
        self.assertEqual(visual.status, "needs_review")
        self.assertEqual(visual.extracted_content["auto_topic"], first_topic.title)
        self.assertEqual(
            visual.extracted_content["auto_match_method"],
            "pdf_topic_section_context_needs_review",
        )

    def test_admin_can_review_visual_and_manual_assignment_is_preserved(self):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            course = PrepCourse.objects.create(
                code="VIS 120",
                title="Visual Admin Review Testing",
                slug="visual-admin-review-testing",
            )
            selected_topic = PrepTopic.objects.create(
                course=course,
                order=1,
                title="Scarcity and Choice",
                slug="visual-review-scarcity",
            )
            heading_topic = PrepTopic.objects.create(
                course=course,
                order=2,
                title="Market Structures",
                slug="visual-review-markets",
            )
            document = PrepDocument.objects.create(
                course=course,
                file=SimpleUploadedFile("visual-review.pdf", build_pdf(draw_graph=True)),
                stage="stage_3",
                extracted_text="--- Page 1 ---\n2: Market Structures\nA graph shows price and quantity.",
            )
            visual = PrepDocumentVisual.objects.create(
                document=document,
                candidate_key="a5" * 32,
                page_number=1,
                bbox=[20, 30, 200, 200],
                crop=SimpleUploadedFile("review-figure.jpg", b"figure", content_type="image/jpeg"),
                context_crop=SimpleUploadedFile("review-context.jpg", b"context", content_type="image/jpeg"),
                status="needs_review",
                extracted_content={"context_before": "Market Structures heading"},
            )
            reviewer = User.objects.create_user(
                username="visual_admin_reviewer",
                email="visual-admin-reviewer@example.test",
                password="Valid123",
            )
            reviewer.is_staff = True
            reviewer.is_superuser = True
            reviewer.save(update_fields=["is_staff", "is_superuser"])
            self.client.force_login(reviewer)

            self.assertIsInstance(admin.site._registry[PrepDocumentVisual], PrepDocumentVisualAdmin)
            change_url = reverse("admin:prep_prepdocumentvisual_change", args=[visual.pk])
            response = self.client.get(change_url)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "Full-width neighboring context")
            self.assertContains(response, "Adjust crop on original PDF page")
            self.assertContains(response, "Market Structures heading")
            source_page_url = reverse("admin:prep_prepdocumentvisual_source_page", args=[visual.pk])
            source_page_response = self.client.get(source_page_url)
            self.assertEqual(source_page_response.status_code, 200)
            self.assertEqual(source_page_response["Content-Type"], "image/png")
            old_crop_name = visual.crop.name

            response = self.client.post(change_url, {
                "status": "approved",
                "reviewed_topic": str(selected_topic.pk),
                "review_notes": "Figure evidence supports this topic.",
                "bbox": json.dumps([80, 100, 480, 540]),
                "_save": "Save",
            })

            self.assertEqual(response.status_code, 302)
            visual.refresh_from_db()
            self.assertEqual(visual.status, "approved")
            self.assertEqual(visual.reviewed_topic, selected_topic)
            self.assertEqual(visual.reviewed_by, reviewer)
            self.assertIsNotNone(visual.reviewed_at)
            self.assertEqual(visual.review_notes, "Figure evidence supports this topic.")
            self.assertEqual(visual.extracted_content["auto_decision"], "tutor_approved")
            self.assertEqual(visual.bbox, [80, 100, 480, 540])
            self.assertNotEqual(visual.crop.name, old_crop_name)
            with visual.crop.storage.open(visual.crop.name, "rb") as crop_file:
                updated_crop = crop_file.read()
            self.assertTrue(updated_crop.startswith(b"\xff\xd8"))
            self.assertEqual(Image.open(BytesIO(updated_crop)).size, (800, 880))
            topic_list_url = reverse("admin:prep_prepdocumentvisual_changelist")
            topic_list_response = self.client.get(topic_list_url, {"visual_topic": str(selected_topic.pk)})
            self.assertEqual(topic_list_response.status_code, 200)
            self.assertContains(topic_list_response, selected_topic.title)

            assignments = assign_visuals_to_topics(
                document,
                [selected_topic, heading_topic],
                allow_auto_approval=True,
            )
            visual.refresh_from_db()
            self.assertEqual(assignments["approved"], 0)
            self.assertEqual(visual.reviewed_topic, selected_topic)
            self.assertEqual(visual.extracted_content["auto_decision"], "tutor_approved")

            rejected_visual = PrepDocumentVisual.objects.create(
                document=document,
                candidate_key="a6" * 32,
                page_number=1,
                bbox=[210, 30, 390, 200],
                crop=SimpleUploadedFile("irrelevant-figure.jpg", b"figure", content_type="image/jpeg"),
                status="needs_review",
            )
            rejected_url = reverse("admin:prep_prepdocumentvisual_change", args=[rejected_visual.pk])
            response = self.client.post(rejected_url, {
                "status": "rejected",
                "reviewed_topic": "",
                "review_notes": "This figure is unrelated to the course topic.",
                "bbox": json.dumps(rejected_visual.bbox),
                "_save": "Save",
            })
            self.assertEqual(response.status_code, 302)
            rejected_visual.refresh_from_db()
            self.assertEqual(rejected_visual.status, "rejected")
            self.assertEqual(rejected_visual.reviewed_by, reviewer)
            self.assertEqual(rejected_visual.extracted_content["auto_decision"], "tutor_rejected")

    @patch("services.prep_ingestion.upload_to_github_storage", return_value="")
    def test_document_ingestion_keeps_text_and_persists_visual_candidates_without_vision(self, _upload):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            pdf_bytes = build_pdf(
                text=("Selectable lecture text remains available for local extraction. " * 8),
                draw_graph=True,
            )
            course = PrepCourse.objects.create(
                code="VIS 100",
                title="Visual Ingestion Testing",
                slug="visual-ingestion-testing",
            )
            document = PrepDocument.objects.create(
                course=course,
                doc_type="Final Examination Paper",
                file=SimpleUploadedFile("mixed.pdf", pdf_bytes, content_type="application/pdf"),
            )

            result = process_prep_document(document)

            document.refresh_from_db()
            self.assertTrue(result["success"], result)
            self.assertEqual(result["method_used"], "digital_pdfplumber")
            self.assertGreater(result["visual_candidates"], 0)
            self.assertIn("Selectable lecture text remains available", document.extracted_text)
            self.assertGreater(document.page_evidence[0]["text_chars"], 0)
            self.assertTrue(PrepDocumentVisual.objects.filter(document=document, status="candidate").exists())
            self.assertEqual(document.validation_report["status"], "needs_review")
            self.assertIn("approved_content_rules_missing", {
                issue["code"] for issue in document.validation_report["issues"]
            })

    @patch("services.prep_ingestion.upload_to_github_storage", return_value="")
    @patch("services.prep_ingestion.extract_scanned_ocr_together")
    def test_ingestion_persists_disallowed_graph_issue_with_page_provenance(self, ocr, _upload):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            course = PrepCourse.objects.create(
                code="VIS 105",
                title="Restricted Graph Testing",
                slug="restricted-graph-testing",
                study_profile_version=1,
                study_profile={
                    "content_rules": {
                        "schema_version": 1,
                        "modalities": {
                            "graphs": {
                                "policy": "disallowed",
                                "rationale": "The approved topic source contains no graphs.",
                            },
                        },
                    },
                },
            )
            document = PrepDocument.objects.create(
                course=course,
                doc_type="Final Examination Paper",
                file=SimpleUploadedFile(
                    "restricted.pdf",
                    build_pdf(
                        text="The approved examination source includes a supported graph and explanatory course context. " * 5,
                        draw_graph=True,
                    ),
                    content_type="application/pdf",
                ),
            )

            result = process_prep_document(document)

            document.refresh_from_db()
            self.assertEqual(
                set(document.validation_report["detected_modalities"]),
                {"graphs", "text"},
                document.validation_report,
            )
            disallowed = next(
                issue for issue in document.validation_report["issues"]
                if issue["code"] == "modality_disallowed" and issue["modality"] == "graphs"
            )
            self.assertTrue(result["success"], result)
            self.assertEqual(document.stage, "stage_2")
            self.assertEqual(document.validation_report["status"], "needs_review")
            self.assertEqual(disallowed["modality"], "graphs")
            self.assertEqual(disallowed["provenance"]["page_number"], 1)
            ocr.assert_not_called()

    def test_page_evidence_and_crop_are_saved_separately_from_transcription(self):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            pdf_bytes = build_pdf(draw_graph=True)
            course = PrepCourse.objects.create(
                code="VIS 101",
                title="Visual Evidence Testing",
                slug="visual-evidence-testing",
            )
            document = PrepDocument.objects.create(
                course=course,
                file=SimpleUploadedFile("visual.pdf", pdf_bytes, content_type="application/pdf"),
                extracted_text="Local transcription stays unchanged.",
            )

            candidate_count = store_pdf_visual_candidates(document, pdf_bytes)

            document.refresh_from_db()
            visual = PrepDocumentVisual.objects.get(document=document)
            self.assertEqual(candidate_count, 1)
            self.assertEqual(document.extracted_text, "Local transcription stays unchanged.")
            self.assertEqual(document.page_evidence[0]["page_number"], 1)
            self.assertTrue(visual.crop.name)
            self.assertTrue(visual.context_crop.name)
            self.assertIn("context_before", visual.extracted_content)
            self.assertIn("context_after", visual.extracted_content)
            self.assertEqual(visual.status, "candidate")

    @patch("services.prep_ingestion.requests.post")
    @override_settings(TOGETHERAI_API="test-key", TOGETHER_VISION_MODEL="test-vision-model")
    def test_vision_inspection_persists_structured_data_without_approving_it(self, post):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            pdf_bytes = build_pdf(draw_graph=True)
            course = PrepCourse.objects.create(
                code="VIS 102",
                title="Visual Inspection Testing",
                slug="visual-inspection-testing",
            )
            document = PrepDocument.objects.create(
                course=course,
                file=SimpleUploadedFile("graph.pdf", pdf_bytes, content_type="application/pdf"),
            )
            store_pdf_visual_candidates(document, pdf_bytes)
            visual = PrepDocumentVisual.objects.get(document=document)
            post.return_value.json.return_value = {
                "choices": [{"message": {"content": json.dumps({
                    "visual_type": "graph",
                    "caption": "Demand graph",
                    "visible_labels": ["Price", "Quantity"],
                    "axes": {"x_label": "Quantity", "y_label": "Price", "units": None},
                    "elements": ["Downward-sloping demand curve"],
                    "relationships": ["Price and quantity demanded move in opposite directions"],
                    "data_points": [],
                    "qualitative_summary": "Qualitative downward-sloping demand curve.",
                    "uncertainties": [],
                    "confidence": 0.92,
                })}}],
                "usage": {"prompt_tokens": 100, "completion_tokens": 50, "total_tokens": 150},
            }

            result = inspect_visual_candidate_with_vision(visual)

            visual.refresh_from_db()
            self.assertTrue(result["success"])
            self.assertEqual(visual.status, "inspected")
            self.assertEqual(visual.labels, ["Price", "Quantity"])
            self.assertEqual(visual.vision_usage["total_tokens"], 150)
            self.assertNotEqual(visual.status, "approved")
            self.assertEqual(post.call_args.kwargs["json"]["reasoning"], {"enabled": False})
            vision_text = post.call_args.kwargs["json"]["messages"][1]["content"][0]["text"]
            self.assertIn("Text immediately before the figure", vision_text)
            self.assertIn("Text immediately after the figure", vision_text)
            self.assertEqual(post.call_count, 1)

    @patch("services.prep_ingestion.requests.post")
    @override_settings(TOGETHERAI_API="test-key", TOGETHER_VISION_MODEL="test-vision-model")
    def test_conflicting_ode_mass_labels_are_held_for_review_at_high_confidence(self, post):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            visual = self.create_visual_candidate_for_review(
                "VIS 106",
                "ODE Label Conflict Testing",
                "Let A1 and A2 be the two masses. Their displacements are x1 and x2 from O1 and O2; springs S1 and S2.",
            )
            post.return_value.json.return_value = {
                "choices": [{"message": {"content": json.dumps({
                    "visual_type": "diagram",
                    "visible_labels": ["N1", "N2", "S1", "S2", "x1", "x2", "O1", "O2"],
                    "relationships": ["N1 is attached to S1."],
                    "uncertainties": [],
                    "confidence": 0.95,
                })}}],
                "usage": {"total_tokens": 30},
            }

            result = inspect_visual_candidate_with_vision(visual)

            visual.refresh_from_db()
            self.assertTrue(result["success"])
            self.assertEqual(result["status"], "needs_review")
            self.assertEqual(visual.status, "needs_review")
            self.assertGreaterEqual(visual.confidence, 0.8)
            self.assertTrue(any("N1" in issue and "A1" in issue for issue in result["source_conflicts"]))
            self.assertIn("source_conflicts", visual.extracted_content)

    @patch("services.prep_ingestion.requests.post")
    @override_settings(TOGETHERAI_API="test-key", TOGETHER_VISION_MODEL="test-vision-model")
    def test_omitted_kink_and_mr_discontinuity_are_held_for_review(self, post):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            visual = self.create_visual_candidate_for_review(
                "VIS 107",
                "Kinked Demand Conflict Testing",
                "The kink in the demand curve means the MR curve is discontinuous at the corresponding output. Segment DR is the upper demand portion; the segment from S is the lower portion.",
            )
            post.return_value.json.return_value = {
                "choices": [{"message": {"content": json.dumps({
                    "visual_type": "graph",
                    "visible_labels": ["D", "E", "R", "S", "MR", "Output", "P*", "Q*"],
                    "axes": {"x_label": "Output", "y_label": "Price"},
                    "elements": ["Downward demand curve", "Marginal revenue curve"],
                    "relationships": ["Demand slopes downward.", "MR lies below demand."],
                    "data_points": [],
                    "qualitative_summary": "Demand and marginal revenue curves.",
                    "uncertainties": [],
                    "confidence": 0.97,
                })}}],
                "usage": {"total_tokens": 30},
            }

            result = inspect_visual_candidate_with_vision(visual)

            visual.refresh_from_db()
            self.assertTrue(result["success"])
            self.assertEqual(result["status"], "needs_review")
            self.assertEqual(visual.status, "needs_review")
            self.assertTrue(any("kink" in issue.lower() for issue in result["source_conflicts"]))
            self.assertTrue(any("discontinuous marginal revenue" in issue.lower() for issue in result["source_conflicts"]))

    @patch("services.prep_ingestion.requests.post")
    def test_visual_inspection_management_command_is_dry_run_by_default(self, post):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            pdf_bytes = build_pdf(draw_graph=True)
            course = PrepCourse.objects.create(
                code="VIS 103",
                title="Visual Command Testing",
                slug="visual-command-testing",
            )
            document = PrepDocument.objects.create(
                course=course,
                file=SimpleUploadedFile("command.pdf", pdf_bytes, content_type="application/pdf"),
            )
            store_pdf_visual_candidates(document, pdf_bytes)
            output = StringIO()

            call_command(
                "inspect_pdf_visuals",
                "--document-id", str(document.pk),
                stdout=output,
            )

            self.assertIn("Dry run only", output.getvalue())
            post.assert_not_called()

    @patch("services.prep_ingestion.requests.post")
    @override_settings(TOGETHERAI_API="test-key", TOGETHER_VISION_MODEL="test-vision-model")
    def test_visual_inspection_command_reports_source_conflicts_as_needs_review(self, post):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            pdf_bytes = build_pdf(draw_graph=True)
            course = PrepCourse.objects.create(
                code="VIS 108",
                title="Visual Review Command Testing",
                slug="visual-review-command-testing",
            )
            document = PrepDocument.objects.create(
                course=course,
                file=SimpleUploadedFile("command-review.pdf", pdf_bytes, content_type="application/pdf"),
            )
            store_pdf_visual_candidates(document, pdf_bytes)
            visual = PrepDocumentVisual.objects.get(document=document)
            visual.context_text = "The source diagram labels the two masses A1 and A2 and their spring S1."
            visual.save(update_fields=["context_text", "updated_at"])
            post.return_value.json.return_value = {
                "choices": [{"message": {"content": json.dumps({
                    "visual_type": "diagram",
                    "visible_labels": ["N1", "A2", "S1"],
                    "relationships": [],
                    "uncertainties": [],
                    "confidence": 0.98,
                })}}],
                "usage": {},
            }
            output = StringIO()

            call_command(
                "inspect_pdf_visuals",
                "--document-id", str(document.pk),
                "--execute",
                stdout=output,
            )

            visual.refresh_from_db()
            self.assertEqual(visual.status, "needs_review")
            self.assertIn("Needs review on page", output.getvalue())
            self.assertIn("N1", output.getvalue())
            self.assertIn("1 require tutor review", output.getvalue())

    @patch("services.prep_ingestion.requests.post")
    @override_settings(TOGETHERAI_API="test-key", TOGETHER_VISION_MODEL="test-vision-model")
    def test_reasoning_only_provider_response_is_recorded_as_error_with_usage(self, post):
        with tempfile.TemporaryDirectory() as media_root, override_settings(MEDIA_ROOT=media_root):
            pdf_bytes = build_pdf(draw_graph=True)
            course = PrepCourse.objects.create(
                code="VIS 104",
                title="Vision Empty Final Testing",
                slug="vision-empty-final-testing",
            )
            document = PrepDocument.objects.create(
                course=course,
                file=SimpleUploadedFile("reasoning.pdf", pdf_bytes, content_type="application/pdf"),
            )
            store_pdf_visual_candidates(document, pdf_bytes)
            visual = PrepDocumentVisual.objects.get(document=document)
            post.return_value.json.return_value = {
                "choices": [{"message": {"reasoning_content": "internal reasoning only"}, "finish_reason": "length"}],
                "usage": {"completion_tokens": 1500, "reasoning_tokens": 1500},
            }

            result = inspect_visual_candidate_with_vision(visual)

            visual.refresh_from_db()
            self.assertFalse(result["success"])
            self.assertEqual(visual.status, "error")
            self.assertIn("finish_reason=length", visual.inspection_error)
            self.assertEqual(visual.vision_usage["reasoning_tokens"], 1500)