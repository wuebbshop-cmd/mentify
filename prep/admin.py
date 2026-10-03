import json
from pathlib import Path
from uuid import uuid4

import fitz
from django.contrib import admin
from django import forms
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.utils import timezone
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.urls import path, reverse
from django.db.models import Count

from .models import (
    PrepCourse,
    PrepCourseEnrollment,
    PrepTopic,
    PrepDocument,
    PrepDocumentVisual,
    PrepContentUpdate,
    PrepPaper,
    PrepQuestion,
    PrepContentCache,
    PrepNoteGenerationGuard,
    PrepNoteRepair,
    PrepWallet,
    PrepCreditGrant,
    PrepTransaction,
    PrepHistory,
    PrepNotification,
)
from services.credit_service import grant_credits, grant_subscription


def _apply_approved_course_profile(document, profile_data: dict) -> bool:
    from services.prep_ingestion import COURSE_STUDY_FAMILIES
    from prep.content_rules import validate_content_rule_set

    course = document.course
    family = str(profile_data.get("subject_family") or "")
    family_config = COURSE_STUDY_FAMILIES.get(family)
    if (
        not family_config
        or document.doc_type not in {"Lecture Notes", "Revision Sheet"}
        or str(profile_data.get("source_document_id")) != str(document.pk)
    ):
        return False
    if profile_data.get("content_rules") and validate_content_rule_set(
        profile_data["content_rules"], source_document_id=str(document.pk)
    ):
        return False

    profile = dict(profile_data)
    profile["version"] = course.study_profile_version + 1
    course.category = family_config["category"]
    course.study_profile = profile
    course.study_profile_version += 1
    course.save(update_fields=["category", "study_profile", "study_profile_version", "updated_at"])

    outline = profile.get("topic_outline")
    if profile.get("covers_full_syllabus") and isinstance(outline, list) and outline:
        approved_topics = {
            (int(item.get("order") or 1), " ".join(str(item.get("title") or "").casefold().split()))
            for item in outline
            if isinstance(item, dict) and str(item.get("title") or "").strip()
        }
        for topic in course.topics.all():
            key = (topic.order, " ".join(topic.title.casefold().split()))
            should_be_active = key in approved_topics
            if topic.is_active != should_be_active:
                topic.is_active = should_be_active
                topic.save(update_fields=["is_active"])
    return True


class VerificationQueueFilter(admin.SimpleListFilter):
    """Filter to quickly identify documents needing tutor/admin attention."""
    title = "Review Status"
    parameter_name = "review_status"

    def lookups(self, request, model_admin):
        return [
            ("needs_tutor_review", "⚡ Needs Tutor Review (Stage 2)"),
            ("stage_1_ingestion", "Stage 1: Ingestion & Extraction"),
            ("published_stage_3", "✓ Stage 3: Published & Live"),
            ("rejected", "✕ Rejected"),
            ("has_text", "Has Extracted Text"),
            ("no_text", "No Extracted Text"),
        ]

    def queryset(self, request, queryset):
        val = self.value()
        if val == "needs_tutor_review":
            return queryset.filter(stage="stage_2")
        elif val == "stage_1_ingestion":
            return queryset.filter(stage="stage_1")
        elif val == "published_stage_3":
            return queryset.filter(stage="stage_3")
        elif val == "rejected":
            return queryset.filter(stage="rejected")
        elif val == "has_text":
            return queryset.exclude(extracted_text__exact="")
        elif val == "no_text":
            return queryset.filter(extracted_text__exact="")
        return queryset


class PrepPaperInline(admin.TabularInline):
    model = PrepPaper
    extra = 0
    show_change_link = True
    fields = ("id", "title", "year", "total_marks", "is_published")


def _open_visual_source_page(visual):
    if not visual.document.file:
        raise ValueError("The source PDF is not available.")
    with visual.document.file.open("rb") as source_file:
        pdf_bytes = source_file.read()
    source = fitz.open(stream=pdf_bytes, filetype="pdf")
    page_index = visual.page_number - 1
    if page_index < 0 or page_index >= len(source):
        source.close()
        raise ValueError("The visual page number is outside the source PDF.")
    return source, source[page_index]


class VisualTopicFilter(admin.SimpleListFilter):
    title = "Topic"
    parameter_name = "visual_topic"

    def lookups(self, request, model_admin):
        topics = PrepTopic.objects.filter(
            course__documents__visual_candidates__isnull=False,
        ).select_related("course").distinct().order_by("course__code", "order", "title")
        course_id = request.GET.get("document__course__id__exact")
        if course_id and course_id.isdigit():
            topics = topics.filter(course_id=course_id)
        return [(str(topic.pk), f"{topic.course.code} / {topic.title}") for topic in topics]

    def queryset(self, request, queryset):
        if not self.value():
            return queryset
        topic = PrepTopic.objects.filter(pk=self.value()).first()
        if not topic:
            return queryset.none()
        return queryset.filter(
            Q(reviewed_topic=topic)
            | Q(extracted_content__auto_topic=topic.title)
            | Q(document__topic_name=topic.title)
        )


class PrepDocumentVisualReviewForm(forms.ModelForm):
    bbox = forms.JSONField(widget=forms.HiddenInput)

    class Meta:
        model = PrepDocumentVisual
        fields = ("status", "reviewed_topic", "review_notes", "bbox")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            topics = PrepTopic.objects.filter(course_id=self.instance.document.course_id)
            self.fields["reviewed_topic"].queryset = topics
            if not self.instance.reviewed_topic_id:
                metadata = self.instance.extracted_content
                suggested_topic = metadata.get("auto_topic") if isinstance(metadata, dict) else ""
                match = topics.filter(title__iexact=suggested_topic).first() if suggested_topic else None
                if match:
                    self.initial["reviewed_topic"] = match.pk
            self.initial["bbox"] = self.instance.bbox

    def clean_bbox(self):
        bbox = self.cleaned_data["bbox"]
        if (
            not isinstance(bbox, list)
            or len(bbox) != 4
            or any(not isinstance(value, (int, float)) or isinstance(value, bool) for value in bbox)
        ):
            raise forms.ValidationError("Select a valid crop rectangle on the source page.")
        x0, y0, x1, y1 = map(float, bbox)
        if x1 - x0 < 20 or y1 - y0 < 20:
            raise forms.ValidationError("The crop must be at least 20 PDF points wide and high.")
        try:
            source, page = _open_visual_source_page(self.instance)
        except (OSError, ValueError, fitz.FileDataError) as exc:
            raise forms.ValidationError(f"Could not read the source page: {exc}") from exc
        try:
            page_rect = page.rect
            if x0 < page_rect.x0 or y0 < page_rect.y0 or x1 > page_rect.x1 or y1 > page_rect.y1:
                raise forms.ValidationError("Keep the crop rectangle inside the source page.")
        finally:
            source.close()
        return [round(x0, 2), round(y0, 2), round(x1, 2), round(y1, 2)]

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("status") == "approved" and not cleaned_data.get("reviewed_topic"):
            self.add_error("reviewed_topic", "Choose the topic this figure belongs to before approving it.")
        return cleaned_data


