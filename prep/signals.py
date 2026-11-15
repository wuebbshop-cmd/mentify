from django.contrib.auth import get_user_model
from django.contrib.auth.signals import user_logged_in
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import PrepContentCache, PrepCourseEnrollment, PrepNoteGenerationGuard, PrepTopic, PrepWallet


@receiver(post_save, sender=get_user_model())
def create_prep_trial_wallet(sender, instance, created, **kwargs):
    """Start the exactly 72-hour trial at account creation."""
    if created:
        PrepWallet.get_or_create_wallet(instance)


@receiver(user_logged_in)
def notify_standard_email_credit_allowance(sender, request, user, **kwargs):
    """Explain the reduced free allowance once after a standard-email sign-in."""
    from services.credit_service import notify_standard_account_credit_limit

    notify_standard_account_credit_limit(user)


@receiver(pre_save, sender=PrepTopic)
def detect_topic_source_change(sender, instance, **kwargs):
    """Mark only materially changed topic source data for note invalidation."""
    instance._invalidate_topic_notes = False
    if not instance.pk:
        return
    previous = sender.objects.filter(pk=instance.pk).values("title", "summary", "subtopics").first()
    if previous:
        instance._invalidate_topic_notes = any(
            previous[field] != getattr(instance, field)
            for field in ("title", "summary", "subtopics")
        )


@receiver(post_save, sender=PrepTopic)
def invalidate_notes_after_topic_source_change(sender, instance, created, **kwargs):
    """Safely handle topic source changes without permanently deleting content cache.
    
    Instead of hard-deleting expensive generated notes, we:
    1. Clear the generation guard so new/updated notes can be queued when requested.
    2. Invalidate old cached PDF artifacts so stale downloads are rebuilt.
    3. Clear in-memory/view-level Django caches for this topic.
    Content records in PrepContentCache are preserved for fallback, revalidation, and recovery.
    """
    if not created and getattr(instance, "_invalidate_topic_notes", False):
        PrepNoteGenerationGuard.objects.filter(topic=instance).delete()
        
        from django.core.cache import cache
        cache.delete(f"prep_pub_topic_notes_{instance.pk}")
        cache.delete(f"prep_pub_levels_{instance.pk}_True")
        cache.delete(f"prep_pub_levels_{instance.pk}_False")
        
        from services.prep_pdf_artifacts import invalidate_topic_note_pdfs
        invalidate_topic_note_pdfs(instance)


@receiver(post_save, sender=PrepCourseEnrollment)
def add_shared_cost_shares_for_new_course_member(sender, instance, created, **kwargs):
    if created and instance.user.role == "learner":
        from services.prep_course_billing import add_course_member_shares

        add_course_member_shares(instance.user, instance.course)
