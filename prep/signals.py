from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import PrepWallet


@receiver(post_save, sender=get_user_model())
def create_prep_trial_wallet(sender, instance, created, **kwargs):
    """Start the exactly 72-hour trial at account creation."""
    if created:
        PrepWallet.get_or_create_wallet(instance)