@admin.register(PrepDocument)
class PrepDocumentAdmin(admin.ModelAdmin):
    """
    Stage 2 Tutor/Admin Verification Queue & Publishing Engine.
    Allows tutors and admins to inspect incoming course notes and CAT papers,
    verify extracted LaTeX, edit review notes, and publish to the live course knowledge graph.
    """
    list_display = (
        "course_badge",
        "doc_type",
        "academic_year",
        "topic_name",
        "stage_badge",
        "file_preview",
        "uploader_info",
        "created_at",
    )
    list_filter = (VerificationQueueFilter, "stage", "doc_type", "course__category", "course")
    search_fields = ("course__code", "course__title", "topic_name", "academic_year", "user__email", "extracted_text")
    readonly_fields = (
        "id", "file_size_display", "file_preview_link", "file_sha256", "text_sha256",
        "is_duplicate", "duplicate_of", "validation_report", "created_at", "updated_at",
    )
    inlines = [PrepPaperInline]
    date_hierarchy = "created_at"

    fieldsets = (
        ("Document Identification", {
            "fields": (
                "course",
                "doc_type",
                "academic_year",
                "topic_name",
                "user",
            )
        }),
        ("Uploaded File & Permanent Storage", {
            "fields": (
                "file",
                "file_preview_link",
                "file_size_display",
                "github_raw_url",
            )
        }),
        ("Stage 2 Tutor Review Gate", {
            "fields": (
                "stage",
                "tutor_review_notes",
                "reviewed_by",
                "reviewed_at",
            ),
            "description": "Tutors review mathematical correctness, syllabus alignment, and verify OCR/LaTeX formulas.",
        }),
        ("Extracted Content & LaTeX", {
            "classes": ("collapse",),
            "fields": ("extracted_text",),
            "description": "Raw extracted text or parsed LaTeX from pdfplumber / Together.ai Vision OCR.",
        }),
        ("Automated Validation Report", {
            "classes": ("collapse",),
            "fields": ("validation_report",),
            "description": "Review findings and source provenance. Error-level conflicts with approved modality rules block publication.",
        }),
        ("Duplicate & Update Analysis", {
            "classes": ("collapse",),
            "fields": ("is_duplicate", "duplicate_of", "file_sha256", "text_sha256"),
            "description": "Duplicate uploads are excluded from re-indexing. Content additions are reviewed as pending update proposals below.",
        }),
        ("Audit Metadata", {
            "classes": ("collapse",),
            "fields": ("id", "created_at", "updated_at"),
        }),
    )

    actions = [
        "approve_stage_3_publish",
        "move_to_stage_2_review",
        "requeue_stage_1_extraction",
        "propose_course_study_profile",
        "index_assessment_questions",
        "reject_document",
    ]

    def _apply_safe_content_updates(self, document, reviewer, now):
        """Apply only additive, reviewer-approved updates; never overwrite a topic."""
        applied = 0
        for update in document.content_updates.filter(status="pending").select_related("topic"):
            data = update.proposed_data if isinstance(update.proposed_data, dict) else {}
            topic = update.topic

            if update.update_type == "course_profile":
                if not _apply_approved_course_profile(document, data):
                    continue
            elif update.update_type == "topic_content_rules" and topic:
                from prep.content_rules import validate_content_rule_set

                if (
                    topic.course_id != document.course_id
                    or document.doc_type not in {"Lecture Notes", "Revision Sheet"}
                    or not isinstance(data.get("content_rules"), dict)
                    or validate_content_rule_set(
                        data["content_rules"], source_document_id=str(document.pk)
                    )
                ):
                    continue
                topic.content_rules = data["content_rules"]
                topic.save(update_fields=["content_rules"])
            elif update.update_type == "new_topic":
                order = int(data.get("order") or 1)
                title = str(data.get("title") or "").strip()
                if not title:
                    continue
                topic, created = PrepTopic.objects.get_or_create(
                    course=document.course,
                    order=order,
                    defaults={
                        "title": title,
                        "subtopics": data.get("subtopics") if isinstance(data.get("subtopics"), list) else [],
                        "summary": str(data.get("summary") or "").strip(),
                    },
                )
                if not created and topic.title.strip().casefold() != title.casefold():
                    # Another reviewer has already established a different
                    # canonical topic at this order. Keep this proposal
                    # pending rather than silently attaching it to that topic.
                    continue
            elif update.update_type == "add_subtopics" and topic:
                existing = topic.subtopics if isinstance(topic.subtopics, list) else []
                existing_keys = {str(item).strip().casefold() for item in existing}
                additions = [
                    str(item).strip() for item in data.get("subtopics", [])
                    if str(item).strip() and str(item).strip().casefold() not in existing_keys
                ]
                if additions:
                    topic.subtopics = [*existing, *additions]
                    topic.save(update_fields=["subtopics"])
            elif update.update_type == "fill_summary" and topic and not topic.summary.strip():
                summary = str(data.get("summary") or "").strip()
                if summary:
                    topic.summary = summary
                    topic.save(update_fields=["summary"])
            else:
                # Summary changes require an explicit per-proposal admin decision.
                continue

            update.status = "approved"
            update.reviewed_by = reviewer
            update.reviewed_at = now
            update.save(update_fields=["status", "reviewed_by", "reviewed_at"])
            applied += 1
        return applied

    def course_badge(self, obj):
        return format_html(
            '<span style="font-weight:700; background:#0f766e; color:#ffffff; padding:3px 8px; border-radius:4px;">{}</span> {}',
            obj.course.code,
            obj.course.title[:25] + ("..." if len(obj.course.title) > 25 else ""),
        )
    course_badge.short_description = "Course Unit"
    course_badge.admin_order_field = "course__code"

    def stage_badge(self, obj):
        colors = {
            "stage_1": ("#0284c7", "#e0f2fe", "Stage 1: Ingestion"),
            "stage_2": ("#d97706", "#fef3c7", "⚡ Stage 2: Tutor Review"),
            "stage_3": ("#16a34a", "#dcfce7", "✓ Stage 3: Published"),
            "rejected": ("#dc2626", "#fee2e2", "✕ Rejected"),
        }
        color, bg, label = colors.get(obj.stage, ("#64748b", "#f1f5f9", obj.stage))
        return format_html(
            '<span style="display:inline-block; font-size:0.75rem; font-weight:700; color:{}; background:{}; padding:3px 10px; border-radius:12px; border:1px solid {};">{}</span>',
            color, bg, color, label
        )
    stage_badge.short_description = "Pipeline Stage"
    stage_badge.admin_order_field = "stage"

    def file_preview(self, obj):
        if obj.file:
            return format_html(
                '<a href="{}" target="_blank" style="color:#0f766e; font-weight:600; text-decoration:underline;">View PDF</a>',
                obj.file.url
            )
        return "—"
    file_preview.short_description = "Original PDF"

    def file_preview_link(self, obj):
        if obj.file:
            return format_html(
                '<a href="{}" target="_blank" class="button" style="background:#0f766e; color:#ffffff; padding:6px 12px; border-radius:4px; text-decoration:none;">Open Uploaded PDF File</a>',
                obj.file.url
            )
        return "No file uploaded"
    file_preview_link.short_description = "PDF Action"

    def file_size_display(self, obj):
        if obj.file_size_bytes:
            mb = round(obj.file_size_bytes / (1024 * 1024), 2)
            return f"{mb} MB ({obj.file_size_bytes:,} bytes)"
        return "Unknown"
    file_size_display.short_description = "File Size"

    def uploader_info(self, obj):
        if obj.user:
            return obj.user.get_full_name() or obj.user.email
        return "Guest / System"
    uploader_info.short_description = "Uploaded By"

    @admin.action(description="✓ Stage 3: Approve, Publish & Integrate into Course Graph")
    def approve_stage_3_publish(self, request, queryset):
        """
        Publishing Engine:
        1. Promotes selected documents to Stage 3 (Published).
        2. Automatically creates or publishes derived PrepPaper if the document is a CAT/Exam paper.
        3. Stamps reviewed_by and reviewed_at.
        4. Logs publication into student's PrepHistory for real-time dashboard notification.
        """
        published_papers_count = 0
        applied_updates_count = 0
        published_documents_count = 0
        ingestion_failures = 0
        validation_failures = 0
        courses_to_precompute = set()
        now = timezone.now()

        for doc in queryset:
            if doc.is_duplicate:
                continue

            # Admin publication is the final ingestion gate. Older uploads or
            # failed requests may still be at Stage 1 with no extracted text;
            # never publish those rows until ingestion succeeds.
            if doc.stage == "stage_1" or not doc.extracted_text.strip():
                from services.prep_ingestion import process_prep_document

                try:
                    ingestion_result = process_prep_document(doc)
                except Exception as exc:
                    ingestion_result = {"success": False, "error": str(exc)}
                if not ingestion_result.get("success") or not doc.extracted_text.strip():
                    ingestion_failures += 1
                    doc.tutor_review_notes = f"Publication blocked: ingestion failed. {ingestion_result.get('error', 'No extracted content was produced.')[:1000]}"
                    doc.save(update_fields=["tutor_review_notes", "updated_at"])
                    continue

            from prep.document_validation import validate_prep_document

            doc.validation_report = validate_prep_document(doc)
            doc.save(update_fields=["validation_report", "updated_at"])
            blocking_issues = [
                issue for issue in doc.validation_report.get("issues", [])
                if issue.get("severity") == "error"
            ]
            if blocking_issues:
                validation_failures += 1
                reasons = "; ".join(issue.get("message", "Validation error") for issue in blocking_issues)
                doc.tutor_review_notes = f"Publication blocked by validation: {reasons}"[:2000]
                doc.save(update_fields=["tutor_review_notes", "updated_at"])
                continue

            doc.stage = "stage_3"
            doc.reviewed_by = request.user
            doc.reviewed_at = now
            if not doc.tutor_review_notes:
                doc.tutor_review_notes = f"Approved and verified for syllabus inclusion by {request.user.get_full_name() or request.user.email}."
            doc.save()
            applied_updates_count += self._apply_safe_content_updates(doc, request.user, now)
            if doc.doc_type in {"Lecture Notes", "Revision Sheet"} and doc.visual_candidates.exists():
                from services.prep_ingestion import assign_visuals_to_topics

                assign_visuals_to_topics(
                    doc,
                    list(doc.course.topics.filter(is_active=True).order_by("order", "id")),
                    allow_auto_approval=True,
                )
            published_documents_count += 1
            if doc.doc_type in {"Lecture Notes", "Revision Sheet"}:
                courses_to_precompute.add(doc.course_id)

            # Auto-create or publish derived paper if doc is CAT or Exam
            if doc.doc_type in ["Continuous Assessment Test (CAT)", "Final Examination Paper"]:
                paper_id = f"{doc.course.code.lower().replace(' ', '')}-doc-{str(doc.id)[:8]}"
                title = f"{doc.doc_type} ({doc.academic_year or 'Current Session'})"
                marks = 70 if "Final" in doc.doc_type else 30

                paper, created = PrepPaper.objects.get_or_create(
                    id=paper_id,
                    defaults={
                        "course": doc.course,
                        "title": title,
                        "year": doc.academic_year or "Current Academic Year",
                        "total_marks": marks,
                        "source_document": doc,
                        "is_published": True,
                    }
                )
                if not created and not paper.is_published:
                    paper.is_published = True
                    paper.save()
                from services.prep_ingestion import index_assessment_questions
                index_assessment_questions(doc, paper)
                published_papers_count += 1

            # Log to student's history
            if doc.user:
                PrepHistory.objects.create(
                    user=doc.user,
                    title=f"Verified: {doc.course.code} {doc.doc_type}",
                    course_code=doc.course.code,
                    item_type="Document Verified",
                    url=reverse("prep:past_papers") if "CAT" in doc.doc_type or "Exam" in doc.doc_type else reverse("prep:courses"),
                )
                course_slug = doc.course.slug or doc.course.code.replace(" ", "-")
                PrepNotification.objects.create(
                    user=doc.user,
                    title=f"Published: {doc.course.code} {doc.doc_type}",
                    message=f"Your uploaded material for '{doc.course.code}' has been reviewed, verified, and published to the live course knowledge graph.",
                    category="published",
                    url=reverse("prep:course_detail", kwargs={"course_code": course_slug}),
                )

            # Trigger Step 6 Email Automation (Resend)
            try:
                from services.email_service import send_prep_review_completed_email
                send_prep_review_completed_email(doc)
            except Exception as e:
                pass

        queued_precomputations = 0
        for course_id in courses_to_precompute:
            from services.prep_note_precompute import enqueue_course_level_two_precompute

            course = PrepCourse.objects.get(pk=course_id)
            _, queued = enqueue_course_level_two_precompute(course)
            queued_precomputations += int(queued)

        self.message_user(
            request,
            f"Successfully approved and published {published_documents_count} document(s) to Stage 3. "
            f"Applied {applied_updates_count} additive course update(s) and activated {published_papers_count} course paper(s). "
            f"Queued Level 2 note preparation for {queued_precomputations} course(s). "
            f"Blocked {ingestion_failures} document(s) whose ingestion did not complete and "
            f"{validation_failures} document(s) with validation errors."
        )

    @admin.action(description="Propose subject profile from selected lecture notes")
    def propose_course_study_profile(self, request, queryset):
        from services.prep_ingestion import (
            create_content_update_proposals,
            extract_course_study_profile,
        )

        proposed = 0
        skipped = 0
        for document in queryset.filter(doc_type__in=["Lecture Notes", "Revision Sheet"]):
            profile = extract_course_study_profile(
                document.course,
                document.extracted_text,
                source_document=document,
            )
            if not profile:
                skipped += 1
                continue
            proposed += len(create_content_update_proposals(
                document.course,
                document,
                [],
                course_profile=profile,
            ))
        self.message_user(
            request,
            f"Created {proposed} course-profile proposal(s) from notes. {skipped} document(s) had insufficient grounded evidence.",
        )

    @admin.action(description="⚡ Stage 2: Move to Tutor Review Gate")
    def move_to_stage_2_review(self, request, queryset):
        count = queryset.update(stage="stage_2")
        self.message_user(request, f"{count} document(s) assigned to Stage 2 Tutor Review Gate.")

    @admin.action(description="↺ Re-queue for Stage 1 Ingestion / OCR Extraction")
    def requeue_stage_1_extraction(self, request, queryset):
        from services.prep_ingestion import process_prep_document

        processed = 0
        failed = 0
        for document in queryset:
            document.stage = "stage_1"
            document.save(update_fields=["stage", "updated_at"])
            try:
                result = process_prep_document(document)
                if result.get("success"):
                    processed += 1
                else:
                    failed += 1
                    document.tutor_review_notes = f"Re-ingestion failed: {result.get('error', 'Unknown ingestion error')[:1000]}"
                    document.save(update_fields=["tutor_review_notes", "updated_at"])
            except Exception as exc:
                failed += 1
                document.tutor_review_notes = f"Re-ingestion failed: {str(exc)[:1000]}"
                document.save(update_fields=["tutor_review_notes", "updated_at"])
        self.message_user(
            request,
            f"Reprocessed {processed} document(s). {failed} document(s) still require attention.",
        )

    @admin.action(description="Index approved assessment questions from extracted text")
    def index_assessment_questions(self, request, queryset):
        from services.prep_ingestion import index_assessment_questions

        indexed = 0
        skipped = 0
        for doc in queryset.filter(doc_type__in=["Continuous Assessment Test (CAT)", "Final Examination Paper"]):
            paper = PrepPaper.objects.filter(source_document=doc).first()
            if not paper:
                skipped += 1
                continue
            indexed += index_assessment_questions(doc, paper)
        self.message_user(request, f"Indexed {indexed} question(s). Skipped {skipped} document(s) without a linked paper.")

    @admin.action(description="✕ Reject Selected Documents")
    def reject_document(self, request, queryset):
        now = timezone.now()
        for doc in queryset:
            doc.stage = "rejected"
            doc.reviewed_by = request.user
            doc.reviewed_at = now
            doc.save()
            if doc.user:
                PrepNotification.objects.create(
                    user=doc.user,
                    title=f"Review Update: {doc.course.code}",
                    message=f"Material '{doc.file.name.split('/')[-1]}' was reviewed: {doc.tutor_review_notes or 'Requires revision or clarification before syllabus inclusion.'}",
                    category="rejected",
                    url=reverse("prep:upload"),
                )
            try:
                from services.email_service import send_prep_review_completed_email
                send_prep_review_completed_email(doc)
            except Exception:
                pass
        self.message_user(request, f"{queryset.count()} document(s) marked as Rejected and feedback notification sent.")


