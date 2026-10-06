import uuid
from django.db import models
from django.conf import settings
from django.utils.text import slugify


class PrepCourse(models.Model):
    """Canonical course unit with syllabus structure and past papers."""
    code = models.CharField(max_length=50, unique=True, db_index=True, help_text="e.g. SMA 300")
    title = models.CharField(max_length=200, help_text="e.g. Real Analysis I")
    slug = models.SlugField(max_length=100, unique=True)
    category = models.CharField(
        max_length=100,
        choices=[
            ("Mathematics", "Mathematics"),
            ("Statistics", "Statistics"),
            ("Computing", "Computing"),
            ("Engineering", "Engineering"),
            ("Chemistry", "Chemistry"),
            ("Physics", "Physics"),
            ("Social Sciences", "Social Sciences"),
            ("Humanities", "Humanities"),
            ("Business & Economics", "Business & Economics"),
            ("General Sciences", "General Sciences"),
            ("Other", "Other"),
        ],
        default="Mathematics",
    )
    level = models.CharField(max_length=100, default="Undergraduate")
    description = models.TextField(blank=True, help_text="Canonical course objectives, syllabus scope, and references.")
    study_profile = models.JSONField(default=dict, blank=True, help_text="Tutor-approved, source-grounded subject rules for notes and topics.")
    study_profile_version = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["code"]
        verbose_name = "Prep Course"
        verbose_name_plural = "Prep Courses"

    def __str__(self):
        return f"{self.code} - {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.code)
        super().save(*args, **kwargs)


class PrepCourseEnrollment(models.Model):
    """A user's personal dashboard list of shared catalogue courses."""
    SOURCE_CHOICES = [
        ("catalog", "Added from Catalog"),
        ("upload", "Created by Upload"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="prep_course_enrollments")
    course = models.ForeignKey(PrepCourse, on_delete=models.CASCADE, related_name="enrollments")
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default="catalog")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(fields=["user", "course"], name="unique_prep_course_enrollment"),
        ]

    def __str__(self):
        return f"{self.user} added {self.course.code}"


class PrepCourseSharedCost(models.Model):
    """A source upload or generated note cost shared by a course's catalog members."""
    COST_TYPES = [
        ("upload", "Course Resource Upload"),
        ("topic_notes", "AI Topic Notes"),
    ]

    course = models.ForeignKey(PrepCourse, on_delete=models.CASCADE, related_name="shared_costs")
    cost_type = models.CharField(max_length=20, choices=COST_TYPES, db_index=True)
    document = models.ForeignKey(
        "PrepDocument", on_delete=models.SET_NULL, null=True, blank=True, related_name="shared_costs"
    )
    topic = models.ForeignKey(
        "PrepTopic", on_delete=models.SET_NULL, null=True, blank=True, related_name="shared_costs"
    )
    level = models.CharField(max_length=20, blank=True)
    source_transaction = models.OneToOneField(
        "PrepTransaction", on_delete=models.SET_NULL, null=True, blank=True, related_name="shared_course_cost"
    )
    source_key = models.CharField(max_length=255, unique=True)
    total_credits = models.PositiveIntegerField()
    per_student_credits = models.PositiveIntegerField()
    member_count_at_creation = models.PositiveIntegerField(default=0)
    usage = models.JSONField(default=dict, blank=True)
    model_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at", "id"]

    def __str__(self):
        return f"{self.course.code} {self.cost_type}: {self.total_credits} credits"


class PrepCourseCostShare(models.Model):
    """A learner's payable share for one shared course cost."""
    cost = models.ForeignKey(PrepCourseSharedCost, on_delete=models.CASCADE, related_name="shares")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="prep_course_cost_shares")
    required_credits = models.PositiveIntegerField()
    paid_credits = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    settled_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["cost", "user"], name="unique_prep_course_cost_share"),
        ]
        ordering = ["cost__created_at", "cost_id"]

    @property
    def is_settled(self):
        return self.paid_credits >= self.required_credits


class PrepNotePrecomputeJob(models.Model):
    """Durable queue item for preparing shared Level 2 notes after publication."""
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("running", "Running"),
        ("complete", "Complete"),
        ("failed", "Failed"),
    ]

    course = models.ForeignKey(PrepCourse, on_delete=models.CASCADE, related_name="note_precompute_jobs")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", db_index=True)
    attempts = models.PositiveIntegerField(default=0)
    last_error = models.TextField(blank=True)
    queued_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["course"],
                name="unique_prep_note_precompute_course",
            ),
        ]
        ordering = ["queued_at", "id"]


