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


class PrepTopic(models.Model):
    """Syllabus module/topic under a canonical course."""
    course = models.ForeignKey(PrepCourse, on_delete=models.CASCADE, related_name="topics")
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    order = models.PositiveIntegerField(default=1)
    summary = models.TextField(blank=True, help_text="LaTeX notes, fundamental theorems, and core formulas.")
    subtopics = models.JSONField(default=list, blank=True, help_text="Ordered list of subtopics under this unit.")
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
        super().save(*args, **kwargs)


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


class PrepContentUpdate(models.Model):
    """A reviewable proposal to enrich, not overwrite, the shared course graph."""
    UPDATE_TYPES = [
        ("course_profile", "Course Study Profile"),
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
        ("flagged", "Flagged for Correction"),
    ]

    QUESTION_TYPES = [
        ("authentic", "Authentic Past Paper"),
        ("adapted", "Adapted Past Paper"),
        ("generated", "AI Generated Variant"),
    ]

    paper = models.ForeignKey(PrepPaper, on_delete=models.SET_NULL, null=True, blank=True, related_name="questions")
    topic = models.ForeignKey(PrepTopic, on_delete=models.SET_NULL, null=True, blank=True, related_name="questions")
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


class PrepTransaction(models.Model):
    """Audit ledger for credit deductions and M-Pesa top-up purchases."""
    ACTION_CHOICES = [
        ("trial_grant", "3-Day Free Trial Starter Credits"),
        ("upload_text", "Digital Text PDF Upload (2 credits)"),
        ("upload_ocr", "Scanned Vision OCR Ingestion (5 credits)"),
        ("deep_reasoning", "Complex Proof / Derivation (5 credits)"),
        ("ai_practice_gen", "AI Practice Question Generation"),
        ("topic_notes", "AI Topic Notes Generation"),
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
