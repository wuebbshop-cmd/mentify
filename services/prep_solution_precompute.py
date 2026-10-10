import logging
import time
from django.db import close_old_connections, transaction
from prep.models import PrepQuestion
from services.prep_ai_router import (
    clean_latex_document_markup,
    get_or_generate_question_solution,
    normalize_math_delimiters,
    validated_question_solution,
)

logger = logging.getLogger(__name__)


def precompute_solution_for_question(question: PrepQuestion) -> bool:
    """
    Precompute and verify a solution for a single assessment question.
    Operates outside any long-running transaction to avoid database locks.
    Returns True if a verified solution is now present.
    """
    if not question or question.verification_status not in PrepQuestion.ANSWERABLE_STATUSES:
        return False

    # Check if question already has a valid solution
    existing_sol = validated_question_solution(question)
    if existing_sol:
        return True

    course = getattr(question.topic, "course", None) if question.topic else None
    if course is None and question.paper_id:
        course = getattr(question.paper, "course", None)
    course_code = course.code if course else "Mathematics"
    topic_label = question.topic_label or (question.topic.title if question.topic else "")

    close_old_connections()
    try:
        res = get_or_generate_question_solution(
            question_latex=question.question_latex,
            course_code=course_code,
            topic_label=topic_label,
            question_obj=question,
        )
        if not res.get("solution"):
            logger.warning(
                "[Precompute Solutions] Could not generate solution for Q%s (id=%s): %s",
                question.number,
                question.id,
                res.get("error", "Unknown generation failure"),
            )
            return False

        clean_sol = normalize_math_delimiters(clean_latex_document_markup(res["solution"]))
        with transaction.atomic():
            question.solution_latex = clean_sol
            question.save(update_fields=["solution_latex"])

        logger.info(
            "[Precompute Solutions] Successfully precomputed verified solution for Q%s (id=%s)",
            question.number,
            question.id,
        )
        return True
    except Exception as exc:
        logger.exception(
            "[Precompute Solutions] Error precomputing solution for Q%s (id=%s): %s",
            question.number,
            question.id,
            exc,
        )
        return False
    finally:
        close_old_connections()


def precompute_solutions_for_questions(
    questions,
    sleep_seconds: float = 1.0,
    progress_callback=None,
) -> dict:
    """
    Sequentially precomputes and verifies solutions for a list of questions.
    Paces requests with sleep_seconds to prevent CPU/thread or API rate limit starvation.
    """
    total = len(questions)
    completed = 0
    already_valid = 0
    failed = 0

    for idx, q in enumerate(questions, start=1):
        if validated_question_solution(q):
            already_valid += 1
            if progress_callback:
                progress_callback(idx, total, q, "already_valid")
            continue

        success = precompute_solution_for_question(q)
        if success:
            completed += 1
            if progress_callback:
                progress_callback(idx, total, q, "completed")
        else:
            failed += 1
            if progress_callback:
                progress_callback(idx, total, q, "failed")

        if sleep_seconds > 0 and idx < total:
            time.sleep(sleep_seconds)

    return {
        "total": total,
        "completed": completed,
        "already_valid": already_valid,
        "failed": failed,
    }


def precompute_solutions_for_paper(paper, sleep_seconds: float = 1.0) -> dict:
    """Precompute solutions for all learner-visible questions in an approved paper."""
    if not paper:
        return {"total": 0, "completed": 0, "already_valid": 0, "failed": 0}

    from services.prep_ingestion import learner_visible_assessment_questions

    visible_qs = learner_visible_assessment_questions(
        paper.questions.filter(verification_status__in=PrepQuestion.ANSWERABLE_STATUSES).order_by("number", "id")
    )
    return precompute_solutions_for_questions(visible_qs, sleep_seconds=sleep_seconds)
