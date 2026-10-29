"""
Service for managing Mentify Prep topic note tiers and token/credit spending.

Tiers:
- Level 2 (Core Concepts / Detailed): 100% Free for all students (trial, freemium, paid).
- Level 1 (Foundation & Intuition / Concise): 2 credits flat charge.
- Level 3 (Exam Focus & Worked CAT Traps): 4 credits flat charge.

Deduction Rules:
- Pure token/credit spending deducted from wallet.
- Deducted ONLY and ONLY IF the note is present and successfully delivered from cache.
- If notes are absent or awaiting review, 0 credits are deducted.
- Once unlocked by a student, access persists so repeat visits do not charge again.
"""

import logging
from typing import Set, Tuple, Dict, Any

logger = logging.getLogger(__name__)

NOTE_LEVEL_CREDIT_COSTS: Dict[str, int] = {
    "level_1": 2,  # Foundation & Intuition (Concise notes)
    "level_2": 0,  # Core Concepts (Detailed notes) - Free
    "level_3": 4,  # Exam Focus (High-yield exam traps & CATs)
}

NOTE_LEVEL_LABELS: Dict[str, str] = {
    "level_1": "Foundation & Intuition",
    "level_2": "Core Concepts",
    "level_3": "Exam Focus",
}


def is_topic_note_unlocked(user, topic, level: str) -> bool:
    """
    Check if user has access to this topic note level.
    Level 2 is always free and unlocked.
    Level 1 and Level 3 require a 1-time unlock per student per topic.
    """
    if level == "level_2":
        return True
    if not user or not getattr(user, "is_authenticated", False):
        return False
    if getattr(user, "is_staff", False) or getattr(user, "is_superuser", False):
        return True
    from prep.models import PrepTransaction
    return PrepTransaction.objects.filter(
        wallet__user=user,
        action_type="topic_notes",
        metadata__topic_id=int(topic.id),
        metadata__level=level,
    ).exists()


def get_unlocked_topic_note_levels(user, topic) -> Set[str]:
    """
    Return the set of note levels unlocked by this student for this topic.
    Always includes 'level_2'.
    """
    unlocked = {"level_2"}
    if not user or not getattr(user, "is_authenticated", False):
        return unlocked
    if getattr(user, "is_staff", False) or getattr(user, "is_superuser", False):
        return {"level_1", "level_2", "level_3"}
    from prep.models import PrepTransaction
    unlocked_levels = PrepTransaction.objects.filter(
        wallet__user=user,
        action_type="topic_notes",
        metadata__topic_id=int(topic.id),
    ).values_list("metadata__level", flat=True)
    for lvl in unlocked_levels:
        if lvl and str(lvl) in NOTE_LEVEL_CREDIT_COSTS:
            unlocked.add(str(lvl))
    return unlocked


def unlock_topic_note_level(user, topic, level: str, note_content: str) -> Tuple[bool, int, str]:
    """
    Validate and unlock a topic note level for a student.

    Returns:
        (success: bool, credits_deducted: int, error_message: str)
    """
    if level == "level_2":
        return True, 0, ""

    cost = NOTE_LEVEL_CREDIT_COSTS.get(level, 0)
    label = NOTE_LEVEL_LABELS.get(level, level)

    # 1. Deduct ONLY IF note content is present in cache
    if not note_content or not note_content.strip():
        return (
            False,
            0,
            f"{label} notes are currently awaiting review or being prepared in the background. No credits were deducted."
        )

    # 2. Check if student already unlocked this level
    if is_topic_note_unlocked(user, topic, level):
        return True, 0, ""

    # 3. Check wallet balance
    if not user or not getattr(user, "is_authenticated", False):
        return False, 0, "Please sign in to unlock topic notes."

    from prep.models import PrepWallet
    from services.credit_service import consume_credits, get_available_credits, InsufficientCredits

    wallet = PrepWallet.get_or_create_wallet(user)
    available = get_available_credits(wallet)
    if available < cost:
        return (
            False,
            0,
            f"You need at least {cost} credits to unlock {label} notes. Your current balance is {available} credits."
        )

    # 4. Deduct flat credits and record transaction
    try:
        consume_credits(
            wallet=wallet,
            amount=cost,
            action_type="topic_notes",
            description=f"Unlocked {label} Notes ({cost} credits): {topic.course.code} - {topic.title}",
            metadata={
                "topic_id": int(topic.id),
                "level": level,
                "course_id": topic.course_id,
                "course_code": topic.course.code,
                "credits_charged": cost,
            },
        )
        wallet.refresh_from_db()
        logger.info(
            "User %s unlocked %s for topic %s (%s credits deducted). Remaining: %s",
            user.pk,
            level,
            topic.pk,
            cost,
            get_available_credits(wallet),
        )
        return True, cost, ""
    except InsufficientCredits:
        return (
            False,
            0,
            f"You need at least {cost} credits to unlock {label} notes. Your current balance is {available} credits."
        )
