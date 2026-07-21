# Project Spec: Kenyan EdTech Platform

## 1. What this platform is

A web platform for Kenyan learners (teens and younger) and tutors, built with **Django** and **MySQL**.

Two learning tracks:

1. **Tech track (run by the platform owner initially):** modern programming (with AI-assisted coding in mind, not rote syntax drilling), basic machine learning, software engineering fundamentals, statistics and math for ML, and an accessible introduction to modern AI concepts.
2. **CBC academic + specialist tracks (tutor-led, onboarded later):** CBC curriculum subjects (Math, Chemistry, Biology, Physics, etc.), starting with Junior Secondary School and expanding later, plus specialist subjects — Software Engineering, Electronics & Robotics, Cybersecurity — each led by an independent tutor.

Delivery model:
- Pre-recorded video lessons (hosted on **Bunny Stream**) with PDF notes(uploaded to a github repo using the github python library), links, assignments(uploaded to a github repo as well), and resources attached to each lesson. No auto-generated transcripts — explicitly out of scope.
- Scheduled live classes via **manually pasted meeting links** (Zoom/Google Meet/etc.) — no Zoom API integration, no automated meeting creation.
- Classes run on **weekends and school holidays**.
- Make-up sessions for learners who miss a scheduled live class.
- Monthly subscription billing per course/cohort.
- Payments via **Paystack** (cards/mobile money through Paystack's Kenya rails) and **manual cash entry** by the platform admin (some parents pay cash in person; admin creates/extends the learner's access manually).
- A grading system for assignments and progress tracking.
- Every tutor gets a dashboard to manage their own courses/cohorts: post videos, resources, assignments; schedule live sessions; grade submissions; see their enrolled learners.

## 2. User roles

- **Admin (platform owner):** manages all courses, cohorts, users, payments (including manual cash entries), and has visibility across the whole platform. Also acts as a tutor for the tech track initially.
- **Tutor:** owns one or more courses/cohorts. Can create lessons, upload resources, post assignments, schedule live sessions, grade submissions, view their own learners' progress. Cannot see other tutors' cohorts or platform-wide admin data.
- **Learner:** enrolls in cohorts, watches lessons, submits assignments, joins live sessions via posted links, sees their own grades/progress.
- **Guardian (parent, optional/secondary):** linked to one or more learners. Can view a learner's progress/grades and payment status. (Build after core learner/tutor flows work — not a blocker for MVP.)

## 3. Core data model

```
User (Django auth user) -- has a Profile with role: admin / tutor / learner
Guardian -- linked to one or more Learners (many-to-many or FK depending on design)

Course        -- a template/subject (e.g. "Intro to Programming", "JSS Chemistry")
  Cohort      -- one actual running instance of a Course
                 (tutor, term/dates, schedule, capacity, price, status)
    Enrollment -- Learner <-> Cohort (status: active / paused / completed / expired)

Lesson         -- belongs to a Cohort (or Course, if content is reused across cohorts)
  VideoAsset   -- Bunny Stream video ID/embed reference (no transcript field)
  Resource     -- PDF / external link, attached to a Lesson
  Assignment   -- attached to a Lesson
    Submission -- Learner's submitted work for an Assignment
      Grade    -- score + rubric breakdown + tutor comment, linked to a Submission

LiveSession    -- belongs to a Cohort: date/time, manually-entered meeting link, notes
  Attendance   -- Learner <-> LiveSession (attended / missed / excused) -- manually marked by tutor, no Zoom webhook
  MakeupSession -- FK back to the original LiveSession it replaces

Subscription   -- Learner <-> Cohort (or Course), monthly, has paid_until date, status
Payment        -- linked to a Subscription
                  method: paystack | cash
                  for cash: recorded_by = admin user, includes a note/reference
```

