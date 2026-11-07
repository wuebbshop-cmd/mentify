from django.test import TestCase

from prep.models import PrepContentCache, PrepCourse, PrepTopic
from prep.views import _get_course_topics_summary
from services.prep_ai_router import NOTE_VALIDATION_STATE


class CourseTopicSummaryTests(TestCase):
    def setUp(self):
        self.course = PrepCourse.objects.create(
            code="SUM 101",
            title="Summary test course",
            slug="summary-test-course",
        )
        self.topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Validated notes",
            slug="validated-notes",
        )

    def _cache_note(self, key, payload):
        return PrepContentCache.objects.create(
            cache_key=key,
            content_type="topic_notes",
            prompt_hash=key.ljust(64, "x")[:64],
            course=self.course,
            topic=self.topic,
            payload=payload,
        )

    def test_readiness_dots_count_only_validated_nonempty_note_payloads(self):
        # Prime the course summary cache first. Saving the valid entry below must
        # invalidate it so the course page immediately reflects ready notes.
        initial_topics, _ = _get_course_topics_summary(self.course)
        self.assertEqual(initial_topics[0]["ready_levels_count"], 0)

        valid = {"validation_state": NOTE_VALIDATION_STATE, "level": "level_2", "content": "Ready notes."}
        self._cache_note("arbitrary-cache-key", valid)
        self._cache_note("pending-level-one", {"level": "level_1", "content": "Awaiting validation."})
        self._cache_note("empty-level-three", {
            "validation_state": NOTE_VALIDATION_STATE,
            "level": "level_3",
            "content": "",
        })
        self._cache_note("skipped-level-one", {
            "validation_state": NOTE_VALIDATION_STATE,
            "review_status": "skipped_no_source",
            "level": "level_1",
            "content": "Do not show this.",
        })
        self._cache_note("valid-level-three", {
            "validation_state": NOTE_VALIDATION_STATE,
            "level": "level_3",
            "notes": "Also ready.",
        })

        topics, _ = _get_course_topics_summary(self.course)

        self.assertEqual(topics[0]["ready_levels_count"], 2)
        self.assertEqual(
            [item["key"] for item in topics[0]["ready_levels"]],
            ["level_2", "level_3"],
        )
