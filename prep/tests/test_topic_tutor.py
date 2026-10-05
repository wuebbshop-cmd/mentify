from types import SimpleNamespace
from unittest.mock import Mock, patch

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import SimpleTestCase, TestCase, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

from prep.models import (
    PrepCourse,
    PrepCourseEnrollment,
    PrepTopic,
    PrepTopicChatMessage,
    PrepTopicChatSession,
    PrepTopicChatUpload,
    PrepTransaction,
    PrepWallet,
)
from services.credit_service import grant_credits
from services import prep_topic_tutor


class TopicTutorUploadTests(SimpleTestCase):
    def test_image_with_pdf_filename_still_uses_detected_image_limit(self):
        image = SimpleUploadedFile(
            "notes.pdf",
            b"\x89PNG\r\n\x1a\n" + b"x" * (prep_topic_tutor.MAX_IMAGE_BYTES + 1),
            content_type="image/png",
        )

        with self.assertRaisesRegex(prep_topic_tutor.TopicTutorError, "4 MB image limit"):
            prep_topic_tutor._prepare_uploads([image])

    def test_duplicate_image_names_get_distinct_ocr_labels(self):
        image_bytes = b"\x89PNG\r\n\x1a\n" + b"readable image"
        uploads = [
            SimpleUploadedFile("notes.png", image_bytes, content_type="image/png"),
            SimpleUploadedFile("notes.png", image_bytes, content_type="image/png"),
        ]

        prepared, images = prep_topic_tutor._prepare_uploads(uploads)

        self.assertEqual(len(prepared), 2)
        self.assertEqual(len({image["label"] for image in images}), 2)
        self.assertEqual(prepared[0]["vision_labels"], ["notes.png image 1"])
        self.assertEqual(prepared[1]["vision_labels"], ["notes.png image 2"])

    def test_rejects_more_than_three_images(self):
        image_bytes = b"\x89PNG\r\n\x1a\n" + b"pixels"
        uploads = [
            SimpleUploadedFile(f"image-{index}.png", image_bytes, content_type="image/png")
            for index in range(4)
        ]

        with self.assertRaisesRegex(prep_topic_tutor.TopicTutorError, "no more than 3 images"):
            prep_topic_tutor._prepare_uploads(uploads)

    def test_text_pdf_is_limited_to_four_pages(self):
        pdf = SimpleUploadedFile("notes.pdf", b"%PDF-1.7 body", content_type="application/pdf")
        readable_text = " ".join(f"topic concept word{index}" for index in range(60))
        with patch.object(prep_topic_tutor, "_pdf_text_and_pages", return_value=(readable_text, 5)):
            with self.assertRaisesRegex(prep_topic_tutor.TopicTutorError, "no more than 4 pages"):
                prep_topic_tutor._prepare_uploads([pdf])


