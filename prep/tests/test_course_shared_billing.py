from datetime import timedelta
from types import SimpleNamespace
from unittest.mock import Mock, patch

from django.core.management import call_command
from django.test import SimpleTestCase, TestCase, override_settings
from django.utils import timezone

from accounts.models import User
from prep.models import (
    PrepCourse,
    PrepCourseCostShare,
    PrepCourseEnrollment,
    PrepCourseSharedCost,
    PrepNotePrecomputeJob,
    PrepTopic,
    PrepTopicNotesJob,
    PrepTransaction,
    PrepWallet,
)
from services.credit_service import get_available_credits, grant_credits
from services.prep_course_billing import create_shared_course_cost, ensure_note_access, settle_course_cost_share
from services.prep_note_precompute import (
    enqueue_course_level_two_precompute,
    enqueue_topic_note_job,
    process_course_notes_in_background,
    process_single_topic_notes_job,
)


class NoteWorkerQueueStatusTests(SimpleTestCase):
    @override_settings(PREP_AUTOMATIC_NOTE_PREPARATION=False)
    def test_worker_does_not_claim_note_jobs_when_automatic_preparation_is_disabled(self):
        from prep.management.commands.run_prep_note_worker import Command

        command = Command()
        with (
            patch.object(command, "_expire_due_credits"),
            patch.object(command, "_recover_stale_documents"),
            patch.object(command, "_claim_topic_notes_job") as claim_topic_job,
            patch.object(command, "_claim_job") as claim_course_job,
        ):
            command.handle(once=True, poll_seconds=1.0, max_notes=0)

        claim_topic_job.assert_not_called()
        claim_course_job.assert_not_called()

    def test_course_precompute_stays_pending_while_topic_notes_are_pending(self):
        from prep.management.commands.run_prep_note_worker import Command

        child_jobs = Mock()
        pending_jobs = Mock()
        pending_jobs.exists.return_value = True
        child_jobs.filter.side_effect = [pending_jobs]
        job = SimpleNamespace(
            course=SimpleNamespace(code="ECO 101"),
            status="running",
            completed_at=timezone.now(),
            started_at=timezone.now(),
            last_error="old error",
        )

        with (
            patch("services.prep_note_precompute.enqueue_course_topic_note_jobs", return_value=3),
            patch("prep.models.PrepTopicNotesJob.objects.filter", return_value=child_jobs),
            patch.object(Command, "_save_job_resilient") as save_job,
        ):
            Command()._process_job(job)

        self.assertEqual(job.status, "pending")
        self.assertIsNone(job.started_at)
        self.assertIsNone(job.completed_at)
        self.assertEqual(job.last_error, "")
        self.assertEqual(
            save_job.call_args.kwargs["update_fields"],
            ["status", "started_at", "completed_at", "last_error"],
        )