class PrepQuestionInline(admin.StackedInline):
    model = PrepQuestion
    extra = 1
    fields = (
        ("number", "marks", "topic_label", "verification_status"),
        "question_latex",
        "solution_latex",
    )


@admin.register(PrepDocumentVisual)
class PrepDocumentVisualAdmin(admin.ModelAdmin):
    form = PrepDocumentVisualReviewForm
    list_display = (
        "page_number",
        "document_link",
        "visual_type",
        "topic_display",
        "status",
        "updated_at",
    )
    list_filter = ("status", "visual_type", "document__course", VisualTopicFilter)
    search_fields = (
        "document__course__code",
        "document__course__title",
        "document__topic_name",
        "reviewed_topic__title",
    )
    readonly_fields = (
        "document",
        "page_number",
        "visual_type",
        "candidate_reasons",
        "crop_editor",
        "crop_preview",
        "context_preview",
        "context_text",
        "neighboring_text",
        "labels",
        "extracted_content",
        "reviewed_by",
        "reviewed_at",
        "created_at",
        "updated_at",
    )
    fieldsets = (
        ("Figure and Source Context", {
            "fields": (
                "document",
                "page_number",
                "visual_type",
                "crop_editor",
                "bbox",
                "crop_preview",
                "context_preview",
                "neighboring_text",
                "context_text",
                "candidate_reasons",
                "labels",
                "extracted_content",
            ),
        }),
        ("Review Decision", {
            "fields": ("status", "reviewed_topic", "review_notes"),
        }),
        ("Review Audit", {
            "fields": ("reviewed_by", "reviewed_at", "created_at", "updated_at"),
        }),
    )
    ordering = ("status", "document__course__code", "page_number")
    list_per_page = 25

    class Media:
        js = ("prep/admin/visual_crop_editor.js",)
        css = {"all": ("prep/admin/visual_crop_editor.css",)}

    def get_urls(self):
        custom_urls = [
            path(
                "<path:object_id>/source-page/",
                self.admin_site.admin_view(self.source_page_preview),
                name="prep_prepdocumentvisual_source_page",
            ),
        ]
        return custom_urls + super().get_urls()

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            "document", "document__course", "reviewed_topic", "reviewed_by"
        )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    @admin.display(description="Source document")
    def document_link(self, obj):
        url = reverse("admin:prep_prepdocument_change", args=(obj.document_id,))
        return format_html('<a href="{}">{}</a>', url, obj.document)

    @admin.display(description="Assigned topic")
    def topic_display(self, obj):
        if obj.reviewed_topic_id:
            return obj.reviewed_topic.title
        metadata = obj.extracted_content if isinstance(obj.extracted_content, dict) else {}
        return metadata.get("auto_topic") or "Unassigned"

    @staticmethod
    def _image_preview(field, label):
        try:
            url = field.url if field else ""
        except (ValueError, OSError):
            url = ""
        if not url:
            return "No image available"
        return format_html(
            '<a href="{}" target="_blank"><img src="{}" alt="{}" '
            'style="display:block;max-width:100%;max-height:520px;border:1px solid #bbb"></a>',
            url,
            url,
            label,
        )

    @admin.display(description="Figure crop")
    def crop_preview(self, obj):
        return self._image_preview(obj.crop, f"Page {obj.page_number} figure crop")

    @admin.display(description="Full-width neighboring context")
    def context_preview(self, obj):
        return self._image_preview(obj.context_crop, f"Page {obj.page_number} surrounding context")

    @admin.display(description="Adjust crop on original PDF page")
    def crop_editor(self, obj):
        if not obj or not obj.pk:
            return "Save the visual before adjusting its crop."
        try:
            source, page = _open_visual_source_page(obj)
        except (OSError, ValueError, fitz.FileDataError):
            return "Original PDF page is unavailable."
        try:
            page_width = page.rect.width
            page_height = page.rect.height
        finally:
            source.close()
        preview_url = reverse("admin:prep_prepdocumentvisual_source_page", args=(obj.pk,))
        bbox_json = json.dumps(obj.bbox)
        return format_html(
            '<div class="visual-crop-editor" data-page-width="{}" data-page-height="{}" '
            'data-saved-bbox="{}" data-preview-url="{}">'
            '<p>Drag inside the red box to move it. Drag an edge or corner to include clipped labels.</p>'
            '<div class="visual-crop-stage"><img class="visual-source-page" src="{}" alt="Original page {}">'
            '<div class="visual-crop-selection" aria-label="Selected crop">'
            '<button type="button" class="visual-crop-handle n" data-edge="n" aria-label="Resize top"></button>'
            '<button type="button" class="visual-crop-handle ne" data-edge="ne" aria-label="Resize top right"></button>'
            '<button type="button" class="visual-crop-handle e" data-edge="e" aria-label="Resize right"></button>'
            '<button type="button" class="visual-crop-handle se" data-edge="se" aria-label="Resize bottom right"></button>'
            '<button type="button" class="visual-crop-handle s" data-edge="s" aria-label="Resize bottom"></button>'
            '<button type="button" class="visual-crop-handle sw" data-edge="sw" aria-label="Resize bottom left"></button>'
            '<button type="button" class="visual-crop-handle w" data-edge="w" aria-label="Resize left"></button>'
            '<button type="button" class="visual-crop-handle nw" data-edge="nw" aria-label="Resize top left"></button>'
            '</div></div>'
            '<button type="button" class="button visual-crop-reset">Reset crop</button>'
            '<span class="visual-crop-save-hint">Crop changes are rendered from the original PDF when saved.</span>'
            '</div>',
            page_width,
            page_height,
            bbox_json,
            preview_url,
            preview_url,
            obj.page_number,
        )

    def source_page_preview(self, request, object_id):
        visual = self.get_object(request, object_id)
        if not visual:
            raise Http404("Visual candidate not found.")
        if not self.has_view_or_change_permission(request, visual):
            raise PermissionDenied
        try:
            source, page = _open_visual_source_page(visual)
            try:
                page_image = page.get_pixmap(matrix=fitz.Matrix(1.2, 1.2), alpha=False).tobytes("png")
            finally:
                source.close()
        except (OSError, ValueError, fitz.FileDataError) as exc:
            raise Http404("Could not render the original source page.") from exc
        response = HttpResponse(page_image, content_type="image/png")
        response["Cache-Control"] = "private, no-store"
        return response

    @staticmethod
    def _render_crop(visual, bbox):
        try:
            source, page = _open_visual_source_page(visual)
        except (OSError, ValueError, fitz.FileDataError) as exc:
            raise ValidationError(f"Could not read the source PDF: {exc}") from exc
        try:
            rect = fitz.Rect(bbox)
            if not page.rect.contains(rect) or rect.width < 20 or rect.height < 20:
                raise ValidationError("The crop rectangle must be inside the source page and at least 20 points wide and high.")
            return page.get_pixmap(matrix=fitz.Matrix(2, 2), clip=rect, alpha=False).tobytes("jpeg")
        finally:
            source.close()

    @admin.display(description="Text before and after figure")
    def neighboring_text(self, obj):
        metadata = obj.extracted_content if isinstance(obj.extracted_content, dict) else {}
        return format_html(
            "<strong>Before</strong><pre>{}</pre><strong>After</strong><pre>{}</pre>",
            metadata.get("context_before", ""),
            metadata.get("context_after", ""),
        )

    def save_model(self, request, obj, form, change):
        crop_bytes = self._render_crop(obj, obj.bbox) if change and "bbox" in form.changed_data else None
        metadata = dict(obj.extracted_content) if isinstance(obj.extracted_content, dict) else {}
        if obj.status == "approved":
            if not obj.reviewed_topic_id or obj.reviewed_topic.course_id != obj.document.course_id:
                raise forms.ValidationError("Choose a topic from this document's course before approving.")
            metadata.update({
                "auto_topic": obj.reviewed_topic.title,
                "auto_decision": "tutor_approved",
                "auto_match_method": "tutor_review",
            })
            obj.reviewed_by = request.user
            obj.reviewed_at = timezone.now()
        elif obj.status == "rejected":
            metadata.update({
                "auto_decision": "tutor_rejected",
                "auto_match_method": "tutor_review",
            })
            obj.reviewed_by = request.user
            obj.reviewed_at = timezone.now()
        else:
            if metadata.get("auto_decision") in {"tutor_approved", "tutor_rejected"}:
                metadata.pop("auto_decision", None)
                metadata["auto_match_method"] = "tutor_review_reopened"
            obj.reviewed_by = None
            obj.reviewed_at = None
        obj.extracted_content = metadata
        super().save_model(request, obj, form, change)
        if crop_bytes:
            original_path = Path(obj.crop.name)
            obj.crop.save(
                f"{original_path.stem}-edited-{uuid4().hex[:8]}.jpg",
                ContentFile(crop_bytes),
                save=False,
            )
            obj.save(update_fields=["crop", "updated_at"])


