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
    PrepCreditReservation,
    PrepTransaction,
    PrepWallet,
)
from services.credit_service import (
    InsufficientCredits,
    consume_credits,
    get_available_credits,
    grant_credits,
    release_credit_reservation,
    reserve_credits,
)
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
            course=SimpleNamespace(code="STA 210", title="Statistical Inference"),
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

        self.assertEqual(response, "I can only answer questions about this topic.")
        self.assertNotIn("secret implementation", response)

    def test_plain_text_model_response_is_validated_and_accepted(self):
        answer = (
            "Start with the definitions and key ideas in this topic. "
            "Then practise applying each idea to a short exam question."
        )

        self.assertEqual(prep_topic_tutor._parse_tutor_response(answer, self.topic), answer)

    def test_malformed_structured_model_response_is_not_treated_as_plain_text(self):
        with self.assertRaisesRegex(
            prep_topic_tutor.TopicTutorError,
            "unreadable response",
        ):
            prep_topic_tutor._parse_tutor_response(
                '{"decision":"answer","answer":"unfinished',
                self.topic,
            )

    def test_plain_text_fallback_still_rejects_links_and_html(self):
        for answer in (
            "<script>alert(1)</script>",
            "Read [this page](https://example.com) for more.",
        ):
            with self.subTest(answer=answer), self.assertRaises(prep_topic_tutor.TopicTutorError):
                prep_topic_tutor._parse_tutor_response(answer, self.topic)

    def test_prompt_requests_direct_answers_without_unprompted_source_mentions(self):
        with patch.object(prep_topic_tutor, "_output_format_rules", return_value="Use standard notation"):
            system_prompt, user_prompt = prep_topic_tutor._build_prompt(
                self.topic,
                "Internal topic notes",
                "Internal course source",
                [],
                "Explain estimator bias",
                [],
            )

        self.assertIn(
            "Give a direct answer without mentioning notes, uploaded materials, sources",
            user_prompt,
        )
        self.assertIn("without mentioning notes, source documents", system_prompt)
        self.assertNotIn("distinguish it from what the supplied notes say", user_prompt)

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

    def test_topic_page_includes_compact_tutor_composer_and_disclosure(self):
        response = self.client.get(reverse("prep:topic_study", kwargs={"topic_id": self.topic.pk}))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ask a Topic Tutor")
        self.assertContains(response, 'id="pillar-assistant"', html=False)
        self.assertContains(response, 'id="topic-tutor-attach"', html=False)
        self.assertContains(response, 'aria-label="Choose files to attach"', html=False)
        self.assertContains(response, 'id="topic-tutor-upload-menu"', html=False)
        self.assertContains(response, 'id="topic-tutor-choose-pdf"', html=False)
        self.assertContains(response, 'id="topic-tutor-choose-image"', html=False)
        self.assertContains(response, 'accept="application/pdf,.pdf"', html=False)
        self.assertContains(response, 'accept="image/png,image/jpeg,.png,.jpg,.jpeg"', html=False)
        self.assertContains(response, "topic-tutor-upload-remove")
        self.assertContains(response, 'id="topic-tutor-send"', html=False)
        self.assertContains(response, "topic-tutor-spinner")
        self.assertContains(response, "topic-tutor-pending-dot")
        self.assertContains(response, 'class="topic-tutor-composer-disclosure"', html=False)
        self.assertContains(response, "Up to 3 PNG/JPEG images")
        self.assertContains(response, "scanned PDF pages and images cost 5 credits each")
        self.assertContains(response, 'stroke="var(--danger)"', html=False)
        self.assertContains(response, 'id="topic-tutor-expand"', html=False)
        self.assertContains(response, "Expand tutor to full screen")
        self.assertContains(response, ".topic-tutor-shell.topic-tutor-expanded")
        self.assertContains(response, "body.topic-tutor-expanded .footer")
        self.assertContains(response, "display: none !important;", html=False)
        self.assertContains(response, "event.key === 'Escape'")
        self.assertContains(response, 'id="topic-tutor-history-toggle"', html=False)
        self.assertContains(response, 'id="topic-tutor-history-close"', html=False)
        self.assertContains(response, 'id="topic-tutor-history-backdrop"', html=False)
        self.assertContains(response, "display: none;\n      position: fixed;\n      z-index: 1201;", html=False)
        self.assertContains(
            response,
            ".topic-tutor-shell.topic-tutor-history-open .topic-tutor-history-backdrop",
        )
        self.assertContains(response, "topic-tutor-shell.topic-tutor-history-open .topic-tutor-history")
        self.assertContains(response, "transform: translateX(-105%)")
        self.assertContains(response, "window.matchMedia('(max-width: 800px)').matches")
        self.assertContains(response, "width: min(680px, 100%)")
        self.assertContains(response, "transform: translateX(-50%)")
        self.assertContains(response, "height: min(86vh, 960px)")
        self.assertContains(response, "padding: 40px clamp(24px, 5vw, 64px) 180px")
        self.assertContains(response, "setTopicTutorHistoryOpen(false)")
        self.assertContains(response, 'id="topic-tutor-error-dismiss"', html=False)
        self.assertContains(response, 'aria-label="Dismiss error message"', html=False)
        self.assertContains(response, "setTimeout(clearTopicTutorError, 10000)")
        self.assertContains(response, "position: fixed;\n      z-index: 1200;\n      inset: 0;", html=False)
        self.assertContains(response, "height: 100dvh;\n      min-height: 0;", html=False)
        page_script = response.content.decode()
        self.assertLess(
            page_script.index("formData.set('message', text);"),
            page_script.index("input.disabled = true;"),
        )
        self.assertIn("files.forEach(file => formData.append('files', file, file.name));", page_script)

    def test_reservations_prevent_other_spending_from_using_held_credits(self):
        reservation = reserve_credits(
            self.wallet,
            20,
            purpose="topic_tutor",
        )

        self.assertEqual(get_available_credits(self.wallet), 10)
        with self.assertRaises(InsufficientCredits):
            consume_credits(
                self.wallet,
                11,
                action_type="test_spend",
                description="Must not spend held tutor credits",
            )
        release_credit_reservation(reservation, reason="Test cleanup")
        self.assertEqual(get_available_credits(self.wallet), 30)

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
        self.assertEqual(transaction.metadata["provider"], "deepseek")
        reservation = PrepCreditReservation.objects.get(wallet=self.wallet)
        self.assertEqual(reservation.status, "settled")
        self.assertEqual(reservation.charged_credits, 1)
        self.assertEqual(reservation.remaining_reserved_credits, 0)

    @patch("services.prep_course_billing.ensure_note_access", return_value=(True, 30))
    @patch.object(prep_topic_tutor, "_topic_context", return_value=("Approved notes", ""))
    @patch.object(prep_topic_tutor, "_build_prompt", return_value=("system", "user"))
    @patch(
        "services.prep_ai_router.route_math_request",
        return_value={"success": False, "content": "", "usage": {}},
    )
    def test_failed_chat_without_usage_releases_the_full_reservation(
        self, route_math, build_prompt, topic_context, note_access
    ):
        response = self.client.post(self.url, {"message": "Explain unbiasedness simply"})

        self.assertEqual(response.status_code, 502)
        self.assertEqual(response.json()["credits_balance"], 30)
        reservation = PrepCreditReservation.objects.get(wallet=self.wallet)
        self.assertEqual(reservation.status, "released")
        self.assertEqual(reservation.charged_credits, 0)
        self.assertEqual(reservation.remaining_reserved_credits, 0)
        self.assertEqual(get_available_credits(self.wallet), 30)

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
            "deepseek-ai/DeepSeek-V4.1-Flash",
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
        ocr_transaction = PrepTransaction.objects.get(
            wallet=self.wallet,
            action_type="topic_tutor_ocr",
        )
        self.assertEqual(ocr_transaction.amount, -5)
        self.assertEqual(ocr_transaction.metadata["flat_credits_per_image_or_page"], 5)
        self.assertEqual(ocr_transaction.metadata["image_or_page_count"], 1)
        self.assertEqual(
            PrepTransaction.objects.filter(wallet=self.wallet, action_type="topic_tutor").count(),
            1,
        )
        upload = PrepTopicChatUpload.objects.get(session__user=self.user)
        self.assertEqual(upload.original_name, "estimators.png")
        self.assertEqual(upload.source_type, "image_ocr")
        self.assertEqual(upload.message.role, "user")
        self.assertEqual(PrepTopicChatMessage.objects.filter(session=upload.session).count(), 2)
