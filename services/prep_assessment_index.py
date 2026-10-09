import hashlib

from django.db import IntegrityError, transaction
from django.utils import timezone

from prep.models import PrepAssessmentIndexJob


ASSESSMENT_DOCUMENT_TYPES = {
    "Continuous Assessment Test (CAT)",
    "Final Examination Paper",
}


def assessment_source_signature(document):
    """Fingerprint the exact extracted source used to index a paper."""
    digest = hashlib.sha256()
    digest.update(str(document.pk).encode("utf-8"))
    digest.update(b"\0")
    digest.update(str(document.file_sha256 or "").encode("utf-8"))
    digest.update(b"\0")
    digest.update(str(document.extracted_text or "").encode("utf-8"))
    return digest.hexdigest()


def enqueue_assessment_index(paper, *, reconstruct_invalid=True, force=False):
    """Create one idempotent job for the currently approved source version."""
    document = paper.source_document
    if document is None:
        raise ValueError(f"Assessment paper {paper.pk} has no source document.")
    if document.stage != "stage_3":
        raise ValueError(f"Source document {document.pk} is not approved for publication.")
    if document.doc_type not in ASSESSMENT_DOCUMENT_TYPES:
        raise ValueError(f"Source document {document.pk} is not an assessment paper.")
    if not str(document.extracted_text or "").strip():
        raise ValueError(f"Source document {document.pk} has no extracted text to index.")

    signature = assessment_source_signature(document)
    try:
        with transaction.atomic():
            job, created = PrepAssessmentIndexJob.objects.get_or_create(
                paper=paper,
                source_signature=signature,
                reconstruct_invalid=reconstruct_invalid,
                defaults={
                    "source_document": document,
                    "next_attempt_at": timezone.now(),
                },
            )
            if force and not created:
                job = PrepAssessmentIndexJob.objects.select_for_update().get(pk=job.pk)
                if job.status in {"complete", "failed", "superseded"}:
                    job.status = "pending"
                    job.stage = "queued"
                    job.attempts = 0
                    job.indexed_questions = 0
                    job.next_attempt_at = timezone.now()
                    job.started_at = None
                    job.completed_at = None
                    job.last_error = ""
                    job.save(update_fields=[
                        "status", "stage", "attempts", "indexed_questions",
                        "next_attempt_at", "started_at", "completed_at", "last_error",
                    ])
                    created = True
    except IntegrityError:
        job = PrepAssessmentIndexJob.objects.get(
            paper=paper,
            source_signature=signature,
            reconstruct_invalid=reconstruct_invalid,
        )
        created = False
    return job, created