@admin.register(PrepPaper)
class PrepPaperAdmin(admin.ModelAdmin):
    """CAT & Past Examination Papers management."""
    list_display = ("id", "course_badge", "title", "year", "total_marks", "questions_count", "publication_badge", "created_at")
    list_filter = ("is_published", "course__category", "course")
    search_fields = ("title", "course__code", "course__title", "year")
    inlines = [PrepQuestionInline]
    actions = ["publish_papers", "unpublish_papers"]

    def course_badge(self, obj):
        return format_html(
            '<span style="font-weight:700; color:#0f766e;">{}</span> - {}',
            obj.course.code,
            obj.course.title,
        )
    course_badge.short_description = "Course"

    def publication_badge(self, obj):
        if obj.is_published:
            return format_html('<span style="color:#16a34a; font-weight:700; background:#dcfce7; padding:2px 8px; border-radius:10px;">✓ Published</span>')
        return format_html('<span style="color:#64748b; font-weight:700; background:#f1f5f9; padding:2px 8px; border-radius:10px;">Draft</span>')
    publication_badge.short_description = "Status"
    publication_badge.admin_order_field = "is_published"

    def questions_count(self, obj):
        count = obj.questions.count()
        return format_html('<strong>{}</strong> questions', count)
    questions_count.short_description = "Questions"

    @admin.action(description="✓ Publish Selected Papers to Live Catalog")
    def publish_papers(self, request, queryset):
        count = queryset.update(is_published=True)
        self.message_user(request, f"{count} paper(s) published to live course catalog.")

    @admin.action(description="✕ Unpublish Selected Papers (Move to Draft)")
    def unpublish_papers(self, request, queryset):
        count = queryset.update(is_published=False)
        self.message_user(request, f"{count} paper(s) moved to Draft.")


