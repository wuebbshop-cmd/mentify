"""Shared course upload and topic-note credit accounting."""
from django.db import transaction
from django.utils import timezone


def _share_amount(total_credits: int, member_count: int) -> int:
    del member_count
    return max(0, int(total_credits))


def create_shared_course_cost(
    *,
    course,
    cost_type: str,
    total_credits: int,
    source_key: str,
    document=None,
    topic=None,
    level: str = "",
    usage=None,
    model_name: str = "",
    source_transaction=None,
):
    """Record a provider/upload cost once; each catalog member owes its full cost."""
    from prep.models import PrepCourseCostShare, PrepCourseEnrollment, PrepCourseSharedCost

    total_credits = max(0, int(total_credits))
    with transaction.atomic():
        member_ids = list(
            PrepCourseEnrollment.objects.filter(course=course, user__role="learner")
            .order_by("user_id")
            .values_list("user_id", flat=True)
        )
        cost, created = PrepCourseSharedCost.objects.get_or_create(
            source_key=source_key,
            defaults={
                "course": course,
                "cost_type": cost_type,
                "document": document,
                "topic": topic,
                "level": level,
                "source_transaction": source_transaction,
                "total_credits": total_credits,
                "per_student_credits": _share_amount(total_credits, len(member_ids)),
                "member_count_at_creation": len(member_ids),
                "usage": usage or {},
                "model_name": model_name,
            },
        )
        if created:
            PrepCourseCostShare.objects.bulk_create([
                PrepCourseCostShare(
                    cost=cost,
                    user_id=user_id,
                    required_credits=cost.per_student_credits,
                )
                for user_id in member_ids
            ])
        return cost


def add_course_member_shares(user, course) -> None:
    """Give a newly enrolled user the full saved course cost for existing events."""
    from prep.models import PrepCourseCostShare, PrepCourseSharedCost

    if getattr(user, "role", "") != "learner":
        return

    costs = PrepCourseSharedCost.objects.filter(course=course).only("id", "per_student_credits")
    PrepCourseCostShare.objects.bulk_create(
        [
            PrepCourseCostShare(cost_id=cost.id, user=user, required_credits=cost.per_student_credits)
            for cost in costs
        ],
        ignore_conflicts=True,
    )
    settle_existing_course_costs(user, course)


def settle_existing_course_costs(user, course) -> None:
    """Settle existing course costs in upload, Level 2 syllabus, then other-level order."""
    from prep.models import PrepCourseCostShare, PrepTopic

    shares = list(
        PrepCourseCostShare.objects.filter(user=user, cost__course=course)
        .select_related("cost", "cost__topic")
    )
    topic_order = dict(PrepTopic.objects.filter(course=course).values_list("id", "order"))

    def order_key(share):
        cost = share.cost
        if cost.cost_type == "upload":
            return (0, 0, 0, cost.created_at, cost.id)
        if cost.level == "level_2":
            return (1, topic_order.get(cost.topic_id, 0), 0, cost.created_at, cost.id)
        level_order = {"level_1": 1, "level_3": 2}.get(cost.level, 3)
        return (2, topic_order.get(cost.topic_id, 0), level_order, cost.created_at, cost.id)

    for share in sorted(shares, key=order_key):
        if not settle_course_cost_share(share):
            break


def is_trial_exempt_for_course_cost(wallet, cost_type: str, level: str = "") -> bool:
    return (
        cost_type in {"upload", "topic_notes"}
        and (cost_type != "topic_notes" or level == "level_2")
        and wallet.current_plan == "trial"
        and wallet.plan_expires_at is not None
        and wallet.plan_expires_at > timezone.now()
    )


def settle_course_cost_share(share) -> bool:
    """Charge one complete share if allowed and affordable; never partially charge a topic."""
    from prep.models import PrepCourseCostShare, PrepWallet
    from services.credit_service import InsufficientCredits, consume_credits, get_available_credits

    with transaction.atomic():
        locked = (
            PrepCourseCostShare.objects.select_for_update()
            .select_related("cost", "user")
            .get(pk=share.pk)
        )
        if locked.paid_credits >= locked.required_credits:
            return True

        wallet = PrepWallet.get_or_create_wallet(locked.user)
        if is_trial_exempt_for_course_cost(wallet, locked.cost.cost_type, locked.cost.level):
            return True

        remaining = locked.required_credits - locked.paid_credits
        if get_available_credits(wallet) < remaining:
            return False

        try:
            consume_credits(
                wallet,
                remaining,
                action_type=(
                    "topic_notes"
                    if locked.cost.cost_type == "topic_notes"
                    else "upload_ocr"
                    if locked.cost.model_name == "together_vision_ocr"
                    else "upload_text"
                ),
                description=(
                    f"Shared course cost ({locked.cost.cost_type}): {locked.cost.course.code}"
                    + (f" - {locked.cost.topic.title} ({locked.cost.level})" if locked.cost.topic_id else "")
                ),
                usage=locked.cost.usage,
                model_name=locked.cost.model_name,
                metadata={
                    "shared_course_cost_id": locked.cost_id,
                    "course_id": locked.cost.course_id,
                    "topic_id": locked.cost.topic_id,
                    "level": locked.cost.level,
                },
            )
        except InsufficientCredits:
            return False

        locked.paid_credits = locked.required_credits
        locked.settled_at = timezone.now()
        locked.save(update_fields=["paid_credits", "settled_at"])
        return True


def ensure_note_access(user, topic, level: str) -> tuple[bool, int]:
    """Settle ordered course shares; Level 2 advances topic-by-topic after top-ups."""
    from prep.models import PrepCourseCostShare, PrepCourseEnrollment, PrepTopic
    from services.credit_service import get_available_credits

    if not PrepCourseEnrollment.objects.filter(user=user, course=topic.course).exists():
        if getattr(user, "role", "") != "learner":
            return True, 0
        return False, 0

    upload_shares = PrepCourseCostShare.objects.filter(
        user=user,
        cost__course=topic.course,
        cost__cost_type="upload",
    ).select_related("cost").order_by("cost__created_at", "cost_id")
    for share in upload_shares:
        if not settle_course_cost_share(share):
            return False, get_available_credits(share.user.prep_wallet)

    if level == "level_2":
        ordered_topics = PrepTopic.objects.filter(
            course=topic.course,
            is_active=True,
            order__lte=topic.order,
        ).order_by("order", "id")
        for ordered_topic in ordered_topics:
            shares = PrepCourseCostShare.objects.filter(
                user=user,
                cost__topic=ordered_topic,
                cost__cost_type="topic_notes",
                cost__level="level_2",
            ).select_related("cost").order_by("cost__created_at", "cost_id")
            for share in shares:
                if not settle_course_cost_share(share):
                    return False, get_available_credits(share.user.prep_wallet)
        return True, get_available_credits(user.prep_wallet)

    shares = PrepCourseCostShare.objects.filter(
        user=user,
        cost__topic=topic,
        cost__cost_type="topic_notes",
        cost__level="level_2",
    ).select_related("cost").order_by("cost__created_at", "cost_id")
    for share in shares:
        if not settle_course_cost_share(share):
            return False, get_available_credits(share.user.prep_wallet)
    return True, get_available_credits(user.prep_wallet)