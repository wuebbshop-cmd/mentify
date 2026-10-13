from __future__ import annotations

import hashlib
import json
import logging
from datetime import timedelta

from django.conf import settings
from django.db import close_old_connections, transaction
from django.db.models import F, Q
from django.utils import timezone
from django.utils.text import slugify

from prep.models import PrepQuestion, PrepTopic, PrepTopicPdfArtifact


logger = logging.getLogger(__name__)
NOTE_LEVELS = ("level_1", "level_2", "level_3")
MAX_ATTEMPTS = 3
STALE_JOB_MINUTES = 30


def _digest(payload) -> str:
    serialized = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def request_topic_pdf_artifact(
    topic: PrepTopic,
    artifact_type: str,
    level: str = "",
    *,
    source_signature: str = "",
    force: bool = False,
) -> tuple[PrepTopicPdfArtifact, bool]:
    """Queue or refresh one artifact without rendering in the caller's process."""
    if artifact_type not in {"notes", "questions"}:
        raise ValueError(f"Unsupported PDF artifact type: {artifact_type}")
    if artifact_type == "notes" and level not in NOTE_LEVELS:
        raise ValueError(f"Unsupported notes PDF level: {level}")
    if artifact_type == "questions" and level:
        raise ValueError("Question PDF artifacts do not have a note level.")

    now = timezone.now()
    with transaction.atomic():
        artifact, created = PrepTopicPdfArtifact.objects.select_for_update().get_or_create(
            topic=topic,
            artifact_type=artifact_type,
            level=level,
            defaults={
                "status": "pending",
                "source_signature": source_signature,
                "queued_at": now,
                "next_attempt_at": now,
            },
        )
        if created:
            return artifact, True
        if (
            not force
            and source_signature
            and artifact.source_signature == source_signature
            and artifact.status in {"pending", "running", "ready", "empty"}
        ):
            return artifact, False

        PrepTopicPdfArtifact.objects.filter(pk=artifact.pk).update(
            request_version=F("request_version") + 1,
            source_signature=source_signature or artifact.source_signature,
            status="running" if artifact.status == "running" else "pending",
            attempts=0,
            last_error="",
            queued_at=now,
            next_attempt_at=now,
            started_at=artifact.started_at if artifact.status == "running" else None,
            completed_at=None,
        )
        artifact.refresh_from_db()
        return artifact, True


def invalidate_topic_note_pdfs(topic: PrepTopic) -> int:
    """Prevent downloads of old note PDFs while the notes source is being rebuilt."""
    changed = 0
    existing_levels = set(
        PrepTopicPdfArtifact.objects.filter(
            topic=topic,
            artifact_type="notes",
        ).values_list("level", flat=True)
    )
    for level in existing_levels.intersection(NOTE_LEVELS):
        _, queued = request_topic_pdf_artifact(
            topic,
            "notes",
            level,
            force=True,
        )
        changed += int(queued)
    return changed


def enqueue_question_pdf_artifacts_for_record(question) -> int:
    """Refresh topic packs affected by an edited or removed question record."""
    topics = []
    if question.topic_id:
        topics.append(question.topic)
    elif question.paper_id and question.topic_label:
        candidates = PrepTopic.objects.filter(
            course=question.paper.course,
            is_active=True,
        ).order_by("order", "id")
        topics.extend(
            topic for topic in candidates
            if topic.title.casefold() in question.topic_label.casefold()
        )

    queued = 0
    for topic in topics:
        _, created = enqueue_topic_pdf_artifact(topic, "questions")
        queued += int(created)
    return queued


def _topic_question_records(topic: PrepTopic):
    from services.prep_ingestion import learner_visible_assessment_questions

    records = PrepQuestion.objects.filter(
        question_type__in=("authentic", "adapted"),
        verification_status__in=PrepQuestion.LEARNER_VISIBLE_STATUSES,
    ).filter(
        # Explicitly topic-linked questions and unlinked paper questions mapped
        # to this topic by the existing topic-label convention.
        Q(topic=topic)
        | Q(
            topic__isnull=True,
            paper__course=topic.course,
            topic_label__icontains=topic.title,
        )
    ).select_related("paper").order_by("paper", "number", "id")
    return learner_visible_assessment_questions(records)