@admin.register(PrepQuestion)
class PrepQuestionAdmin(admin.ModelAdmin):
    """Mathematical question bank with LaTeX preview and Tutor verification."""
    list_display = (
        "id_display",
        "parent_paper_or_topic",
        "marks",
        "topic_label",
        "verification_badge",
        "question_snippet",
        "verified_by",
        "created_at",
    )
    list_filter = ("verification_status", "paper__course", "paper", "topic")
    search_fields = ("question_latex", "solution_latex", "topic_label", "paper__title")
    readonly_fields = (
        "source_document",
        "source_page_number",
        "extraction_confidence",
        "reconstructed_from",
        "reconstruction_metadata",
    )
    actions = ["verify_questions", "flag_questions", "mark_pending"]

    fieldsets = (
        ("Assessment Attachment", {
            "fields": (
                ("paper", "topic"),
                ("number", "marks", "topic_label"),
            )
        }),
        ("Mathematical LaTeX Statement & Derivation", {
            "fields": (
                "question_latex",
                "solution_latex",
            ),
            "description": "Enter clean LaTeX formulas (e.g. $B_r(x)$, \\mathbb{R}^n, \\int_0^\\infty).",
        }),
        ("Source & Reconstruction Provenance", {
            "fields": (
                "source_document",
                "source_page_number",
                "extraction_confidence",
                "reconstructed_from",
                "reconstruction_metadata",
            ),
            "classes": ("collapse",),
        }),
        ("Tutor / SymPy Verification Status", {
            "fields": (
                "verification_status",
                "verified_by",
            )
        }),
    )

    def id_display(self, obj):
        return f"Q{obj.number}"
    id_display.short_description = "Q#"

    def parent_paper_or_topic(self, obj):
        if obj.paper:
            return format_html('<strong>{}</strong>: {}', obj.paper.course.code, obj.paper.title[:30])
        elif obj.topic:
            return format_html('<strong>{}</strong>: {}', obj.topic.course.code, obj.topic.title[:30])
        return "Independent Question"
    parent_paper_or_topic.short_description = "Context"

    def verification_badge(self, obj):
        badges = {
            "verified": ("#16a34a", "#dcfce7", "✓ Verified (Tutor/SymPy)"),
            "auto_validated": ("#0369a1", "#e0f2fe", "✓ Auto-validated source extraction"),
            "reconstructed": ("#7c3aed", "#ede9fe", "↻ AI-reconstructed (confidence checked)"),
            "pending": ("#d97706", "#fef3c7", "⏳ Pending Review"),
            "flagged": ("#dc2626", "#fee2e2", "⚠ Flagged for Correction"),
        }
        color, bg, label = badges.get(obj.verification_status, ("#64748b", "#f1f5f9", obj.verification_status))
        return format_html(
            '<span style="font-size:0.75rem; font-weight:700; color:{}; background:{}; padding:2px 8px; border-radius:10px; border:1px solid {};">{}</span>',
            color, bg, color, label
        )
    verification_badge.short_description = "Verification"
    verification_badge.admin_order_field = "verification_status"

    def question_snippet(self, obj):
        snippet = obj.question_latex[:85]
        if len(obj.question_latex) > 85:
            snippet += "..."
        return snippet
    question_snippet.short_description = "Problem Statement"

    @admin.action(description="✓ Mark Selected Questions as Verified (Tutor / SymPy Approved)")
    def verify_questions(self, request, queryset):
        count = 0
        for question in queryset:
            question.verification_status = "verified"
            question.verified_by = request.user
            if question.question_type == "adapted":
                metadata = question.reconstruction_metadata if isinstance(question.reconstruction_metadata, dict) else {}
                question.reconstruction_metadata = {
                    **metadata,
                    "review_status": "approved",
                    "reviewed_by": str(request.user.pk),
                    "reviewed_at": timezone.now().isoformat(),
                }
            question.save(update_fields=["verification_status", "verified_by", "reconstruction_metadata"])
            count += 1
        self.message_user(request, f"Marked {count} question(s) as officially verified.")

    @admin.action(description="⚠ Flag Selected Questions for Mathematical Correction")
    def flag_questions(self, request, queryset):
        count = 0
        for question in queryset:
            question.verification_status = "flagged"
            if question.question_type == "adapted":
                metadata = question.reconstruction_metadata if isinstance(question.reconstruction_metadata, dict) else {}
                question.reconstruction_metadata = {**metadata, "review_status": "needs_correction"}
            question.save(update_fields=["verification_status", "reconstruction_metadata"])
            count += 1
        self.message_user(request, f"Flagged {count} question(s) for correction.")

    @admin.action(description="⏳ Move to Pending Verification")
    def mark_pending(self, request, queryset):
        count = 0
        for question in queryset:
            question.verification_status = "pending"
            if question.question_type == "adapted":
                metadata = question.reconstruction_metadata if isinstance(question.reconstruction_metadata, dict) else {}
                question.reconstruction_metadata = {**metadata, "review_status": "pending"}
            question.save(update_fields=["verification_status", "reconstruction_metadata"])
            count += 1
        self.message_user(request, f"Moved {count} question(s) to pending review.")


