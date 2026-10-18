import logging
from datetime import datetime, timedelta, timezone as dt_timezone
from django.utils import timezone

try:
    from fsrs import Card, Rating, Scheduler, State
    HAS_FSRS = True
except ImportError:
    HAS_FSRS = False
    Card = None
    Rating = None
    Scheduler = None
    State = None

logger = logging.getLogger(__name__)

# Map integer / string ratings to fsrs.Rating enum or fallback values
if HAS_FSRS:
    RATING_MAP = {
        "again": Rating.Again,
        "1": Rating.Again,
        1: Rating.Again,
        "hard": Rating.Hard,
        "2": Rating.Hard,
        2: Rating.Hard,
        "good": Rating.Good,
        "3": Rating.Good,
        3: Rating.Good,
        "easy": Rating.Easy,
        "4": Rating.Easy,
        4: Rating.Easy,
    }
else:
    RATING_MAP = {
        "again": 1,
        "1": 1,
        1: 1,
        "hard": 2,
        "2": 2,
        2: 2,
        "good": 3,
        "3": 3,
        3: 3,
        "easy": 4,
        "4": 4,
        4: 4,
    }



def get_due_spaced_cards(user, topic=None, limit: int = 10):
    """
    Returns spaced repetition topic cards due for review today for the student.
    Can be filtered by topic, or across all enrolled courses.
    """
    from prep.models import PrepStudentSpacedCard
    now = timezone.now()
    qs = (
        PrepStudentSpacedCard.objects.filter(user=user, due_date__lte=now, question__isnull=True)
        .select_related("topic", "topic__course")
    )
    if topic:
        qs = qs.filter(topic=topic)
    return list(qs.order_by("due_date")[:limit])


def get_or_create_spaced_card_for_topic(user, topic):
    """
    Creates or retrieves an FSRS spaced repetition tracking card for a syllabus topic.
    """
    from prep.models import PrepStudentSpacedCard
    card = PrepStudentSpacedCard.objects.filter(user=user, topic=topic, question__isnull=True).first()
    if not card:
        course_name = f"{topic.course.code} - {topic.course.title}" if topic.course else ""
        card = PrepStudentSpacedCard.objects.create(
            user=user,
            topic=topic,
            question=None,
            card_title=topic.title,
            prompt_text=f"Review core syllabus concepts, derivations, and problem sets for {topic.title} ({course_name}).",
            answer_text="",
            due_date=timezone.now(),
            state=0,  # State.New
        )
    return card


def toggle_spaced_card_for_topic(user, topic):
    """
    Toggles a topic in/out of the student's daily revision deck.
    If already enrolled, removes it. If not enrolled, creates it.
    Returns (card_or_none, is_enrolled)
    """
    from prep.models import PrepStudentSpacedCard
    existing = PrepStudentSpacedCard.objects.filter(user=user, topic=topic, question__isnull=True).first()
    if existing:
        existing.delete()
        return None, False
    card = get_or_create_spaced_card_for_topic(user, topic)
    return card, True


def review_spaced_card(card_id: int, user, user_rating: str):
    """
    Applies the FSRS memory calculation when a student rates their retention.
    Ratings: 'again' (fail), 'hard', 'good', 'easy'.
    Returns updated card data and next due date.
    """
    from prep.models import PrepStudentSpacedCard

    card_obj = PrepStudentSpacedCard.objects.filter(pk=card_id, user=user).first()
    if not card_obj:
        return None

    now = datetime.now(dt_timezone.utc)
    if HAS_FSRS and Card and Scheduler and State:
        rating_enum = RATING_MAP.get(str(user_rating).lower().strip(), Rating.Good)
        fsrs_card = Card()
        fsrs_card.due = card_obj.due_date
        fsrs_card.stability = card_obj.stability if (card_obj.stability and card_obj.stability > 0) else None
        fsrs_card.difficulty = card_obj.difficulty if (card_obj.difficulty and card_obj.difficulty > 0) else None
        if card_obj.state in {1, 2, 3}:
            fsrs_card.state = State(card_obj.state)
        else:
            fsrs_card.state = State.Learning
        fsrs_card.last_review = card_obj.last_review

        scheduler = Scheduler()
        updated_card, review_log = scheduler.review_card(fsrs_card, rating_enum, now)
        next_due = updated_card.due
        next_state = int(updated_card.state.value if hasattr(updated_card.state, "value") else updated_card.state)
        next_stability = updated_card.stability or 0.0
        next_difficulty = updated_card.difficulty or 0.0
        is_again = (rating_enum == Rating.Again)
    else:
        is_again = str(user_rating).lower().strip() in {"again", "1"}
        interval_days = 1 if is_again else 3
        next_due = now + timedelta(days=interval_days)
        next_state = 1
        next_stability = 1.0
        next_difficulty = 5.0

    # Persist updated state to database
    card_obj.due_date = next_due
    card_obj.stability = next_stability
    card_obj.difficulty = next_difficulty

    if card_obj.last_review:
        card_obj.elapsed_days = max(0, (now.date() - card_obj.last_review.date()).days)
    else:
        card_obj.elapsed_days = 0

    card_obj.scheduled_days = max(0, (next_due.date() - now.date()).days)
    card_obj.reps = (card_obj.reps or 0) + 1
    if is_again and card_obj.reps > 1:
        card_obj.lapses = (card_obj.lapses or 0) + 1

    card_obj.state = next_state
    card_obj.last_review = now
    card_obj.save()

    return {
        "id": card_obj.id,
        "due_date": card_obj.due_date.isoformat(),
        "scheduled_days": card_obj.scheduled_days,
        "reps": card_obj.reps,
        "state": card_obj.state,
    }