Key design point: **cash payments and Paystack payments both write to the same `Payment`/`Subscription` model.** Cash is just a payment method with `recorded_by` set to the admin, not a separate account-creation path. Access control (can this learner see this cohort's content) should always check `Subscription.paid_until >= today`, regardless of how they paid.

## 4. Payments

- **Paystack**: integrate their standard Kenya-supported checkout (card + M-Pesa via Paystack, if enabled on the account) for online monthly subscription payments. Use Paystack's webhook to confirm payment and extend `Subscription.paid_until` by one month from the current `paid_until` (or from today if lapsed).
- **Manual cash**: an admin-only view/action — "Record Payment" — where the admin selects a learner + cohort, enters amount and date, and the system creates a `Payment(method='cash')` and extends `Subscription.paid_until` exactly like a Paystack webhook would. If the learner doesn't have an account yet, the same flow should allow creating the learner account (and Guardian, if applicable) inline before recording the payment.
- **Access gating**: a daily scheduled task (Django management command run via cron, or `django-crontab`/Celery beat if already using Celery for other things) checks all subscriptions and flags/suspends access for anyone past `paid_until`. Keep this simple — don't build automated recurring billing/auto-charge in v1; monthly payment is a manual action by the parent (or admin, for cash) each month.

## 5. Video content (Bunny Stream)

- Videos are uploaded to Bunny Stream (via their API or dashboard) and the platform stores only the Bunny video ID / embed/player URL against a `VideoAsset` row — never store or serve raw video files from the Django app itself.
- Use Bunny's signed URLs / token authentication if available on the plan, so video links aren't freely shareable outside the platform.
- No transcript generation or storage — explicitly out of scope.
- Each Lesson can have one video plus multiple Resources (PDFs, links) and one or more Assignments.

## 6. Live sessions (manual links, no Zoom API)

- A `LiveSession` is created by a tutor for their cohort with a date/time and a manually pasted meeting link (any provider).
- Learners see upcoming sessions for their enrolled cohorts on their dashboard with the join link active close to the session time.
- Attendance is marked manually by the tutor after the session (simple present/missed/excused per learner).
- If a learner misses a session, the tutor can schedule a `MakeupSession` linked back to the original — this should show up distinctly on the learner's dashboard as "make-up available."

## 7. Grading system

- **Assignments**: rubric-based. A rubric is a set of weighted criteria defined per assignment by the tutor; grading produces a per-criterion score + comment, rolled up into a total.
- **Quizzes** (optional, useful for CBC subjects and stats/math fundamentals): auto-graded objective questions (MCQ, short numeric answer).
- **Progress view**: per learner, show % lessons completed, assignment completion rate, attendance rate — separate from raw grades. This should be visible to the learner and (later) their guardian.

## 8. Dashboards

- **Tutor dashboard**: list of their cohorts → per cohort: manage lessons/resources/assignments, schedule live sessions, mark attendance, grade submissions, see enrolled learners and their progress.
- **Learner dashboard**: their enrolled cohorts → lessons (watch video, download resources, submit assignments), upcoming/past live sessions with join links, grades/progress, subscription/payment status.
- **Admin dashboard**: everything above across all tutors/cohorts, plus user management, manual payment recording, and platform-wide reporting. Lean heavily on Django's built-in admin for this rather than building custom admin screens from scratch, especially in v1.

## 9. Non-functional notes for the build

- Target users are on mobile data in Kenya a lot of the time — keep pages light, avoid heavy JS bundles where server-rendered Django templates + light JS (or HTMX) will do.
- MySQL as the database (not Postgres) — confirmed choice.
- No Zoom API, no Daraja, no video transcription — do not add these as "nice to have" scope creep during the build.
- Keep the codebase organized as Django apps by domain, e.g.: `accounts` (users/roles/guardians), `courses` (Course/Cohort/Enrollment), `content` (Lesson/VideoAsset/Resource), `assignments` (Assignment/Submission/Grade), `sessions` (LiveSession/Attendance/MakeupSession), `payments` (Subscription/Payment/Paystack integration).

## 10. Build plan (phased)

**Phase 1 — Foundation**
- Django project setup, MySQL configured, `accounts` app with roles (admin/tutor/learner), auth (login/signup), basic Django admin access for the platform owner.
- `courses` app: Course, Cohort, Enrollment models + basic CRUD via Django admin.

**Phase 2 — Content**
- `content` app: Lesson, VideoAsset (Bunny Stream integration for upload/embed), Resource.
- Tutor-facing views to create/edit lessons and attach resources within their own cohorts only (enforce ownership checks).
- Learner-facing views to browse enrolled cohorts and watch lessons.

**Phase 3 — Payments**
- `payments` app: Subscription, Payment models.
- Paystack integration: checkout initiation + webhook handler that extends `paid_until`.
- Admin "Record Cash Payment" flow, including inline learner/guardian account creation.
- Access-gating: daily check that suspends content access when `paid_until` has passed; enforce on all content/lesson views.

**Phase 4 — Assignments & Grading**
- `assignments` app: Assignment, Submission, Grade (rubric-based).
- Tutor grading UI; learner submission UI; progress rollups (completion %, attendance %).

**Phase 5 — Live sessions**
- `sessions` app: LiveSession (manual link), Attendance (manual marking), MakeupSession.
- Learner dashboard surfaces upcoming sessions and make-up sessions clearly.

**Phase 6 — Dashboards & polish**
- Build out tutor and learner dashboards as the main day-to-day UI (rather than relying on Django admin for non-admin users).
- Guardian accounts and guardian-facing progress/payment view.
- Reporting for the admin (active subscriptions, revenue by cohort, attendance trends).

Each phase should be independently testable and deployable — don't wait until everything is built to have a working, demoable slice of the platform (Phases 1–3 alone give you a usable "learners can pay and watch content" product).


Self‑service linking (recommended UX):
Allow guardians to add a child by email/username from their dashboard.
Backend validates the learner exists and has role learner.
Send a confirmation request to the learner (or to admin) and require acceptance (consent), or require the guardian to provide a verification code from the learner account.
Create (or update) the Guardian record and add the learner to guardian.learners only after successful validation/consent.
Admin-managed linking (current, simple):
Keep admin linking via Django admin for controlled environments or until the self‑serve flow is implemented.
Security & privacy:
Require learner consent or admin approval before exposing progress/grades.
Log link/unlink events (audit trail) and notify both parties by email.

For any needed notifications, Use gmail smtp