@admin.register(PrepCourse)
class PrepCourseAdmin(admin.ModelAdmin):
    """Canonical syllabus course units."""
    list_display = ("code", "title", "category", "level", "topics_count", "papers_count", "is_active", "created_at")
    list_filter = ("category", "level", "is_active")
    search_fields = ("code", "title", "description")
    prepopulated_fields = {"slug": ("code",)}
    ordering = ("code",)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            _topics_count=Count("topics", distinct=True),
            _papers_count=Count("papers", distinct=True),
        )

    def topics_count(self, obj):
        return obj._topics_count
    topics_count.short_description = "Topics"

    def papers_count(self, obj):
        return obj._papers_count
    papers_count.short_description = "Papers"


@admin.register(PrepCourseEnrollment)
class PrepCourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "source", "created_at")
    list_filter = ("source", "created_at")
    search_fields = ("user__email", "course__code", "course__title")


@admin.register(PrepTopic)
class PrepTopicAdmin(admin.ModelAdmin):
    """Syllabus topics with LaTeX summaries."""
    list_display = ("course", "order", "title", "questions_count", "slug", "created_at")
    list_filter = ("course__category", "course")
    search_fields = ("title", "summary", "course__code", "course__title")
    ordering = ("course", "order")

    def questions_count(self, obj):
        return obj.questions.count()
    questions_count.short_description = "Questions"