def _load_artifact_source(artifact: PrepTopicPdfArtifact) -> tuple[str, dict]:
    topic = PrepTopic.objects.select_related("course").get(pk=artifact.topic_id)
    if artifact.artifact_type == "notes":
        from services.prep_ai_router import get_published_topic_note_levels

        notes = get_published_topic_note_levels(topic, validated_only=True).get(artifact.level, "")
        payload = {
            "kind": "notes",
            "topic_id": topic.pk,
            "course_code": topic.course.code,
            "course_title": topic.course.title,
            "topic_title": topic.title,
            "level": artifact.level,
            "content": notes,
        }
        return _digest(payload), payload

    from services.prep_ai_router import validated_question_solution

    records = _topic_question_records(topic)
    questions = []
    for question in records:
        questions.append({
            "id": question.pk,
            "number": question.number,
            "marks": question.marks,
            "topic": question.topic_label or topic.title,
            "paper_title": question.paper.title if question.paper else f"{topic.course.code} Examination",
            "year": question.paper.year if question.paper else "Official Examination",
            "question_latex": question.question_latex,
            "solution_latex": validated_question_solution(question),
        })
    payload = {
        "kind": "questions",
        "topic_id": topic.pk,
        "course_code": topic.course.code,
        "course_title": topic.course.title,
        "topic_title": topic.title,
        "questions": questions,
    }
    return _digest(payload), payload


def enqueue_topic_pdf_artifact(
    topic: PrepTopic,
    artifact_type: str,
    level: str = "",
    *,
    force: bool = False,
) -> tuple[PrepTopicPdfArtifact, bool]:
    signature, _ = _load_artifact_source(
        PrepTopicPdfArtifact(topic=topic, artifact_type=artifact_type, level=level)
    )
    return request_topic_pdf_artifact(
        topic,
        artifact_type,
        level,
        source_signature=signature,
        force=force,
    )


def enqueue_existing_topic_pdf_artifacts() -> int:
    """Idempotently seed missing/stale artifacts for the active topic catalogue."""
    from services.prep_ai_router import get_published_topic_note_levels

    queued = 0
    topics = PrepTopic.objects.filter(is_active=True).select_related("course").order_by("course_id", "order", "id")
    for topic in topics.iterator():
        published_levels = get_published_topic_note_levels(topic, validated_only=True)
        for level in NOTE_LEVELS:
            if published_levels.get(level):
                _, created = enqueue_topic_pdf_artifact(topic, "notes", level)
                queued += int(created)
        _, created = enqueue_topic_pdf_artifact(topic, "questions")
        queued += int(created)
    return queued


def enqueue_paper_topic_question_pdfs(paper) -> int:
    """Reconcile every course topic after a paper is indexed or reverified."""
    topics = PrepTopic.objects.filter(course=paper.course, is_active=True).order_by("order", "id")
    queued = 0
    for topic in topics:
        _, created = enqueue_topic_pdf_artifact(topic, "questions")
        queued += int(created)
    return queued


def _claim_artifact():
    now = timezone.now()
    with transaction.atomic():
        artifact = (
            PrepTopicPdfArtifact.objects.select_for_update(skip_locked=True)
            .filter(status="pending", next_attempt_at__lte=now)
            .order_by("queued_at", "id")
            .first()
        )
        if artifact is None:
            return None
        artifact.status = "running"
        artifact.attempts += 1
        artifact.started_at = now
        artifact.last_error = ""
        artifact.save(update_fields=["status", "attempts", "started_at", "last_error"])
        return artifact.pk, artifact.request_version