class PrepTopicNotesJob(models.Model):
    """Durable per-topic notes generation, processed outside web requests."""

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("running", "Running"),
        ("complete", "Complete"),
        ("failed", "Failed"),
    ]

    topic = models.ForeignKey(
        "PrepTopic",
        on_delete=models.CASCADE,
        related_name="notes_generation_jobs",
    )
    level = models.CharField(max_length=20)
    source_signature = models.CharField(max_length=64, db_index=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", db_index=True)
    attempts = models.PositiveSmallIntegerField(default=0)
    last_error = models.TextField(blank=True)
    queued_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["topic", "level", "source_signature"],
                name="unique_prep_topic_notes_job",
            ),
        ]
        ordering = ["queued_at", "id"]


class PrepTopic(models.Model):
    """Syllabus module/topic under a canonical course."""
    course = models.ForeignKey(PrepCourse, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    order = models.PositiveIntegerField(default=1)
    summary = models.TextField(blank=True, help_text="LaTeX notes, fundamental theorems, and core formulas.")
    subtopics = models.JSONField(default=list, blank=True, help_text="Ordered list of subtopics under this unit.")
    content_rules = models.JSONField(default=dict, blank=True, help_text="Reviewer-approved, source-grounded modality rules for this topic.")
    content_rules_version = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["course", "order", "id"]
        unique_together = ("course", "slug")
        verbose_name = "Prep Topic"
        verbose_name_plural = "Prep Topics"

    def __str__(self):
        return f"{self.course.code}: Topic {self.order} - {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"topic-{self.order}-{self.title[:30]}")
        update_fields = kwargs.get("update_fields")
        if self.pk and (update_fields is None or "content_rules" in update_fields):
            previous_rules = type(self).objects.filter(pk=self.pk).values_list("content_rules", flat=True).first()
            if previous_rules is not None and previous_rules != (self.content_rules or {}):
                self.content_rules_version += 1
                if update_fields is not None:
                    kwargs["update_fields"] = set(update_fields) | {"content_rules_version"}
        super().save(*args, **kwargs)


class PrepTopicChatSession(models.Model):
    """A learner's persistent, topic-scoped study conversation."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="prep_topic_chat_sessions")
    topic = models.ForeignKey(PrepTopic, on_delete=models.CASCADE, related_name="chat_sessions")
    title = models.CharField(max_length=160, default="Topic study chat")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at", "-id"]


class PrepTopicChatMessage(models.Model):
    """One bounded learner/assistant turn retained for the topic history panel."""
    ROLES = [("user", "Learner"), ("assistant", "Assistant")]

    session = models.ForeignKey(PrepTopicChatSession, on_delete=models.CASCADE, related_name="messages")
    role = models.CharField(max_length=20, choices=ROLES)
    content = models.TextField()
    input_tokens = models.PositiveIntegerField(default=0)
    output_tokens = models.PositiveIntegerField(default=0)
    credits_charged = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at", "id"]


class PrepTopicChatUpload(models.Model):
    """Validated text extracted from a learner upload available to one chat."""
    session = models.ForeignKey(PrepTopicChatSession, on_delete=models.CASCADE, related_name="uploads")
    message = models.ForeignKey(
        PrepTopicChatMessage,
        on_delete=models.CASCADE,
        related_name="uploads",
        null=True,
        blank=True,
    )
    original_name = models.CharField(max_length=255)
    extracted_text = models.TextField()
    page_count = models.PositiveIntegerField(default=1)
    source_type = models.CharField(max_length=30, default="text_pdf")
    created_at = models.DateTimeField(auto_now_add=True)


class PrepDocument(models.Model):
    """Raw uploaded document (notes or CAT papers) progressing through the 3-stage pipeline."""
    DOC_TYPES = [
        ("Lecture Notes", "Lecture Notes / Module"),
        ("Continuous Assessment Test (CAT)", "Continuous Assessment Test (CAT)"),
        ("Final Examination Paper", "Final Examination Past Paper"),
        ("Revision Sheet", "Revision Exercises / Tutorial"),
    ]

    STAGES = [
        ("stage_1", "Stage 1: Ingestion & Extraction"),
        ("stage_2", "Stage 2: Tutor Review Gate"),
        ("stage_3", "Stage 3: Published"),
        ("rejected", "Rejected"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="prep_documents",
    )
    course = models.ForeignKey(PrepCourse, on_delete=models.CASCADE, related_name="documents")
    doc_type = models.CharField(max_length=60, choices=DOC_TYPES, default="Lecture Notes")
    academic_year = models.CharField(max_length=100, blank=True, help_text="e.g. 2024/2025 Semester 1")
    topic_name = models.CharField(max_length=255, blank=True, help_text="Topic or unit covered")
    file = models.FileField(upload_to="prep/documents/%Y/%m/")
    file_size_bytes = models.PositiveIntegerField(default=0)
    github_raw_url = models.URLField(max_length=500, blank=True, help_text="Raw GitHub permanent reference URL")
    extracted_text = models.TextField(blank=True, help_text="Extracted plain text or structured LaTeX")
    page_evidence = models.JSONField(default=list, blank=True)
    validation_report = models.JSONField(default=dict, blank=True)
    file_sha256 = models.CharField(max_length=64, blank=True, db_index=True)
    text_sha256 = models.CharField(max_length=64, blank=True, db_index=True)
    is_duplicate = models.BooleanField(default=False, db_index=True)
    duplicate_of = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="duplicate_documents",
    )
    stage = models.CharField(max_length=20, choices=STAGES, default="stage_1", db_index=True)
    tutor_review_notes = models.TextField(blank=True, help_text="Feedback or corrections from tutor review gate")
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_prep_documents",
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Prep Document"
        verbose_name_plural = "Prep Documents"

    def __str__(self):
        return f"{self.course.code} - {self.doc_type} ({self.get_stage_display()})"


class PrepDocumentVisual(models.Model):
    """A source-page visual candidate and its bounded, optional inspection result."""
    VISUAL_TYPES = [
        ("graph", "Graph or Plot"),
        ("diagram", "Diagram or Flowchart"),
        ("table", "Table"),
        ("illustration", "Illustration"),
        ("unclassified", "Unclassified Visual"),
    ]
    STATUSES = [
        ("candidate", "Candidate Captured"),
        ("inspected", "Vision Inspected"),
        ("needs_review", "Needs Review"),
        ("approved", "Tutor Approved"),
        ("rejected", "Rejected as Irrelevant"),
        ("error", "Inspection Error"),
    ]

    document = models.ForeignKey(PrepDocument, on_delete=models.CASCADE, related_name="visual_candidates")
    candidate_key = models.CharField(max_length=64, unique=True, db_index=True)
    page_number = models.PositiveIntegerField(db_index=True)
    bbox = models.JSONField(default=list, help_text="Crop bounds in PDF points: [x0, y0, x1, y1].")
    candidate_reasons = models.JSONField(default=list, blank=True)
    context_text = models.TextField(blank=True)
    crop = models.FileField(upload_to="prep/visual-crops/%Y/%m/", blank=True)
    context_crop = models.FileField(upload_to="prep/visual-context/%Y/%m/", blank=True)
    visual_type = models.CharField(max_length=20, choices=VISUAL_TYPES, default="unclassified")
    labels = models.JSONField(default=list, blank=True)
    extracted_content = models.JSONField(default=dict, blank=True)
    reconstruction_proposal = models.JSONField(default=dict, blank=True)
    confidence = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUSES, default="candidate", db_index=True)
    reviewed_topic = models.ForeignKey(
        PrepTopic,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_visual_candidates",
    )
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_prep_visuals",
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    review_notes = models.TextField(blank=True)
    vision_model = models.CharField(max_length=120, blank=True)
    vision_usage = models.JSONField(default=dict, blank=True)
    inspection_error = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["document", "page_number", "id"]
        indexes = [models.Index(fields=["document", "page_number", "status"])]

    def __str__(self):
        return f"{self.document.course.code}: page {self.page_number} {self.visual_type}"


class PrepContentUpdate(models.Model):
    """A reviewable proposal to enrich, not overwrite, the shared course graph."""
    UPDATE_TYPES = [
        ("course_profile", "Course Study Profile"),
        ("topic_content_rules", "Topic Content Rules"),
        ("new_topic", "New Topic"),
        ("add_subtopics", "Add Missing Subtopics"),
        ("fill_summary", "Fill Missing Topic Summary"),
        ("summary_review", "Possible Summary Improvement"),
        ("topic_conflict", "Conflicting Topic Identity"),
    ]
    STATUS_CHOICES = [
        ("pending", "Pending Review"),
        ("approved", "Approved and Applied"),
        ("rejected", "Rejected"),
    ]

    document = models.ForeignKey(PrepDocument, on_delete=models.CASCADE, related_name="content_updates")
    topic = models.ForeignKey(PrepTopic, on_delete=models.SET_NULL, null=True, blank=True, related_name="content_updates")
    update_type = models.CharField(max_length=30, choices=UPDATE_TYPES)
    proposed_data = models.JSONField(default=dict)
    rationale = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", db_index=True)
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviewed_prep_content_updates",
    )
    reviewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["status", "created_at"]

    def __str__(self):
        target = self.topic.title if self.topic else self.proposed_data.get("title", "New topic")
        return f"{self.document.course.code}: {self.get_update_type_display()} - {target}"


class PrepPaper(models.Model):
    """Structured CAT or examination paper organized by course."""
    id = models.SlugField(primary_key=True, max_length=120)
    course = models.ForeignKey(PrepCourse, on_delete=models.CASCADE, related_name="papers")
    title = models.CharField(max_length=255, help_text="e.g. Continuous Assessment Test 1 (CAT 1)")
    year = models.CharField(max_length=100, help_text="e.g. 2024/2025 Semester 1")
    total_marks = models.PositiveIntegerField(default=30)
    source_document = models.ForeignKey(
        PrepDocument,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="derived_papers",
    )
    is_published = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["course", "-created_at"]
        verbose_name = "Prep Paper"
        verbose_name_plural = "Prep Papers"

    def __str__(self):
        return f"{self.course.code}: {self.title} ({self.year})"


class PrepQuestion(models.Model):
    """Structured, verified mathematical question belonging to a CAT paper or topic."""
    VERIFICATION_CHOICES = [
        ("pending", "Pending Verification"),
        ("verified", "Verified (Tutor / SymPy)"),
        ("auto_validated", "Auto-validated source extraction"),
        ("reconstructed", "AI-reconstructed equivalent"),
        ("flagged", "Flagged for Correction"),
    ]
    LEARNER_VISIBLE_STATUSES = ("verified", "auto_validated", "reconstructed")
    ANSWERABLE_STATUSES = ("verified", "auto_validated", "reconstructed")

    QUESTION_TYPES = [
        ("authentic", "Authentic Past Paper"),
        ("adapted", "Adapted Past Paper"),
        ("generated", "AI Generated Variant"),
    ]

    paper = models.ForeignKey(PrepPaper, on_delete=models.SET_NULL, null=True, blank=True, related_name="questions")
    topic = models.ForeignKey(PrepTopic, on_delete=models.SET_NULL, null=True, blank=True, related_name="questions")
    source_document = models.ForeignKey(
        PrepDocument,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sourced_questions",
    )
    source_page_number = models.PositiveIntegerField(null=True, blank=True)
    extraction_confidence = models.FloatField(null=True, blank=True)
    reconstructed_from = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="adapted_reconstructions",
    )
    reconstruction_metadata = models.JSONField(default=dict, blank=True)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default="authentic", db_index=True)
    number = models.PositiveIntegerField(default=1)
    marks = models.PositiveIntegerField(default=10)
    topic_label = models.CharField(max_length=150, blank=True, help_text="Topic badge label e.g. Metric Spaces")
    question_latex = models.TextField(help_text="LaTeX formatted problem statement")
    solution_latex = models.TextField(blank=True, help_text="LaTeX step-by-step verified derivation and proof")
    verification_status = models.CharField(max_length=20, choices=VERIFICATION_CHOICES, default="verified")
    verified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="verified_prep_questions",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["paper", "number", "id"]
        verbose_name = "Prep Question"
        verbose_name_plural = "Prep Questions"

    def __str__(self):
        parent = self.paper.title if self.paper else (self.topic.title if self.topic else "General")
        return f"Q{self.number} ({self.marks}m) - {parent}"


class PrepContentCache(models.Model):
    """
    Zero-marginal-cost content cache.
    Stores pre-generated/verified solutions and notes to prevent duplicate LLM calls
    and protect against excessive API token consumption.
    """
    cache_key = models.CharField(max_length=255, unique=True, db_index=True)
    course = models.ForeignKey(PrepCourse, on_delete=models.CASCADE, null=True, blank=True, related_name="cached_contents")
    topic = models.ForeignKey(PrepTopic, on_delete=models.CASCADE, null=True, blank=True, related_name="cached_contents")
    content_type = models.CharField(max_length=50, help_text="e.g. topic_notes, solution_derivation, practice_set")
    prompt_hash = models.CharField(max_length=64, db_index=True)
    payload = models.JSONField(default=dict)
    hit_count = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Prep Content Cache"
        verbose_name_plural = "Prep Content Caches"

    def __str__(self):
        return f"Cache [{self.content_type}] {self.cache_key} (Hits: {self.hit_count})"


class PrepNoteGenerationGuard(models.Model):
    """Stops repeated provider spend when one topic/level cannot validate."""

    STATUS_CHOICES = [
        ("open", "Retry permitted"),
        ("needs_review", "Needs tutor/admin review"),
    ]

    topic = models.ForeignKey(PrepTopic, on_delete=models.CASCADE, related_name="note_generation_guards")
    level = models.CharField(max_length=20)
    source_signature = models.CharField(max_length=64, db_index=True)
    failed_attempts = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open", db_index=True)
    last_error = models.TextField(blank=True)
    last_failed_at = models.DateTimeField(null=True, blank=True)
    notification_sent_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["topic", "level", "source_signature"],
                name="unique_prep_note_generation_guard",
            ),
        ]
        ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.topic} {self.level}: {self.status} ({self.failed_attempts} failures)"


class PrepNoteRepair(models.Model):
    """Quarantined note content and bounded targeted-repair attempts."""

    STATUS_CHOICES = [
        ("open", "Repair Pending"),
        ("validated", "Repair Validated"),
        ("needs_review", "Needs Manual Review"),
    ]

    topic = models.ForeignKey(PrepTopic, on_delete=models.CASCADE, related_name="note_repairs")
    level = models.CharField(max_length=20)
    source_signature = models.CharField(max_length=64, db_index=True)
    cache_key = models.CharField(max_length=255)
    original_content = models.TextField()
    current_content = models.TextField()
    validation_issues = models.JSONField(default=list)
    attempts = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="open", db_index=True)
    last_error = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["topic", "level", "source_signature"],
                name="unique_prep_note_repair",
            ),
        ]
        ordering = ["-updated_at"]

    def __str__(self):
        return f"{self.topic} {self.level}: {self.status} ({self.attempts} attempts)"


class PrepWallet(models.Model):
    """User credit balance and monthly exam readiness plan."""
    PLAN_CHOICES = [
        ("trial", "Free Trial (3 Days)"),
        ("basic", "Basic (Starter Prep)"),
        ("plus", "Plus (Semester Pass)"),
        ("pro", "Pro (Exam Master)"),
        ("expired", "Trial Expired"),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="prep_wallet")
    credits_balance = models.PositiveIntegerField(default=30)
    current_plan = models.CharField(max_length=50, choices=PLAN_CHOICES, default="trial")
    plan_expires_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Prep Wallet"
        verbose_name_plural = "Prep Wallets"

    def __str__(self):
        return f"{self.user} - {self.credits_balance} Credits ({self.current_plan})"

    @classmethod
    def get_or_create_wallet(cls, user):
        """Helper to safely retrieve or create a wallet for a user with default starter balance and 3-day trial."""
        wallet = cls.objects.filter(user=user).first()
        created = False
        if not wallet:
            created = True
            from django.utils import timezone
            from datetime import timedelta
            wallet = cls.objects.create(
                user=user,
                credits_balance=0,
                current_plan="trial",
                plan_expires_at=timezone.now() + timedelta(days=3),
            )
        from services.credit_service import ensure_wallet_credit_state
        ensure_wallet_credit_state(wallet, initialize_trial=created)
        return wallet


class PrepCreditGrant(models.Model):
    """A dated credit lot used to enforce trial, subscription, and top-up expiry."""
    SOURCE_CHOICES = [
        ("trial", "Free Trial"),
        ("subscription", "Subscription Allocation"),
        ("purchased", "Purchased Top-Up"),
        ("admin", "Administrator Grant"),
        ("legacy", "Legacy Balance"),
    ]

    wallet = models.ForeignKey(PrepWallet, on_delete=models.CASCADE, related_name="credit_grants")
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    granted_credits = models.PositiveIntegerField()
    remaining_credits = models.PositiveIntegerField()
    granted_at = models.DateTimeField()
    expires_at = models.DateTimeField(null=True, blank=True)
    reference_code = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["expires_at", "created_at"]
        indexes = [
            models.Index(fields=["wallet", "source", "expires_at"]),
            models.Index(fields=["wallet", "remaining_credits"]),
        ]

    def __str__(self):
        return f"{self.wallet.user} | {self.source} | {self.remaining_credits}/{self.granted_credits}"


class PrepCreditReservation(models.Model):
    """Credits held atomically while a provider request is in flight."""

    STATUS_CHOICES = [
        ("reserved", "Reserved"),
        ("settled", "Settled"),
        ("released", "Released"),
    ]

    wallet = models.ForeignKey(
        PrepWallet,
        on_delete=models.CASCADE,
        related_name="credit_reservations",
    )
    purpose = models.CharField(max_length=50)
    reserved_credits = models.PositiveIntegerField()
    remaining_reserved_credits = models.PositiveIntegerField()
    charged_credits = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="reserved", db_index=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["wallet", "status"], name="prep_res_wallet_status_idx"),
        ]
        ordering = ["created_at", "id"]

    def __str__(self):
        return (
            f"{self.wallet.user} | {self.purpose} | "
            f"{self.remaining_reserved_credits}/{self.reserved_credits} reserved"
        )


class PrepTransaction(models.Model):
    """Audit ledger for credit deductions and M-Pesa top-up purchases."""
    ACTION_CHOICES = [
        ("trial_grant", "3-Day Free Trial Starter Credits"),
        ("upload_text", "Digital Text PDF Upload (2 credits)"),
        ("upload_ocr", "Scanned Vision OCR Ingestion (5 credits)"),
        ("deep_reasoning", "Complex Proof / Derivation (5 credits)"),
        ("ai_practice_gen", "AI Practice Question Generation"),
        ("topic_notes", "AI Topic Notes Generation"),
        ("topic_tutor", "Topic Tutor AI Reply"),
        ("topic_tutor_ocr", "Topic Tutor Upload OCR"),
        ("topup_purchase", "M-Pesa / Paystack Credit Top-Up"),
        ("monthly_grant", "Monthly Plan Credit Allocation"),
        ("credit_expiry", "Expired Credits"),
        ("trial_reminder", "Free Trial Reminder"),
    ]

    wallet = models.ForeignKey(PrepWallet, on_delete=models.CASCADE, related_name="transactions")
    credit_grant = models.ForeignKey(
        PrepCreditGrant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transactions",
    )
    amount = models.IntegerField(help_text="Negative for deductions, positive for top-up credits")
    action_type = models.CharField(max_length=50, choices=ACTION_CHOICES)
    reference_code = models.CharField(max_length=100, blank=True, help_text="e.g. M-Pesa transaction ID / Paystack ref")
    description = models.CharField(max_length=255)
    model_name = models.CharField(max_length=100, blank=True)
    input_tokens = models.PositiveIntegerField(null=True, blank=True)
    output_tokens = models.PositiveIntegerField(null=True, blank=True)
    total_tokens = models.PositiveIntegerField(null=True, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Prep Transaction"
        verbose_name_plural = "Prep Transactions"

    def __str__(self):
        return f"{self.wallet.user} | {self.action_type} | {self.amount:+d} credits"


class PrepHistory(models.Model):
    """Recent student revision history and accessed syllabus items."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="prep_histories")
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=50)
    item_type = models.CharField(max_length=60, help_text="e.g. CAT Paper, Lecture Notes, Topic Revision")
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Prep Revision History"
        verbose_name_plural = "Prep Revision Histories"

    def __str__(self):
        return f"{self.user} - {self.title} ({self.course_code})"


class PrepNotification(models.Model):
    """Live notification for students regarding document reviews, topic indexing, and publications."""
    CATEGORY_CHOICES = [
        ("upload", "Document Uploaded"),
        ("review", "Stage 2: Under Review"),
        ("published", "Stage 3: Approved & Published"),
        ("rejected", "Review Feedback / Rejected"),
        ("general", "General"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="prep_notifications")
    title = models.CharField(max_length=255)
    message = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="general")
    url = models.CharField(max_length=255, blank=True)
    is_read = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Prep Notification"
        verbose_name_plural = "Prep Notifications"

    def __str__(self):
        return f"{self.user} - {self.title} ({'Read' if self.is_read else 'Unread'})"