@admin.register(PrepContentUpdate)
class PrepContentUpdateAdmin(admin.ModelAdmin):
    """Review additive course updates proposed from newly uploaded material."""
    list_display = ("document", "topic", "update_type", "status", "created_at", "reviewed_at")
    list_filter = ("status", "update_type", "document__course")
    search_fields = ("document__course__code", "document__course__title", "topic__title", "rationale")
    readonly_fields = ("document", "topic", "update_type", "proposed_data", "rationale", "created_at")
    actions = ("approve_summary_addenda", "approve_course_profiles", "reject_selected_updates",)

    @admin.action(description="Approve selected summary proposals as addenda")
    def approve_summary_addenda(self, request, queryset):
        now = timezone.now()
        applied = 0
        for update in queryset.filter(status="pending", update_type="summary_review").select_related("topic"):
            if not update.topic:
                continue
            summary = str((update.proposed_data or {}).get("summary") or "").strip()
            if not summary:
                continue
            existing = update.topic.summary.strip()
            if summary.casefold() not in existing.casefold():
                update.topic.summary = f"{existing}\n\n{summary}".strip()
                update.topic.save(update_fields=["summary"])
            update.status = "approved"
            update.reviewed_by = request.user
            update.reviewed_at = now
            update.save(update_fields=["status", "reviewed_by", "reviewed_at"])
            applied += 1
        self.message_user(request, f"Applied {applied} summary addendum(s).")

    @admin.action(description="Approve selected AI course profiles from notes")
    def approve_course_profiles(self, request, queryset):
        now = timezone.now()
        applied = 0
        for update in queryset.filter(status="pending", update_type="course_profile").select_related(
            "document__course"
        ):
            data = update.proposed_data if isinstance(update.proposed_data, dict) else {}
            if not _apply_approved_course_profile(update.document, data):
                continue
            update.status = "approved"
            update.reviewed_by = request.user
            update.reviewed_at = now
            update.save(update_fields=["status", "reviewed_by", "reviewed_at"])
            applied += 1
        self.message_user(request, f"Applied {applied} source-grounded course profile(s).")

    @admin.action(description="Reject selected content update proposals")
    def reject_selected_updates(self, request, queryset):
        count = queryset.filter(status="pending").update(
            status="rejected",
            reviewed_by=request.user,
            reviewed_at=timezone.now(),
        )
        self.message_user(request, f"Rejected {count} content update proposal(s).")