def _recover_stale_artifacts():
    cutoff = timezone.now() - timedelta(minutes=STALE_JOB_MINUTES)
    PrepTopicPdfArtifact.objects.filter(status="running", started_at__lt=cutoff).update(
        status="pending",
        started_at=None,
        next_attempt_at=timezone.now(),
        last_error="Recovered after the PDF worker stopped during rendering.",
    )


def _mark_empty(artifact_id: int, request_version: int, signature: str) -> None:
    with transaction.atomic():
        artifact = PrepTopicPdfArtifact.objects.select_for_update().get(pk=artifact_id)
        if artifact.request_version != request_version:
            artifact.status = "pending"
            artifact.started_at = None
            artifact.next_attempt_at = timezone.now()
            artifact.save(update_fields=["status", "started_at", "next_attempt_at"])
            return
        artifact.source_signature = signature
        artifact.status = "empty"
        artifact.started_at = None
        artifact.completed_at = timezone.now()
        artifact.last_error = ""
        artifact.save(update_fields=[
            "source_signature", "status", "started_at", "completed_at", "last_error",
        ])


def _requeue_current_source(artifact_id: int, request_version: int, signature: str) -> None:
    """Release a running row when its source changed during a render."""
    now = timezone.now()
    with transaction.atomic():
        artifact = PrepTopicPdfArtifact.objects.select_for_update().get(pk=artifact_id)
        updates = {
            "source_signature": signature,
            "status": "pending",
            "attempts": 0,
            "last_error": "",
            "queued_at": now,
            "next_attempt_at": now,
            "started_at": None,
            "completed_at": None,
        }
        if artifact.request_version == request_version:
            updates["request_version"] = F("request_version") + 1
        PrepTopicPdfArtifact.objects.filter(pk=artifact_id).update(**updates)


def _render_artifact(payload: dict) -> bytes:
    from services.prep_export_service import export_paper_questions_pdf, export_topic_notes_pdf

    if payload["kind"] == "notes":
        return export_topic_notes_pdf(
            payload["course_code"],
            payload["topic_title"],
            payload["content"],
            level=payload["level"],
            require_playwright=True,
            timeout_ms=60000,
        )
    questions = payload["questions"]
    return export_paper_questions_pdf(
        payload["course_code"],
        f"{payload['topic_title']} Past Questions and Answers",
        "Compiled Topic Set",
        sum(question["marks"] for question in questions),
        questions,
        include_questions=True,
        include_answers=True,
        require_playwright=True,
        timeout_ms=60000,
    )


def _upload_artifact(topic: PrepTopic, artifact_type: str, level: str, signature: str, pdf_bytes: bytes) -> str:
    from services.github_service import GitHubService

    token = getattr(settings, "GITHUB_TOKEN", "").strip()
    repo = getattr(settings, "GITHUB_REPO", "").strip()
    branch = getattr(settings, "GITHUB_BRANCH", "main").strip() or "main"
    upload_dir = getattr(settings, "GITHUB_UPLOAD_DIR", "uploads").strip("/")
    storage_dir = getattr(settings, "PREP_PDF_STORAGE_DIR", "prep-pdfs").strip("/")
    if not token or not repo:
        raise RuntimeError("GITHUB_TOKEN and GITHUB_REPO are required to publish PDF artifacts.")
    course_slug = slugify(topic.course.code) or f"course-{topic.course_id}"
    topic_slug = slugify(topic.title)[:80] or f"topic-{topic.pk}"
    filename = f"{artifact_type}-{level or 'all'}-{signature[:24]}.pdf"
    repo_path = f"{upload_dir}/{storage_dir}/{course_slug}/{topic.pk}-{topic_slug}/{filename}"
    GitHubService(token=token, repo_name=repo, branch=branch, upload_dir=upload_dir).upload_bytes(
        repo_path,
        pdf_bytes,
        f"[Mentify] Publish {artifact_type} PDF for topic {topic.pk} ({signature[:12]})",
    )
    return repo_path


