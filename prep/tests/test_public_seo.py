from types import SimpleNamespace

from django.template.loader import render_to_string
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from prep.models import PrepContentCache, PrepCourse, PrepPaper, PrepQuestion, PrepTopic
from prep.views import _public_topic_notes, _resolve_course_category_meta


class CourseCategoryIconTests(SimpleTestCase):
    def test_general_sciences_and_other_resolve_to_distinct_icons(self):
        general_science = _resolve_course_category_meta(SimpleNamespace(
            code="SCI 101",
            title="General Science",
            category="General Sciences",
            study_profile={},
        ))
        other = _resolve_course_category_meta(SimpleNamespace(
            code="GEN 101",
            title="Interdisciplinary Studies",
            category="Other",
            study_profile={},
        ))

        self.assertEqual(general_science["subject_key"], "general_science")
        self.assertEqual(other["subject_key"], "other")
        self.assertNotEqual(general_science["subject_key"], other["subject_key"])

    def test_other_category_still_allows_known_course_inference(self):
        course = SimpleNamespace(
            code="ECO 101",
            title="Introduction to Economics",
            category="Other",
            study_profile={},
        )

        self.assertEqual(
            _resolve_course_category_meta(course),
            {"subject_key": "economics", "category": "Economics"},
        )

    def test_general_sciences_and_other_have_dedicated_svg_tiles(self):
        general_science = render_to_string(
            "prep/includes/course_type_icon.html",
            {"subject_key": "general_science", "category": "General Sciences"},
        )
        other = render_to_string(
            "prep/includes/course_type_icon.html",
            {"subject_key": "other", "category": "Other"},
        )

        self.assertIn("is-general-science", general_science)
        self.assertIn("<svg", general_science)
        self.assertIn("is-other", other)
        self.assertIn("<svg", other)
        self.assertNotIn("is-mathematics", other)


class PublicPrepSeoTests(TestCase):
    def setUp(self):
        self.course = PrepCourse.objects.create(
            code="SEO 101",
            title="Search Ready Mathematics",
            slug="seo-101",
            level="Standard",
            description="A public test course for structured study resources.",
        )
        self.topic = PrepTopic.objects.create(
            course=self.course,
            title="Sequences",
            slug="sequences",
            order=1,
        )
        PrepContentCache.objects.create(
            cache_key="seo-public-notes",
            content_type="topic_notes",
            prompt_hash="seo-test",
            course=self.course,
            topic=self.topic,
            payload={
                "content": "## 1. Core Concept Overview & Intuition\n\nA sequence is an ordered list.\n\n## 2. Mathematical Formalization & Core Definitions\n\nA sequence is a function from the natural numbers to a set of values.\n\n## 3. Key Theorems & Essential Results\n\nConvergent sequences have a unique limit.\n\n## 4. Worked Exemplar Problem with Step-by-Step Solution\n\nFor $a_n = 1/n$, the terms become arbitrarily close to zero as $n$ grows.\n\n## 5. High-Yield Exam Takeaways & Common Pitfalls\n\nCheck the stated domain, identify the candidate limit, and justify every limit law used. Do not confuse a bounded sequence with a convergent sequence: boundedness alone is not sufficient. Compare subsequences whenever a proposed limit appears doubtful.",
            },
        )
        paper = PrepPaper.objects.create(
            id="seo-paper",
            course=self.course,
            title="Final Examination",
            year="2026",
            total_marks=10,
            is_published=True,
        )
        PrepQuestion.objects.create(
            paper=paper,
            topic=self.topic,
            question_type="authentic",
            verification_status="verified",
            number=1,
            marks=10,
            question_latex="Find the limit of the sequence.",
            solution_latex="The sequence converges.",
        )
        PrepQuestion.objects.create(
            paper=paper,
            topic=self.topic,
            question_type="authentic",
            verification_status="verified",
            number=2,
            marks=5,
            question_latex="PUBLIC_CORRUPTED_MARKER: explain this value (cid:40) from the source.",
            solution_latex="Should not be shown.",
        )

    def test_public_library_and_resources_are_anonymous_and_indexable(self):
        library = self.client.get(reverse("prep:public_library"))
        course = self.client.get(reverse("prep:public_course", args=[self.course.slug]))
        topic = self.client.get(
            reverse("prep:public_topic", args=[self.course.slug, self.topic.id, self.topic.slug])
        )

        self.assertEqual(library.status_code, 200)
        self.assertContains(library, "Mentify Prep")
        self.assertEqual(course.status_code, 200)
        self.assertContains(course, "Sequences")
        self.assertEqual(topic.status_code, 200)
        self.assertContains(topic, "A sequence is an ordered list.")
        self.assertContains(topic, "Find the limit of the sequence.")
        self.assertNotContains(topic, "PUBLIC_CORRUPTED_MARKER")
        self.assertNotContains(course, "Undergraduate")
        self.assertNotContains(topic, "Undergraduate")
        self.assertNotContains(library, "Undergraduate")
        self.assertContains(topic, 'name="robots" content="index, follow')
        self.assertContains(topic, '"@type":"LearningResource"')

    def test_sitemap_lists_public_prep_library_course_and_topic(self):
        response = self.client.get("/sitemap.xml")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "/prep/library/")
        self.assertContains(response, f"/prep/library/{self.course.slug}/")
        self.assertContains(response, f"/prep/library/{self.course.slug}/{self.topic.id}-{self.topic.slug}/")

    def test_public_notes_withhold_an_image_without_approved_crop_reference(self):
        topic = PrepTopic.objects.create(
            course=self.course,
            title="Unsafe Figure Topic",
            slug="unsafe-figure-topic",
            order=2,
        )
        content = (
            "## 1. One\n\nA source-grounded introduction with explanatory material.\n\n"
            "## 2. Two\n\nAn explanation of the topic and its supported definitions.\n\n"
            "## 3. Three\n\nA relevant source-grounded example.\n\n"
            "## 4. Four\n\n![Unapproved diagram](/media/invented/diagram.png)\n\n"
            "## 5. Five\n\nA substantial final review section that summarizes the approved material, explains a common misconception, and reminds students how to check their answers against the source."
        )
        PrepContentCache.objects.create(
            cache_key="notes:published:unsafe-figure-topic:level_2",
            content_type="topic_notes",
            prompt_hash="unsafe-figure-test",
            course=self.course,
            topic=topic,
            payload={
                "content": content,
                "level": "level_2",
                "validation_state": "validated-v3-source-modalities",
                "source_references": [],
            },
        )

        public_notes, _ = _public_topic_notes(topic)

        self.assertEqual(public_notes, "")