@admin.register(PrepContentCache)
class PrepContentCacheAdmin(admin.ModelAdmin):
    """Zero-marginal cost database cache."""
    list_display = ("cache_key", "content_type", "course", "topic", "hit_count", "created_at", "updated_at")
    list_filter = ("content_type", "course")
    search_fields = ("cache_key", "prompt_hash")
    readonly_fields = ("created_at", "updated_at")


@admin.register(PrepNoteGenerationGuard)
class PrepNoteGenerationGuardAdmin(admin.ModelAdmin):
    list_display = ("topic", "level", "status", "failed_attempts", "last_failed_at", "updated_at")
    list_filter = ("status", "level", "topic__course")
    search_fields = ("topic__title", "topic__course__code", "source_signature", "last_error")
    readonly_fields = ("topic", "level", "source_signature", "failed_attempts", "last_error", "last_failed_at", "notification_sent_at", "created_at", "updated_at")
    actions = ("reset_generation_guards",)

    @admin.action(description="Allow another validated note generation attempt")
    def reset_generation_guards(self, request, queryset):
        guards = list(queryset.values("topic_id", "level", "source_signature"))
        count = queryset.update(status="open", failed_attempts=0, last_error="", last_failed_at=None, notification_sent_at=None)
        for guard in guards:
            PrepNoteRepair.objects.filter(
                topic_id=guard["topic_id"],
                level=guard["level"],
                source_signature=guard["source_signature"],
                status="needs_review",
            ).update(status="open", attempts=0, last_error="")
        self.message_user(request, f"Reset {count} note generation guard(s).")


@admin.register(PrepNoteRepair)
class PrepNoteRepairAdmin(admin.ModelAdmin):
    list_display = ("topic", "level", "status", "attempts", "updated_at")
    list_filter = ("status", "level", "topic__course")
    search_fields = ("topic__title", "topic__course__code", "source_signature", "last_error")
    readonly_fields = (
        "topic", "level", "source_signature", "cache_key", "original_content",
        "current_content", "validation_issues", "attempts", "created_at", "updated_at",
    )


@admin.register(PrepWallet)
class PrepWalletAdmin(admin.ModelAdmin):
    """Student wallets & monthly plans."""
    list_display = ("user_display", "credits_balance", "current_plan", "plan_expires_at", "updated_at")
    list_filter = ("current_plan",)
    search_fields = ("user__email", "user__first_name", "user__last_name")
    actions = ["grant_100_credits", "grant_500_credits", "upgrade_to_pro"]

    def user_display(self, obj):
        return f"{obj.user.get_full_name() or obj.user.email} ({obj.user.email})"
    user_display.short_description = "User"

    @admin.action(description="⚡ Grant +100 Exam Credits to Selected Wallets")
    def grant_100_credits(self, request, queryset):
        for wallet in queryset:
            grant_credits(
                wallet,
                100,
                source="admin",
                action_type="monthly_grant",
                description="Admin promotional credit grant (+100 credits)",
            )
        self.message_user(request, f"Granted +100 credits to {queryset.count()} wallet(s).")

    @admin.action(description="⚡ Grant +500 Exam Credits to Selected Wallets")
    def grant_500_credits(self, request, queryset):
        for wallet in queryset:
            grant_credits(
                wallet,
                500,
                source="admin",
                action_type="monthly_grant",
                description="Admin promotional credit grant (+500 credits)",
            )
        self.message_user(request, f"Granted +500 credits to {queryset.count()} wallet(s).")

    @admin.action(description="★ Upgrade Selected Users to Pro (Exam Pass)")
    def upgrade_to_pro(self, request, queryset):
        count = 0
        for wallet in queryset:
            grant_subscription(wallet, "pro", 650, reference_code="ADMIN-PRO-GRANT")
            count += 1
        self.message_user(request, f"Upgraded {count} user(s) to Pro Plan.")


@admin.register(PrepTransaction)
class PrepTransactionAdmin(admin.ModelAdmin):
    """Credit ledger audit trail."""
    list_display = ("wallet_user", "action_type", "amount_badge", "reference_code", "description", "created_at")
    list_filter = ("action_type", "created_at")
    search_fields = ("wallet__user__email", "reference_code", "description")

    def wallet_user(self, obj):
        return obj.wallet.user.email
    wallet_user.short_description = "User"

    def amount_badge(self, obj):
        if obj.amount > 0:
            return format_html('<span style="color:#16a34a; font-weight:700;">+{} credits</span>', obj.amount)
        return format_html('<span style="color:#dc2626; font-weight:700;">{} credits</span>', obj.amount)
    amount_badge.short_description = "Amount"


@admin.register(PrepCreditGrant)
class PrepCreditGrantAdmin(admin.ModelAdmin):
    """Inspect dated credit lots and their remaining balances."""
    list_display = (
        "wallet_user",
        "source",
        "granted_credits",
        "remaining_credits",
        "granted_at",
        "expires_at",
        "reference_code",
    )
    list_filter = ("source", "expires_at")
    search_fields = ("wallet__user__email", "reference_code")
    readonly_fields = ("created_at",)

    def wallet_user(self, obj):
        return obj.wallet.user.email
    wallet_user.short_description = "User"


@admin.register(PrepHistory)
class PrepHistoryAdmin(admin.ModelAdmin):
    """User revision history entries."""
    list_display = ("user", "title", "course_code", "item_type", "created_at")
    list_filter = ("item_type", "course_code")
    search_fields = ("user__email", "title", "course_code")


@admin.register(PrepNotification)
class PrepNotificationAdmin(admin.ModelAdmin):
    """Student live review & document notifications."""
    list_display = ("user", "title", "category", "is_read", "created_at")
    list_filter = ("category", "is_read", "created_at")
    search_fields = ("user__email", "title", "message")
