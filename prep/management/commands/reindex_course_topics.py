import json
import re
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from prep.models import PrepContentCache, PrepCourse, PrepDocument, PrepDocumentVisual
from services.prep_ai_router import (
    _note_completion_issues,
    _note_modalities,
    _note_validation_options,
    get_or_generate_topic_notes,
)
from services.prep_ingestion import (
    assign_visuals_to_topics,
    extract_and_index_topics,
    extract_topic_candidates,
    store_pdf_visual_candidates,
)


class Command(BaseCommand):
    help = "Reindex course topics from approved lecture notes and validate generated note levels."

    def add_arguments(self, parser):
        parser.add_argument("--course-code", action="append", dest="course_codes")
        parser.add_argument("--source-pdf", help="Use this local PDF as the authoritative topic and visual source.")
        parser.add_argument("--apply", action="store_true", help="Delete and rebuild topics after a successful dry-run plan.")
        parser.add_argument(
            "--validate-existing",
            action="store_true",
            help="Validate existing topics at all three note levels without changing the topic index.",
        )
        parser.add_argument(
            "--skip-generation",
            action="store_true",
            help="Reindex topics and capture visuals without calling note providers.",
        )
        parser.add_argument(
            "--auto-attach-visuals",
            action="store_true",
            help="Approve high-confidence source visuals for topic-aware note generation.",
        )
        parser.add_argument(
            "--topics-with-visuals-only",
            action="store_true",
            help="Generate notes only for topics with approved, automatically assigned visuals.",
        )
        parser.add_argument("--json", action="store_true", help="Emit the audit as JSON.")

    @staticmethod
    def _source_documents(course):
        return list(
            PrepDocument.objects.filter(
                course=course,
                stage="stage_3",
                doc_type__in=["Lecture Notes", "Revision Sheet"],
            ).exclude(extracted_text="").order_by("-updated_at", "-id")
        )

    def _source_text(self, course, source_pdf=None):
        if source_pdf:
            try:
                import fitz

                path = Path(source_pdf)
                if not path.is_file():
                    raise CommandError(f"Source PDF not found: {source_pdf}")
                document = fitz.open(path)
                text = "\n\n".join(
                    f"--- Page {page_number} ---\n{page.get_text()}"
                    for page_number, page in enumerate(document, start=1)
                )
                document.close()
                if not text.strip():
                    raise CommandError(f"Source PDF contains no extractable text: {source_pdf}")
                return text, path.read_bytes()
            except ImportError as exc:
                raise CommandError("PyMuPDF is required when --source-pdf is used") from exc
        documents = self._source_documents(course)
        return "\n\n".join(document.extracted_text or "" for document in documents), None

    def _plan_course(self, course, source_pdf=None):
        documents = self._source_documents(course)
        source_text, source_bytes = self._source_text(course, source_pdf)
        candidates = extract_topic_candidates(source_text)
        unique_candidates = {}
        for candidate in candidates:
            title = str(candidate.get("title") or "").strip()
            order = int(candidate.get("order") or 0)
            if title and order > 0:
                unique_candidates[(order, title.casefold())] = candidate
        return {
            "course_code": course.code,
            "course_title": course.title,
            "source_documents": len(documents),
            "source_text": source_text,
            "source_pdf": source_pdf or "",
            "source_image_refs": 0,
            "source_bytes": source_bytes,
            "existing_topics": course.topics.count(),
            "candidates": sorted(unique_candidates.values(), key=lambda item: (item.get("order", 0), item.get("title", ""))),
            "risks": [] if documents and unique_candidates else [
                "no usable stage_3 lecture-note topic candidates were extracted"
            ],
        }

    def _validate_levels(self, topic):
        levels = {}
        provider_calls = 0
        options = _note_validation_options(
            topic.course,
            topic.title,
            topic.summary,
            topic.subtopics,
            topic_obj=topic,
        )
        for level in ("level_1", "level_2", "level_3"):
            result = get_or_generate_topic_notes(
                topic.course.code,
                topic.title,
                level=level,
                course_obj=topic.course,
                topic_obj=topic,
            )
            notes = result.get("notes", "") if isinstance(result, dict) else ""
            issues = _note_completion_issues(
                notes,
                topic.title,
                **options,
            )
            issues.extend(self._heading_issues(notes))
            levels[level] = {
                "ok": not issues and bool(notes.strip()),
                "issues": issues,
                "cached": bool(result.get("cached")) if isinstance(result, dict) else False,
                "regenerated": bool(result.get("repaired") or result.get("regenerated_from_invalid_cache"))
                if isinstance(result, dict)
                else False,
                "modalities": sorted(_note_modalities(notes)),
            }
            if isinstance(result, dict) and not result.get("cached"):
                provider_calls += 1
        return levels, provider_calls

    @staticmethod
    def _heading_issues(notes):
        headings = re.findall(r"(?m)^\s*(#{1,6})\s+(.+?)\s*$", notes or "")
        return [
            f"unrelated heading: {prefix} {title}"
            for prefix, title in headings
            if prefix == "##" and not re.match(r"\d+\.", title)
        ]

    def _run_course(self, course, apply, source_pdf=None, skip_generation=False, auto_attach_visuals=False):
        plan = self._plan_course(course, source_pdf)
        if plan["risks"] or not apply:
            plan["mode"] = "apply" if apply else "dry_run"
            plan["topics"] = []
            plan.pop("source_text", None)
            plan.pop("source_bytes", None)
            return plan

        with transaction.atomic():
            source_document = self._source_documents(course)[0]
            if source_pdf:
                source_document.extracted_text = plan["source_text"]
                source_document.save(update_fields=["extracted_text", "updated_at"])
                plan["source_image_refs"] = store_pdf_visual_candidates(source_document, plan["source_bytes"])
            course.topics.all().delete()
            topics = extract_and_index_topics(course, plan["source_text"])
            if len(topics) != len(plan["candidates"]):
                raise CommandError(
                    f"{course.code}: reindex produced {len(topics)} topics for "
                    f"{len(plan['candidates'])} source candidates"
                )
            plan["topics"] = []
            if auto_attach_visuals:
                assignments = assign_visuals_to_topics(source_document, topics)
                plan["visual_auto_approved"] = assignments["approved"]
                plan["visual_review"] = assignments["review"]
                plan["visual_rejected"] = assignments["rejected"]
        assigned_titles = set()
        if auto_attach_visuals:
            assigned_titles = {
                str((visual.extracted_content or {}).get("auto_topic") or "")
                for visual in PrepDocumentVisual.objects.filter(document=source_document, status="approved")
                if isinstance(visual.extracted_content, dict)
                and visual.extracted_content.get("auto_decision")
                in {"approved_high_confidence", "tutor_approved"}
            }
        plan["topics"] = []
        plan["provider_calls"] = 0
        for topic in topics:
            should_generate = not skip_generation and (
                not getattr(self, "_topics_with_visuals_only", False)
                or topic.title in assigned_titles
            )
            if should_generate:
                levels, provider_calls = self._validate_levels(topic)
                plan["provider_calls"] += provider_calls
            else:
                levels = {}
            plan["topics"].append({
                "order": topic.order,
                "title": topic.title,
                "levels": levels,
                "generation_skipped": not should_generate,
            })
        plan["mode"] = "apply"
        plan["generation_skipped"] = skip_generation
        plan.pop("source_text", None)
        plan.pop("source_bytes", None)
        return plan

    def _validate_existing_course(self, course):
        plan = self._plan_course(course)
        plan["mode"] = "validate_existing"
        plan["topics"] = []
        plan["provider_calls"] = 0
        existing_topics = course.topics.filter(is_active=True).order_by("order", "id")
        if not existing_topics.exists():
            plan["risks"].append("course has no active indexed topics")
        for topic in existing_topics:
            levels, provider_calls = (
                self._validate_cached_levels(topic)
                if self._cache_only
                else self._validate_levels(topic)
            )
            plan["provider_calls"] += provider_calls
            plan["topics"].append({"order": topic.order, "title": topic.title, "levels": levels})
        plan.pop("source_text", None)
        plan.pop("source_bytes", None)
        return plan

    def _validate_cached_levels(self, topic):
        options = _note_validation_options(
            topic.course,
            topic.title,
            topic.summary,
            topic.subtopics,
            topic_obj=topic,
        )
        payloads = {}
        for cache in PrepContentCache.objects.filter(topic=topic, content_type="topic_notes"):
            payload = cache.payload if isinstance(cache.payload, dict) else {}
            level = payload.get("level")
            if level and level not in payloads:
                payloads[level] = payload
        levels = {}
        for level in ("level_1", "level_2", "level_3"):
            notes = str(payloads.get(level, {}).get("content") or "")
            issues = [f"missing cached note level {level}"] if not notes else _note_completion_issues(
                notes,
                topic.title,
                **options,
            )
            issues.extend(self._heading_issues(notes))
            levels[level] = {
                "ok": not issues,
                "issues": issues,
                "cached": bool(notes),
                "regenerated": False,
                "modalities": sorted(_note_modalities(notes)),
            }
        return levels, 0

    def handle(self, *args, **options):
        requested = options.get("course_codes") or []
        courses = PrepCourse.objects.all().order_by("code")
        if requested:
            courses = courses.filter(code__in=requested)
            found = set(courses.values_list("code", flat=True))
            missing = [code for code in requested if code not in found]
            if missing:
                raise CommandError(f"Course(s) not found: {', '.join(missing)}")

        if options["validate_existing"] and options["apply"]:
            raise CommandError("Use --validate-existing without --apply")
        if options.get("topics_with_visuals_only") and not options.get("auto_attach_visuals"):
            raise CommandError("--topics-with-visuals-only requires --auto-attach-visuals")
        self._topics_with_visuals_only = options.get("topics_with_visuals_only", False)
        if options["validate_existing"]:
            self._cache_only = options.get("skip_generation", False)
            reports = [self._validate_existing_course(course) for course in courses]
        else:
            reports = [
                self._run_course(
                    course,
                    options["apply"],
                    options.get("source_pdf"),
                    options.get("skip_generation", False),
                    options.get("auto_attach_visuals", False),
                )
                for course in courses
            ]
        report = {
            "mode": "apply" if options["apply"] else "dry_run",
            "courses": reports,
            "provider_calls": sum(item.get("provider_calls", 0) for item in reports),
            "ready": not options.get("skip_generation") and bool(reports) and all(
                not item["risks"]
                and all(
                    not topic.get("generation_skipped")
                    and all(level["ok"] for level in topic.get("levels", {}).values())
                    for topic in item.get("topics", [])
                )
                for item in reports
            ),
        }
        if options["json"]:
            self.stdout.write(json.dumps(report, ensure_ascii=True, sort_keys=True))
            return
        self.stdout.write("DRY RUN: no topics changed." if not options["apply"] else "APPLY: topics rebuilt and note levels validated.")
        for item in reports:
            self.stdout.write(
                f"{item['course_code']}: candidates={len(item['candidates'])} "
                f"topics={len(item.get('topics', []))} risks={len(item['risks'])}"
            )
        self.stdout.write(f"ready={report['ready']}")