class TopicTutorSafetyTests(SimpleTestCase):
    def setUp(self):
        self.topic = SimpleNamespace(
            title="Properties of Estimators",
            subtopics=["unbiasedness", "estimator bias"],
            summary="Unbiasedness, bias, and estimator variance.",
        )

    def test_rejects_html_and_markdown_links_in_model_output(self):
        for answer in (
            "<script>alert(1)</script>",
            "Read [this page](https://example.com) for more.",
            "![diagram](https://example.com/image.png)",
        ):
            with self.subTest(answer=answer):
                with self.assertRaises(prep_topic_tutor.TopicTutorError):
                    prep_topic_tutor._safe_answer({"decision": "answer", "answer": answer}, self.topic)

    def test_out_of_scope_response_is_fixed_and_does_not_echo_the_request(self):
        response = prep_topic_tutor._safe_answer(
            {"decision": "out_of_scope", "answer": "the secret implementation"},
            self.topic,
        )

        self.assertIn("can’t discuss AI models", response)
        self.assertNotIn("secret implementation", response)

    @override_settings(TOGETHERAI_API="test-token", TOGETHER_VISION_MODEL="test-ocr")
    def test_ocr_parse_failure_keeps_provider_usage_for_billing(self):
        response = Mock()
        response.status_code = 200
        response.json.return_value = {
            "usage": {"prompt_tokens": 1200, "completion_tokens": 15, "total_tokens": 1215},
            "choices": [{"message": {"content": "not valid JSON"}}],
        }
        with patch.object(prep_topic_tutor.requests, "post", return_value=response):
            with self.assertRaises(prep_topic_tutor.TopicTutorError) as caught:
                prep_topic_tutor._ocr_images([{
                    "label": "page 1",
                    "mime_type": "image/jpeg",
                    "bytes": b"jpeg data",
                }])

        self.assertEqual(caught.exception.status, 502)
        self.assertEqual(caught.exception.usage["total_tokens"], 1215)
        self.assertEqual(caught.exception.model_name, "test-ocr")

    def test_upload_validation_error_after_ocr_retains_usage(self):
        usage = {"total_tokens": 1800}
        image = {"label": "notes.png image 1"}
        prepared = [{
            "name": "notes.png",
            "text": "",
            "page_count": 1,
            "source_type": "image_ocr",
            "vision_labels": [image["label"]],
        }]
        ocr_result = {
            "items": {
                image["label"]: {
                    "content_type": "unreadable",
                    "extracted_text": "",
                }
            },
            "usage": usage,
            "model": "test-ocr",
        }

        with patch.object(prep_topic_tutor, "_ocr_images", return_value=ocr_result):
            with self.assertRaises(prep_topic_tutor.TopicTutorError) as caught:
                prep_topic_tutor._finish_uploads(prepared, [image], self.topic, "")

        self.assertEqual(caught.exception.usage, usage)
        self.assertEqual(caught.exception.model_name, "test-ocr")

    def test_text_pdf_must_be_readable_and_relevant_before_acceptance(self):
        text = (
            "Properties of Estimators: an unbiased estimator has an expected value equal "
            "to the true parameter across repeated samples and its bias measures the "
            "difference between that expectation and the true value."
        )
        prepared = [{
            "name": "estimators.pdf",
            "text": text,
            "page_count": 1,
            "source_type": "text_pdf",
        }]

        accepted, usage, model = prep_topic_tutor._finish_uploads(
            prepared, [], self.topic, "unbiasedness bias estimator variance"
        )

        self.assertEqual(accepted[0]["text"], text)
        self.assertEqual(usage, {})
        self.assertEqual(model, "")

        unrelated = [{
            **prepared[0],
            "text": (
                "Botany explains flower petals, roots, leaves, soil, seeds, stems, "
                "photosynthesis, pollination, and plant growth across many seasons."
            ),
        }]
        with self.assertRaisesRegex(prep_topic_tutor.TopicTutorError, "does not appear related"):
            prep_topic_tutor._finish_uploads(unrelated, [], self.topic, "")