class CourseSharedBillingTests(TestCase):
    def setUp(self):
        self.course = PrepCourse.objects.create(
            code="ECO 101",
            title="Economics",
            slug="eco-101-shared-billing",
        )
        self.first_user = User.objects.create_user(
            username="first-learner",
            email="first-learner@example.test",
            password="Valid123",
        )
        self.second_user = User.objects.create_user(
            username="second-learner",
            email="second-learner@example.test",
            password="Valid123",
        )

    def _fund(self, user, credits):
        wallet = PrepWallet.get_or_create_wallet(user)
        wallet.credit_grants.update(remaining_credits=0)
        wallet.current_plan = "plus"
        wallet.plan_expires_at = timezone.now() + timedelta(days=30)
        wallet.credits_balance = 0
        wallet.save(update_fields=["current_plan", "plan_expires_at", "credits_balance"])
        grant_credits(wallet, credits, source="purchased", description="Test top-up")
        return wallet

    def test_request_queues_current_signature_even_when_old_job_is_complete(self):
        topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Demand",
            slug="demand",
        )
        old_job = PrepTopicNotesJob.objects.create(
            topic=topic,
            level="level_2",
            source_signature="old-signature",
            status="complete",
        )

        current_job = enqueue_topic_note_job(topic, "level_2", "current-signature")

        self.assertEqual(current_job.status, "pending")
        self.assertNotEqual(current_job.pk, old_job.pk)
        old_job.refresh_from_db()
        self.assertEqual(old_job.status, "complete")

    @patch("services.prep_note_precompute._has_current_topic_note_cache", return_value=False)
    def test_request_requeues_completed_current_job_without_publishable_cache(self, _has_cache):
        topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Supply",
            slug="supply",
        )
        job = PrepTopicNotesJob.objects.create(
            topic=topic,
            level="level_2",
            source_signature="current-signature",
            status="complete",
            attempts=2,
            last_error="stale result",
        )

        queued = enqueue_topic_note_job(topic, "level_2", "current-signature")

        self.assertEqual(queued.pk, job.pk)
        self.assertEqual(queued.status, "pending")
        self.assertEqual(queued.attempts, 0)
        self.assertEqual(queued.last_error, "")

    def test_full_cost_is_charged_once_to_each_catalog_member(self):
        PrepCourseEnrollment.objects.create(user=self.first_user, course=self.course)
        PrepCourseEnrollment.objects.create(user=self.second_user, course=self.course)
        first_wallet = self._fund(self.first_user, 20)
        second_wallet = self._fund(self.second_user, 20)
        before = [get_available_credits(first_wallet), get_available_credits(second_wallet)]

        cost = create_shared_course_cost(
            course=self.course,
            cost_type="upload",
            total_credits=10,
            source_key="test-upload-cost",
        )

        shares = list(cost.shares.order_by("user_id"))
        self.assertEqual([share.required_credits for share in shares], [10, 10])
        self.assertTrue(all(settle_course_cost_share(share) for share in shares))
        first_wallet.refresh_from_db()
        second_wallet.refresh_from_db()
        self.assertEqual(
            [get_available_credits(first_wallet), get_available_credits(second_wallet)],
            [before[0] - 10, before[1] - 10],
        )
        self.assertTrue(all(share.is_settled for share in cost.shares.all()))
        self.assertEqual(PrepCourseCostShare.objects.filter(cost=cost).count(), 2)

    def test_late_catalog_member_inherits_full_saved_cost(self):
        PrepCourseEnrollment.objects.create(user=self.first_user, course=self.course)
        second_wallet = self._fund(self.second_user, 10)
        cost = create_shared_course_cost(
            course=self.course,
            cost_type="topic_notes",
            total_credits=7,
            source_key="test-level-two-cost",
            level="level_2",
        )

        PrepCourseEnrollment.objects.create(user=self.second_user, course=self.course)

        share = PrepCourseCostShare.objects.get(cost=cost, user=self.second_user)
        self.assertEqual(share.required_credits, 7)
        self.assertEqual(share.paid_credits, 7)
        self.assertEqual(cost.per_student_credits, 7)
        second_wallet.refresh_from_db()
        self.assertEqual(get_available_credits(second_wallet), 3)

    def test_trial_skips_upload_and_level_two_debits(self):
        PrepCourseEnrollment.objects.create(user=self.first_user, course=self.course)
        wallet = PrepWallet.get_or_create_wallet(self.first_user)
        balance = get_available_credits(wallet)
        cost = create_shared_course_cost(
            course=self.course,
            cost_type="topic_notes",
            total_credits=8,
            source_key="trial-level-two-cost",
            topic=PrepTopic.objects.create(
                course=self.course,
                order=1,
                title="Demand",
                slug="demand-shared-billing",
            ),
            level="level_2",
        )

        self.assertTrue(settle_course_cost_share(cost.shares.get(user=self.first_user)))
        wallet.refresh_from_db()
        self.assertEqual(get_available_credits(wallet), balance)
        self.assertEqual(cost.shares.get(user=self.first_user).paid_credits, 0)

    def test_trial_still_pays_level_one_and_level_three_notes(self):
        PrepCourseEnrollment.objects.create(user=self.first_user, course=self.course)
        wallet = PrepWallet.get_or_create_wallet(self.first_user)
        topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Demand",
            slug="demand-trial-levels",
        )
        upload = create_shared_course_cost(
            course=self.course,
            cost_type="upload",
            total_credits=4,
            source_key="trial-upload-exempt",
        )
        level_two = create_shared_course_cost(
            course=self.course,
            cost_type="topic_notes",
            total_credits=8,
            source_key="trial-level-two-exempt",
            topic=topic,
            level="level_2",
        )
        level_one = create_shared_course_cost(
            course=self.course,
            cost_type="topic_notes",
            total_credits=3,
            source_key="trial-level-one-billed",
            topic=topic,
            level="level_1",
        )
        level_three = create_shared_course_cost(
            course=self.course,
            cost_type="topic_notes",
            total_credits=2,
            source_key="trial-level-three-billed",
            topic=topic,
            level="level_3",
        )

        starting_balance = get_available_credits(wallet)
        self.assertTrue(settle_course_cost_share(upload.shares.get(user=self.first_user)))
        self.assertTrue(settle_course_cost_share(level_two.shares.get(user=self.first_user)))
        self.assertTrue(settle_course_cost_share(level_one.shares.get(user=self.first_user)))
        self.assertTrue(settle_course_cost_share(level_three.shares.get(user=self.first_user)))

        wallet.refresh_from_db()
        self.assertEqual(get_available_credits(wallet), starting_balance - 5)
        self.assertEqual(upload.shares.get(user=self.first_user).paid_credits, 0)
        self.assertEqual(level_two.shares.get(user=self.first_user).paid_credits, 0)
        self.assertEqual(level_one.shares.get(user=self.first_user).paid_credits, 3)
        self.assertEqual(level_three.shares.get(user=self.first_user).paid_credits, 2)

    def test_top_up_unlocks_level_two_topics_in_course_order(self):
        PrepCourseEnrollment.objects.create(user=self.first_user, course=self.course)
        wallet = self._fund(self.first_user, 8)
        topics = [
            PrepTopic.objects.create(
                course=self.course,
                order=order,
                title=f"Topic {order}",
                slug=f"topic-{order}-shared-billing",
            )
            for order in range(1, 3)
        ]
        create_shared_course_cost(
            course=self.course,
            cost_type="upload",
            total_credits=2,
            source_key="ordered-upload-cost",
        )
        for topic in topics:
            create_shared_course_cost(
                course=self.course,
                cost_type="topic_notes",
                total_credits=4,
                source_key=f"ordered-notes-{topic.pk}",
                topic=topic,
                level="level_2",
            )

        allowed, balance = ensure_note_access(self.first_user, topics[1], "level_2")
        self.assertFalse(allowed)
        self.assertEqual(balance, 2)
        self.assertTrue(ensure_note_access(self.first_user, topics[0], "level_2")[0])

        grant_credits(wallet, 2, source="purchased", description="Unlock next topic")
        self.assertTrue(ensure_note_access(self.first_user, topics[1], "level_2")[0])

    @patch("services.prep_note_precompute._has_current_topic_note_cache", return_value=True)
    @patch("services.prep_ai_router._note_completion_issues", return_value=[])
    @patch("services.prep_ai_router.get_or_generate_topic_notes")
    def test_worker_fans_out_all_levels_and_records_level_two_bundle_cost(
        self,
        generate_notes,
        validate_notes,
        note_cache_exists,
    ):
        PrepCourseEnrollment.objects.create(user=self.first_user, course=self.course)
        topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Demand",
            slug="demand-worker-test",
        )
        job = PrepNotePrecomputeJob.objects.create(course=self.course)
        generate_notes.return_value = {
            "notes": "Validated, self-contained Level 2 notes.",
            "cached": False,
            "review_status": "passed",
            "usage": {"prompt_tokens": 1400, "completion_tokens": 1100, "total_tokens": 2500},
            "model": "test-notes-model",
        }

        call_command("run_prep_note_worker", "--once")

        job.refresh_from_db()
        cost = PrepCourseSharedCost.objects.get(topic=topic, level="level_2")
        self.assertEqual(job.status, "complete")
        self.assertEqual(
            [call.kwargs["level"] for call in generate_notes.call_args_list],
            ["level_2", "level_1", "level_3"],
        )
        self.assertEqual(cost.total_credits, 3)
        self.assertEqual(cost.shares.get(user=self.first_user).required_credits, 3)
        self.assertEqual(
            set(topic.notes_generation_jobs.values_list("level", flat=True)),
            {"level_1", "level_2", "level_3"},
        )
        level_two_job = topic.notes_generation_jobs.get(level="level_2")
        self.assertEqual(level_two_job.provider_usage["total_tokens"], 2500)
        self.assertEqual(level_two_job.model_name, "test-notes-model")

    @patch("services.prep_note_precompute._has_current_topic_note_cache", return_value=True)
    @patch("services.prep_ai_router._note_completion_issues", return_value=[])
    @patch("services.prep_ai_router.get_or_generate_topic_notes")
    @patch("services.prep_ai_router._topic_notes_cache_signature", return_value="b" * 64)
    def test_worker_generates_level_one_only_after_level_two_is_complete(
        self,
        note_signature,
        generate_notes,
        validate_notes,
        note_cache_exists,
    ):
        PrepCourseEnrollment.objects.create(user=self.first_user, course=self.course)
        topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Elasticity",
            slug="elasticity-async-notes",
        )
        level_two_job = PrepTopicNotesJob.objects.create(
            topic=topic,
            level="level_2",
            source_signature="b" * 64,
            status="complete",
        )
        job = PrepTopicNotesJob.objects.create(
            topic=topic,
            level="level_1",
            source_signature="b" * 64,
        )
        generate_notes.return_value = {
            "notes": "Validated, simple Level 1 notes.",
            "cached": False,
            "review_status": "passed",
            "usage": {"prompt_tokens": 900, "completion_tokens": 600, "total_tokens": 1500},
            "model": "test-notes-model",
        }

        call_command("run_prep_note_worker", "--once")

        job.refresh_from_db()
        self.assertEqual(job.status, "complete")
        self.assertEqual(generate_notes.call_args.kwargs["level"], "level_1")
        self.assertFalse(PrepCourseSharedCost.objects.filter(topic=topic, level="level_1").exists())

    @patch("services.prep_note_precompute._has_current_topic_note_cache", return_value=False)
    @patch("services.prep_ai_router._note_completion_issues", return_value=[])
    @patch("services.prep_ai_router.get_or_generate_topic_notes")
    @patch("services.prep_ai_router._topic_notes_cache_signature", return_value="d" * 64)
    def test_worker_does_not_complete_without_persisted_current_note_cache(
        self,
        note_signature,
        generate_notes,
        validate_notes,
        note_cache_exists,
    ):
        topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Elasticity",
            slug="elasticity-no-note-cache",
        )
        job = PrepTopicNotesJob.objects.create(
            topic=topic,
            level="level_2",
            source_signature="d" * 64,
        )
        generate_notes.return_value = {
            "notes": "Structurally valid but not persisted notes.",
            "cached": False,
            "review_status": "passed",
            "usage": {"total_tokens": 100},
            "model": "test-notes-model",
        }

        call_command("run_prep_note_worker", "--once")

        job.refresh_from_db()
        self.assertEqual(job.status, "failed")
        self.assertIn("validated cache entry", job.last_error)

    @patch("services.prep_note_precompute.enqueue_course_topic_note_jobs")
    @patch("services.prep_ai_router.get_or_generate_topic_notes")
    @patch("services.prep_ai_router._topic_notes_cache_signature", return_value="b" * 64)
    def test_stale_note_job_is_superseded_without_generation(
        self,
        note_signature,
        generate_notes,
        enqueue_current_jobs,
    ):
        topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Demand",
            slug="demand-stale-note-test",
        )
        job = PrepTopicNotesJob.objects.create(
            topic=topic,
            level="level_2",
            source_signature="a" * 64,
            status="running",
        )

        completed = process_single_topic_notes_job(job)

        job.refresh_from_db()
        self.assertFalse(completed)
        self.assertEqual(job.status, "failed")
        self.assertIn("Superseded", job.last_error)
        generate_notes.assert_not_called()
        enqueue_current_jobs.assert_called_once_with(topic.course)

    @patch("services.prep_note_precompute.enqueue_course_topic_note_jobs")
    @patch("services.prep_ai_router.get_or_generate_topic_notes")
    @patch("services.prep_ai_router._topic_notes_cache_signature", side_effect=["a" * 64, "b" * 64])
    def test_topic_change_during_generation_supersedes_result(
        self,
        note_signature,
        generate_notes,
        enqueue_current_jobs,
    ):
        topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Demand",
            slug="demand-change-during-notes-test",
        )
        job = PrepTopicNotesJob.objects.create(
            topic=topic,
            level="level_2",
            source_signature="a" * 64,
            status="running",
        )
        generate_notes.return_value = {
            "notes": "Generated note content.",
            "cached": False,
            "review_status": "passed",
        }

        completed = process_single_topic_notes_job(job)

        job.refresh_from_db()
        self.assertFalse(completed)
        self.assertEqual(job.status, "failed")
        self.assertIn("Superseded", job.last_error)
        generate_notes.assert_called_once()
        enqueue_current_jobs.assert_called_once_with(topic.course)

    @patch("services.prep_ai_router._note_completion_issues", return_value=[])
    @patch("services.prep_ai_router.get_or_generate_topic_notes")
    @patch("services.prep_ai_router._topic_notes_cache_signature", return_value="c" * 64)
    def test_worker_does_not_mark_unreviewed_notes_complete(self, note_signature, generate_notes, validate_notes):
        topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Supply",
            slug="supply-review-gate",
        )
        job = PrepTopicNotesJob.objects.create(
            topic=topic,
            level="level_2",
            source_signature="c" * 64,
        )
        generate_notes.return_value = {
            "notes": "Structurally valid but not source-reviewed notes.",
            "cached": False,
            "review_status": "skipped_no_source",
            "usage": {"total_tokens": 100},
            "model": "test-notes-model",
        }

        call_command("run_prep_note_worker", "--once")

        job.refresh_from_db()
        self.assertEqual(job.status, "failed")
        self.assertIn("without a successful independent review", job.last_error)
        self.assertFalse(PrepCourseSharedCost.objects.filter(topic=topic).exists())

    def test_completed_course_job_is_requeued_once_for_new_publication(self):
        job = PrepNotePrecomputeJob.objects.create(
            course=self.course,
            status="complete",
            attempts=1,
            last_error="old failure",
            completed_at=timezone.now(),
        )

        requeued_job, queued = enqueue_course_level_two_precompute(self.course)
        duplicate_job, queued_again = enqueue_course_level_two_precompute(self.course)

        requeued_job.refresh_from_db()
        self.assertTrue(queued)
        self.assertFalse(queued_again)
        self.assertEqual(requeued_job.pk, job.pk)
        self.assertEqual(duplicate_job.pk, job.pk)
        self.assertEqual(requeued_job.status, "pending")
        self.assertEqual(requeued_job.attempts, 0)

    def test_course_precompute_stays_open_when_topic_job_failed(self):
        topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Demand",
            slug="demand-failed-precompute",
        )
        precompute_job = PrepNotePrecomputeJob.objects.create(
            course=self.course,
            status="pending",
        )
        PrepTopicNotesJob.objects.create(
            topic=topic,
            level="level_2",
            source_signature="e" * 64,
            status="failed",
        )

        process_course_notes_in_background(self.course.pk)

        precompute_job.refresh_from_db()
        self.assertEqual(precompute_job.status, "pending")

    def test_reconcile_existing_note_cost_preserves_payer_and_charges_catalog_members(self):
        PrepCourseEnrollment.objects.create(user=self.first_user, course=self.course)
        PrepCourseEnrollment.objects.create(user=self.second_user, course=self.course)
        first_wallet = self._fund(self.first_user, 20)
        second_wallet = self._fund(self.second_user, 20)
        topic = PrepTopic.objects.create(
            course=self.course,
            order=1,
            title="Demand",
            slug="demand-reconcile-test",
        )
        PrepTransaction.objects.create(
            wallet=first_wallet,
            amount=-5,
            action_type="topic_notes",
            description=f"AI Topic Notes (level_2): {self.course.code} - {topic.title}",
            model_name="test-model",
            total_tokens=5000,
        )
        PrepTransaction.objects.create(
            wallet=first_wallet,
            amount=-7,
            action_type="topic_notes",
            description=f"AI Topic Notes (level_2): {self.course.code} - {topic.title}",
            model_name="newer-test-model",
            total_tokens=7000,
        )
        second_before = get_available_credits(second_wallet)

        call_command("reconcile_prep_course_costs", course=self.course.code)
        call_command("reconcile_prep_course_costs", course=self.course.code)

        cost = PrepCourseSharedCost.objects.get(course=self.course, topic=topic)
        self.assertEqual(PrepCourseSharedCost.objects.filter(course=self.course, topic=topic).count(), 1)
        self.assertEqual(cost.total_credits, 7)
        self.assertEqual(cost.shares.get(user=self.first_user).paid_credits, 7)
        self.assertEqual(cost.shares.get(user=self.second_user).paid_credits, 7)
        second_wallet.refresh_from_db()
        self.assertEqual(get_available_credits(second_wallet), second_before - 7)