def _process_artifact(claim: tuple[int, int]) -> None:
    artifact_id, request_version = claim
    artifact = PrepTopicPdfArtifact.objects.select_related("topic__course").get(pk=artifact_id)
    signature, payload = _load_artifact_source(artifact)
    if not payload.get("content") and payload["kind"] == "notes":
        _mark_empty(artifact_id, request_version, signature)
        return
    if not payload.get("questions") and payload["kind"] == "questions":
        _mark_empty(artifact_id, request_version, signature)
        return

    with transaction.atomic():
        locked = PrepTopicPdfArtifact.objects.select_for_update().get(pk=artifact_id)
        if locked.request_version != request_version:
            locked.status = "pending"
            locked.source_signature = signature
            locked.started_at = None
            locked.next_attempt_at = timezone.now()
            locked.save(update_fields=["status", "source_signature", "started_at", "next_attempt_at"])
            return
        locked.source_signature = signature
        locked.save(update_fields=["source_signature"])

    pdf_bytes = _render_artifact(payload)
    if not pdf_bytes.startswith(b"%PDF") or len(pdf_bytes) < 1000:
        raise RuntimeError("The pinned Chromium renderer did not produce a valid PDF.")

    latest = PrepTopicPdfArtifact.objects.get(pk=artifact_id)
    latest_signature, _ = _load_artifact_source(latest)
    if latest_signature != signature or latest.request_version != request_version:
        _requeue_current_source(artifact_id, request_version, latest_signature)
        return

    repo_path = _upload_artifact(
        artifact.topic,
        artifact.artifact_type,
        artifact.level,
        signature,
        pdf_bytes,
    )
    with transaction.atomic():
        locked = PrepTopicPdfArtifact.objects.select_for_update().get(pk=artifact_id)
        if locked.request_version != request_version or locked.source_signature != signature:
            locked.status = "pending"
            locked.started_at = None
            locked.next_attempt_at = timezone.now()
            locked.save(update_fields=["status", "started_at", "next_attempt_at"])
            logger.info("Discarding superseded PDF artifact %s after upload.", artifact_id)
            return
        locked.status = "ready"
        locked.published_signature = signature
        locked.github_path = repo_path
        locked.started_at = None
        locked.completed_at = timezone.now()
        locked.last_error = ""
        locked.save(update_fields=[
            "status", "published_signature", "github_path", "started_at",
            "completed_at", "last_error",
        ])


def process_next_pdf_artifact() -> bool:
    """Process one queued artifact; return whether a job was claimed."""
    if not transaction.get_connection().in_atomic_block:
        close_old_connections()
    _recover_stale_artifacts()
    claim = _claim_artifact()
    if claim is None:
        return False
    artifact_id, _ = claim
    try:
        _process_artifact(claim)
    except Exception as exc:
        logger.exception("PDF artifact job %s failed.", artifact_id)
        with transaction.atomic():
            artifact = PrepTopicPdfArtifact.objects.select_for_update().get(pk=artifact_id)
            artifact.last_error = str(exc)[:4000]
            artifact.started_at = None
            if artifact.attempts < MAX_ATTEMPTS:
                artifact.status = "pending"
                artifact.next_attempt_at = timezone.now() + timedelta(minutes=min(2 ** artifact.attempts, 30))
            else:
                artifact.status = "failed"
                artifact.completed_at = timezone.now()
            artifact.save(update_fields=[
                "last_error", "started_at", "status", "next_attempt_at", "completed_at",
            ])
    finally:
        close_old_connections()
    return True


def github_pdf_bytes(repo_path: str) -> bytes:
    """Read a ready PDF through the configured authenticated GitHub repository."""
    from services.github_service import GitHubService

    token = getattr(settings, "GITHUB_TOKEN", "").strip()
    repo = getattr(settings, "GITHUB_REPO", "").strip()
    branch = getattr(settings, "GITHUB_BRANCH", "main").strip() or "main"
    if not token or not repo:
        raise RuntimeError("GitHub PDF storage is not configured.")
    stored_path = f"github://{repo}/{branch}/{repo_path.lstrip('/')}"
    return GitHubService(token=token, repo_name=repo, branch=branch).download_file(stored_path)
