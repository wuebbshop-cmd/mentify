from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import PrepContentCache, PrepNoteGenerationGuard, PrepTopic, PrepWallet


@receiver(post_save, sender=get_user_model())
def create_prep_trial_wallet(sender, instance, created, **kwargs):
    """Start the exactly 72-hour trial at account creation."""
    if created:
        PrepWallet.get_or_create_wallet(instance)


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
    """Discard published notes only when this topic's approved source changes."""
    if not created and getattr(instance, "_invalidate_topic_notes", False):
        PrepContentCache.objects.filter(topic=instance, content_type="topic_notes").delete()
        PrepNoteGenerationGuard.objects.filter(topic=instance).delete()