class TopicTutorApiTests(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.user = user_model.objects.create_user(
            username="topic-tutor-learner",
            email="topic-tutor@example.test",
            password="test-password-123",
        )
        self.other_user = user_model.objects.create_user(
            username="topic-tutor-other",
            email="topic-tutor-other@example.test",
            password="test-password-123",
        )
        self.course = PrepCourse.objects.create(
            code="STA 210",
            title="Statistical Inference",
            slug="sta-210-tutor-test",
            category="Statistics",
        )
        self.topic = PrepTopic.objects.create(
            course=self.course,
            title="Properties of Estimators",
            slug="properties-of-estimators-tutor-test",
            order=1,
            summary="Unbiasedness, bias, and estimator variance.",
        )
        PrepCourseEnrollment.objects.create(user=self.user, course=self.course)
        self.wallet = PrepWallet.get_or_create_wallet(self.user)
        self.wallet.credit_grants.update(remaining_credits=0)
        self.wallet.current_plan = "plus"
        self.wallet.plan_expires_at = timezone.now() + timedelta(days=30)
        self.wallet.credits_balance = 0
        self.wallet.save(update_fields=["current_plan", "plan_expires_at", "credits_balance"])
        grant_credits(self.wallet, 30, source="purchased", description="Topic tutor test balance")
        self.wallet.refresh_from_db()
        self.client.force_login(self.user)
        self.url = reverse("prep:api_topic_tutor", kwargs={"topic_id": self.topic.pk})

    def test_topic_page_includes_assistant_tab_and_upload_billing_disclosure(self):
        response = self.client.get(reverse("prep:topic_study", kwargs={"topic_id": self.topic.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ask a Topic Tutor")
        self.assertContains(response, 'id="pillar-assistant"', html=False)
        self.assertContains(response, "up to 3 PNG/JPEG images")
        self.assertContains(response, "OCR is at least 5 credits")

    def test_another_users_session_cannot_be_loaded(self):
        session = PrepTopicChatSession.objects.create(
            user=self.other_user,
            topic=self.topic,
            title="Private conversation",
        )

        response = self.client.get(self.url, {"session_id": session.pk})

        self.assertEqual(response.status_code, 404)
        self.assertFalse(response.json()["success"])

    @patch("services.prep_course_billing.ensure_note_access", return_value=(True, 30))
    @patch.object(prep_topic_tutor, "_topic_context", return_value=("Approved notes", ""))
    @patch.object(prep_topic_tutor, "_build_prompt", return_value=("system", "user"))
    @patch(
        "services.prep_ai_router.route_math_request",
        return_value={
            "success": True,
            "content": '{"decision":"answer","answer":"An unbiased estimator gets the answer right on average."}',
            "usage": {"prompt_tokens": 100, "completion_tokens": 30, "total_tokens": 130},
            "model_used": "test-model",
        },
    )
    def test_post_creates_private_conversation_and_bills_reply(
        self, route_math, build_prompt, topic_context, note_access
    ):
        response = self.client.post(self.url, {"message": "Explain unbiasedness simply"})

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["credits_charged"], 1)
        self.assertEqual(data["credits_balance"], 29)
        session = PrepTopicChatSession.objects.get(pk=data["session_id"], user=self.user)
        self.assertEqual(session.messages.count(), 2)
        self.assertEqual(
            list(session.messages.values_list("role", flat=True)),
            ["user", "assistant"],
        )
        transaction = PrepTransaction.objects.get(wallet=self.wallet, action_type="topic_tutor")
        self.assertEqual(transaction.amount, -1)

    @patch("services.prep_course_billing.ensure_note_access", return_value=(True, 30))
    @patch.object(prep_topic_tutor, "_topic_context", return_value=("Approved notes", ""))
    @patch.object(
        prep_topic_tutor,
        "_finish_uploads",
        return_value=(
            [{
                "name": "estimators.png",
                "text": "An unbiased estimator has expected value equal to the true parameter.",
                "page_count": 1,
                "source_type": "image_ocr",
            }],
            {"prompt_tokens": 1100, "completion_tokens": 100, "total_tokens": 1200},
            "test-ocr",
        ),
    )
    @patch.object(prep_topic_tutor, "_build_prompt", return_value=("system", "user"))
    @patch(
        "services.prep_ai_router.route_math_request",
        return_value={
            "success": True,
            "content": '{"decision":"answer","answer":"It is right on average across repeated samples."}',
            "usage": {"prompt_tokens": 100, "completion_tokens": 30, "total_tokens": 130},
            "model_used": "test-model",
        },
    )
    def test_image_ocr_and_reply_are_both_billed_and_upload_is_attached_to_turn(
        self, route_math, build_prompt, finish_uploads, topic_context, note_access
    ):
        image = SimpleUploadedFile(
            "estimators.png",
            b"\x89PNG\r\n\x1a\n" + b"small image",
            content_type="image/png",
        )

        response = self.client.post(
            self.url,
            {"message": "Explain the text in this image", "files": [image]},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["credits_charged"], 6)
        self.assertEqual(response.json()["credits_balance"], 24)
        self.assertEqual(
            PrepTransaction.objects.filter(wallet=self.wallet, action_type="topic_tutor_ocr").count(),
            1,
        )
        self.assertEqual(
            PrepTransaction.objects.filter(wallet=self.wallet, action_type="topic_tutor").count(),
            1,
        )
        upload = PrepTopicChatUpload.objects.get(session__user=self.user)
        self.assertEqual(upload.original_name, "estimators.png")
        self.assertEqual(upload.source_type, "image_ocr")
        self.assertEqual(upload.message.role, "user")
        self.assertEqual(PrepTopicChatMessage.objects.filter(session=upload.session).count(), 2)
