"""Universal multi-level study tutor service supporting learners from K-12 to tertiary.

Provides zero-course-upload grade level calibration using negative constraints
and pedagogical boundaries, with Together/DeepSeek multimodal vision inspection.
"""

from __future__ import annotations

import base64
import io
import json
import logging
import os
import re
from typing import Any

from django.conf import settings
from django.db import transaction

from prep.models import PrepSnapMessage, PrepSnapSession, PrepSnapUpload, PrepWallet
from services.credit_service import (
    InsufficientCredits,
    get_available_credits,
    get_remaining_scanned_allowance,
    has_active_subscription,
    record_upload,
    release_credit_reservation,
    reserve_credits,
    settle_credit_reservation,
)
from services.prep_ai_router import route_math_request
from services.prep_topic_tutor import (
    _image_mime_type,
    _ocr_images,
    MAX_IMAGE_BYTES,
    MAX_IMAGE_COUNT,
    MIN_OCR_CREDITS,
)
from services.prep_tutor_billing import (
    calculate_provider_cost,
    estimate_chat_reservation,
    provider_cost_credits,
    quote_summary,
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Multi-Level Pedagogical Constraints Engine
# ---------------------------------------------------------------------------

LEVEL_PEDAGOGICAL_RULES: dict[str, dict[str, str]] = {
    "nursery": {
        "persona": (
            "You are a warm, playful, and cheerful early childhood teacher teaching kindergarten "
            "and nursery children (ages 3 to 6). Speak in very short, encouraging sentences with fun emoji."
        ),
        "guidelines": (
            "- Use simple, phonics-friendly words.\n"
            "- Focus on basic counting (numbers 1 to 20), colors, shapes, letters, sounds, and familiar animals.\n"
            "- Keep explanations sensory and concrete (e.g., 'imagine 3 apples in a basket')."
        ),
        "negative_constraints": (
            "CRITICAL NEGATIVE CONSTRAINTS (NURSERY LEVEL):\n"
            "- NEVER use algebraic variables, equations, or abstract symbols.\n"
            "- NEVER use technical grammatical terms or complex definitions.\n"
            "- NEVER present fractions, multiplication tables, or formal division."
        ),
    },
    "primary": {
        "persona": (
            "You are a patient, encouraging elementary and primary school teacher (Grades 1 to 8 / Standards 1 to 8). "
            "Your explanations are clear, structured, and easy to follow."
        ),
        "guidelines": (
            "- Break calculations down step-by-step with clear arithmetic steps.\n"
            "- In Mathematics: rely on standard arithmetic (+, -, *, /), place value, simple fractions, decimals, "
            "percentages, perimeter, basic area, and simple bar charts.\n"
            "- In Science: explain through observable real-world phenomena (states of matter, simple electric circuits, "
            "plant parts, animal habitats, weather, digestive system)."
        ),
        "negative_constraints": (
            "CRITICAL NEGATIVE CONSTRAINTS (PRIMARY LEVEL):\n"
            "- Strictly AVOID quadratic equations, negative square roots, or complex algebra.\n"
            "- Strictly AVOID trigonometry (sin, cos, tan) or coordinate geometry.\n"
            "- Strictly AVOID calculus, derivatives, integrals, or university theorems.\n"
            "- Strictly AVOID atomic orbital sub-shells (s, p, d, f) or chemical stoichiometry formulas."
        ),
    },
    "secondary": {
        "persona": (
            "You are an experienced high school / secondary school teacher (Grades 9 to 12 / Forms 1 to 4 / O-Level / IGCSE / KCSE). "
            "Your goal is to help the student achieve full marks on national secondary school examinations."
        ),
        "guidelines": (
            "- Provide step-by-step worked solutions matching secondary school examination marking schemes.\n"
            "- Always structure analytical / computational answers as:\n"
            "  1. **Topic & Concept**: Identify the specific high school curriculum topic.\n"
            "  2. **Given Information**: List all provided values and unknowns with proper units.\n"
            "  3. **Formula / Theorem**: State the standard secondary school formula applied.\n"
            "  4. **Working & Calculation**: Show complete algebraic substitution and calculation.\n"
            "  5. **Final Answer**: Clearly state the final numerical answer with units or a concise concluding statement."
        ),
        "negative_constraints": (
            "CRITICAL NEGATIVE CONSTRAINTS (SECONDARY / HIGH SCHOOL LEVEL):\n"
            "- In Mathematics & Physics: STRICTLY AVOID university calculus (derivatives, integrals, limits, L'Hôpital's rule) "
            "or university linear algebra unless the problem statement explicitly uses calculus symbols (e.g. dy/dx or integral). "
            "Use standard high school algebraic, geometric, trigonometric, or kinematic equations (v = u + at, s = ut + 0.5*a*t^2).\n"
            "- In Chemistry: Explain using high school models (Bohr model, shell electron configurations 2,8,8, valence electron dot-and-cross diagrams, "
            "basic periodic trends, and simple balanced chemical equations with state symbols). "
            "STRICTLY DO NOT INVOKE advanced quantum mechanics (sp3 hybridization, sub-orbitals s/p/d/f), reaction mechanisms with curly arrows, "
            "or university thermodynamic derivations (Delta G = Delta H - T*Delta S).\n"
            "- In Biology: Use standard secondary anatomical and physiological terms (cell structures, Mendelian Punnett squares, organ systems). "
            "Do not invoke advanced molecular biochemistry or enzyme kinetics derivations."
        ),
    },
    "tertiary": {
        "persona": (
            "You are a university professor and academic tutor teaching undergraduate and college students. "
            "Deliver rigorous, thorough academic proofs, analytical derivations, and comprehensive explanations."
        ),
        "guidelines": (
            "- Provide full theoretical derivations, mathematical rigor, and standard academic notation.\n"
            "- Discuss underlying mechanisms, boundary conditions, and formal theorems.\n"
            "- Point out academic best practices, edge cases, and methodological assumptions."
        ),
        "negative_constraints": (
            "TERTIARY LEVEL: Do not oversimplify. Maintain high academic standards and exact discipline notation."
        ),
    },
}

SUBJECT_PEDAGOGICAL_RULES: dict[str, str] = {
    "mathematics": (
        "Subject Guidance (Mathematics): Show every intermediate step in standard mathematical notation. "
        "Use LaTeX delimiters ($...$ for inline formulas and $$...$$ for standalone display equations). "
        "Explain the conceptual reasoning behind each algebraic step."
    ),
    "physics": (
        "Subject Guidance (Physics): Identify the physical law governing the problem. State given variables with standard SI units. "
        "Show formula transposition before numerical substitution. State final answers with appropriate SI units."
    ),
    "chemistry": (
        "Subject Guidance (Chemistry): Write balanced chemical equations with state symbols (s, l, g, aq) where appropriate. "
        "Explain reactions clearly and connect observed changes (color, gas evolution, precipitate) to the underlying chemical species."
    ),
    "biology": (
        "Subject Guidance (Biology): Provide clear biological explanations using standard terminology. "
        "Structure functional explanations around structure-function relationships (e.g., how an organ or tissue is adapted to its function)."
    ),
    "sciences": (
        "Subject Guidance (General Sciences): Emphasize empirical observation, scientific inquiry, hypothesis testing, and everyday scientific applications."
    ),
    "humanities": (
        "Subject Guidance (Humanities & Social Studies): Present balanced, analytical discussions. Define key historical or geographic terms clearly "
        "and organize arguments with clear topic sentences and evidence."
    ),
    "business": (
        "Subject Guidance (Business & Economics): Use standard business, accounting, and economic terminology. Show step-by-step bookkeeping or calculation "
        "where financial data is present."
    ),
    "languages": (
        "Subject Guidance (Languages & Literature): Explain grammatical rules, vocabulary context, comprehension questions, or literary devices with clear examples."
    ),
    "general": (
        "Subject Guidance: Deliver a structured, accessible explanation calibrated strictly to the selected education level."
    ),
}

# ---------------------------------------------------------------------------
# Prompt Construction
# ---------------------------------------------------------------------------

def build_snap_tutor_prompt(
    education_level: str,
    subject: str,
    user_message: str,
    extracted_materials: list[dict[str, str]],
    conversation_history: list[dict[str, str]] | None = None,
) -> tuple[str, str]:
    """Construct calibrated system and user prompts for the tutor model with multi-turn memory."""
    level_key = education_level.lower().strip() if education_level else "secondary"
    level_config = LEVEL_PEDAGOGICAL_RULES.get(level_key, LEVEL_PEDAGOGICAL_RULES["secondary"])

    subj_key = subject.lower().strip() if subject else "general"
    subject_guidance = SUBJECT_PEDAGOGICAL_RULES.get(subj_key, SUBJECT_PEDAGOGICAL_RULES["general"])

    system_prompt = (
        f"{level_config['persona']}\n\n"
        f"PEDAGOGICAL GUIDELINES:\n{level_config['guidelines']}\n\n"
        f"{level_config['negative_constraints']}\n\n"
        f"{subject_guidance}\n\n"
        "FORMATTING, CONCEPTUAL & MULTI-TURN ACCURACY RULES:\n"
        "- You are MentifyAI, an intelligent, empathetic multi-level AI study assistant.\n"
        "- MULTI-TURN CONTINUITY & PROACTIVE TUTORING:\n"
        "  * You have full conversational memory of recent conversation turns provided below.\n"
        "  * If you previously asked the student a question or offered to provide a past-paper calculation / example problem "
        "(e.g., 'Would you like me to work through a past-paper style calculation?'), and the student confirms (e.g., 'yes', 'sure', 'do it', 'show me'):\n"
        "    NEVER claim that the question or numbers didn't come through!\n"
        "    YOU offered it, so YOU MUST directly formulate an authentic, grade-appropriate problem with realistic values and work through the full, step-by-step solution immediately!\n"
        "- CONCEPTUAL & THEORETICAL QUESTIONS (NO WORKSHEET REQUIRED):\n"
        "  * Students will frequently ask conceptual questions, definitions, explanations of theorems, or curiosity doubts (e.g., 'What is Newton's 2nd law?', 'Why does momentum conserve?').\n"
        "  * Always answer concept questions directly, thoroughly, and intuitively with real-life analogies suited to the student's grade level.\n"
        "  * Never claim that 'a question didn't come through' when the student is asking a concept question.\n"
        "- MATHEMATICAL & EQUATION FORMATTING:\n"
        "  * Format all mathematical equations in clean standard LaTeX: use $...$ for inline math and $$...$$ on their own dedicated lines for display equations.\n"
        "  * Always leave a blank line before and after display math ($$...$$) so equations never collide with adjacent prose.\n"
        "  * Clearly separate sections with bold headers or numbered steps.\n"
        "- Address the student respectfully, warmly, and clearly."
    )

    user_parts: list[str] = []

    # Include recent conversation turns for multi-turn conversational memory
    if conversation_history:
        history_lines = []
        for turn in conversation_history[-8:]:
            speaker = "Student" if turn.get("role") == "user" else "MentifyAI Tutor"
            text_snip = str(turn.get("content") or "").strip()
            if text_snip:
                history_lines.append(f"[{speaker}]:\n{text_snip}")
        if history_lines:
            user_parts.append("### RECENT CONVERSATION HISTORY (Previous turns in this session):")
            user_parts.append("\n\n".join(history_lines))
            user_parts.append("--- End of recent conversation history ---\n")

    if extracted_materials:
        user_parts.append("### ATTACHED STUDY MATERIALS & QUESTION IMAGES:")
        for idx, item in enumerate(extracted_materials, start=1):
            name = item.get("name", f"Image {idx}")
            c_type = item.get("content_type", "image")
            text = item.get("text", "").strip()
            desc = item.get("visual_description", "").strip()

            user_parts.append(f"\n[Attachment {idx}: {name} (Classified as: {c_type})]")
            if text:
                user_parts.append(f"Visible Text / Question:\n{text}")
            if desc:
                user_parts.append(f"Visual Diagram / Chart Description:\n{desc}")

    if user_message.strip():
        user_parts.append(f"\n### STUDENT'S CURRENT MESSAGE / QUESTION:\n{user_message.strip()}")
    elif extracted_materials:
        user_parts.append("\n### STUDENT'S CURRENT MESSAGE / QUESTION:\nPlease solve and clearly explain the problem shown in the attached image step-by-step.")

    user_prompt = "\n".join(user_parts)
    return system_prompt, user_prompt


# ---------------------------------------------------------------------------
# Image Handling & Vision Extraction
# ---------------------------------------------------------------------------

def process_uploaded_images(uploaded_files: list[Any]) -> tuple[list[dict[str, Any]], dict[str, Any], str]:
    """Inspect and extract text/visual descriptions from uploaded image files.
    
    Returns (processed_results, ocr_usage, ocr_model).
    """
    if not uploaded_files:
        return [], {}, ""

    images_to_ocr: list[dict[str, Any]] = []
    processed_results: list[dict[str, Any]] = []

    for file_obj in uploaded_files[:MAX_IMAGE_COUNT]:
        name = getattr(file_obj, "name", "upload.png")
        try:
            content = file_obj.read()
            if hasattr(file_obj, "seek"):
                file_obj.seek(0)
        except Exception as exc:
            logger.warning("Failed to read uploaded file %s: %s", name, exc)
            continue

        if not content or len(content) > MAX_IMAGE_BYTES:
            continue

        mime = _image_mime_type(content)
        if not mime:
            continue

        images_to_ocr.append({
            "name": name,
            "mime_type": mime,
            "content": content,
            "base64": base64.b64encode(content).decode("utf-8"),
        })

    if not images_to_ocr:
        return [], {}, ""

    ocr_usage: dict[str, Any] = {}
    ocr_model: str = getattr(settings, "TOGETHER_VISION_MODEL", "deepseek-ai/DeepSeek-V4.1-Flash")

    # Call Together / DeepSeek multimodal OCR
    try:
        ocr_payload = _ocr_images(
            [{"name": item["name"], "label": item["name"], "mime_type": item["mime_type"], "base64": item["base64"]} for item in images_to_ocr],
            figure_hint="For homework and exam questions, transcribe all problem numbers, formulas, and labels exactly.",
        )
        ocr_usage = ocr_payload.get("usage") or {}
        ocr_model = ocr_payload.get("model") or ocr_model

        raw_items = ocr_payload.get("items", {})
        if isinstance(raw_items, dict):
            items_by_label = raw_items
        elif isinstance(raw_items, list):
            items_by_label = {
                item.get("label"): item
                for item in raw_items
                if isinstance(item, dict) and item.get("label")
            }
        else:
            items_by_label = {}
    except Exception as exc:
        logger.error("Vision OCR call failed for snap tutor: %s", exc)
        items_by_label = {}

    for img in images_to_ocr:
        extracted_info = items_by_label.get(img["name"], {})
        c_type = extracted_info.get("content_type", "text_notes")
        text = str(extracted_info.get("extracted_text", "") or "").strip()
        desc = str(extracted_info.get("visual_description", "") or "").strip()

        processed_results.append({
            "name": img["name"],
            "mime_type": img["mime_type"],
            "content": img["content"],
            "content_type": c_type,
            "text": text,
            "visual_description": desc,
        })

    return processed_results, ocr_usage, ocr_model


# ---------------------------------------------------------------------------
# High-Level Turn Execution
# ---------------------------------------------------------------------------

def execute_snap_tutor_turn(
    *,
    user: Any,
    session: PrepSnapSession,
    user_message: str,
    uploaded_files: list[Any],
) -> dict[str, Any]:
    """Execute a complete learner interaction turn with vision OCR, reasoning, credit deduction, and DB save."""
    # 1. Fetch previous session history for multi-turn conversational continuity
    recent_msg_records = list(session.messages.order_by("created_at")[:10])
    conversation_history = [
        {"role": m.role, "content": m.content}
        for m in recent_msg_records
    ]

    # 2. Credit estimation and reservation
    wallet = None
    reservation = None
    ocr_reserve = 0
    chat_reserve = 0
    ocr_credits = 0
    chat_credits = 0
    ocr_covered_by_plan = False
    valid_files_count = min(len(uploaded_files or []), MAX_IMAGE_COUNT)
    ocr_per_page = max(1, int(getattr(settings, "PREP_OCR_CREDITS_PER_IMAGE_PAGE", MIN_OCR_CREDITS)))

    if user and user.is_authenticated:
        wallet = PrepWallet.get_or_create_wallet(user)
        has_sub = has_active_subscription(wallet)
        scanned_allowance = get_remaining_scanned_allowance(wallet) if has_sub else 0
        ocr_covered_by_plan = bool(has_sub and (scanned_allowance is None or scanned_allowance >= valid_files_count))
        ocr_reserve = 0 if ocr_covered_by_plan else (ocr_per_page * valid_files_count)

        CHAT_MAX_OUTPUT_TOKENS = 3000
        chat_model = str(getattr(settings, "DEEPSEEK_CHAT_MODEL", "deepseek-chat"))
        # Quick provisional prompt for chat reservation
        provisional_system, provisional_user = build_snap_tutor_prompt(
            education_level=session.education_level,
            subject=session.subject,
            user_message=user_message,
            extracted_materials=[],
            conversation_history=conversation_history,
        )
        chat_reserve, chat_reserve_quote = estimate_chat_reservation(
            provisional_system,
            provisional_user,
            chat_model,
            output_token_cap=CHAT_MAX_OUTPUT_TOKENS,
        )
        total_reserve = ocr_reserve + chat_reserve
        try:
            reservation = reserve_credits(
                wallet,
                total_reserve,
                purpose="snap_tutor",
                metadata={
                    "session_id": str(session.id),
                    "education_level": session.education_level,
                    "subject": session.subject,
                    "ocr_image_count": valid_files_count,
                    "ocr_reserved_credits": ocr_reserve,
                    "chat_reserved_credits": chat_reserve,
                    "chat_reservation_pricing": quote_summary(chat_reserve_quote, chat_reserve),
                },
            )
        except InsufficientCredits:
            available = get_available_credits(wallet)
            raise InsufficientCredits(
                f"MentifyAI requires {total_reserve} credits for this question (you currently have {available}). Please top up your balance."
            )

    # 3. Process and extract any uploaded question images
    try:
        extracted_uploads, ocr_usage, ocr_model = process_uploaded_images(uploaded_files)
    except Exception as exc:
        if reservation:
            release_credit_reservation(reservation, reason=f"Image processing failed: {exc}")
        raise

    # Settle OCR reservation
    if wallet and reservation and extracted_uploads:
        if ocr_covered_by_plan:
            record_upload(
                wallet,
                count=len(extracted_uploads),
                upload_type="snap_image_ocr",
                description=f"MentifyAI Image OCR ({len(extracted_uploads)} images - Plan Allowance)",
            )
            ocr_credits = 0
            if ocr_reserve > 0:
                # If anything was reserved for OCR, release that portion
                release_credit_reservation(reservation, amount=ocr_reserve, reason="Covered by subscription allowance")
        else:
            ocr_quote = calculate_provider_cost("together", ocr_model, ocr_usage)
            ocr_credits = settle_credit_reservation(
                reservation,
                ocr_per_page * len(extracted_uploads),
                release_reserved=ocr_reserve,
                action_type="snap_tutor_ocr",
                description=f"MentifyAI Image OCR ({len(extracted_uploads)} images): {session.get_subject_display()}",
                usage=ocr_usage,
                model_name=ocr_model,
                metadata={
                    "provider": "together",
                    "pricing": quote_summary(ocr_quote, ocr_per_page * len(extracted_uploads)),
                    "image_count": len(extracted_uploads),
                    "session_id": str(session.id),
                },
            )
    elif reservation and ocr_reserve > 0 and not extracted_uploads:
        # Released OCR reserve if no valid uploads found
        release_credit_reservation(reservation, amount=ocr_reserve, reason="No valid images to OCR")

    # 4. Build the context-calibrated prompt with history & extracted images
    system_prompt, user_prompt = build_snap_tutor_prompt(
        education_level=session.education_level,
        subject=session.subject,
        user_message=user_message,
        extracted_materials=extracted_uploads,
        conversation_history=conversation_history,
    )

    # 5. Call DeepSeek / Together reasoning model via route_math_request
    try:
        ai_result = route_math_request(
            user_prompt,
            course_code=f"SNAP-{session.education_level.upper()}",
            topic_label=session.subject.capitalize(),
            system_prompt=system_prompt,
            is_complex_proof=(session.education_level == "tertiary"),
            thinking_enabled=False,
        )
    except Exception as exc:
        if reservation:
            release_credit_reservation(reservation, reason=f"AI model generation failed: {exc}")
        raise

    answer_content = str(ai_result.get("content") or "").strip()
    if not answer_content:
        error_msg = ai_result.get("error") or "The AI tutor was unable to generate a response. Please try again."
        answer_content = f"**Notice:** {error_msg}"

    model_used = ai_result.get("model_used") or "deepseek-v3"
    token_usage = ai_result.get("usage") or {}

    # 6. Settle Chat reservation
    if wallet and reservation:
        if token_usage and any(token_usage.values()):
            chat_quote = calculate_provider_cost("deepseek", model_used, token_usage)
            chat_credits = provider_cost_credits(chat_quote)
            settle_credit_reservation(
                reservation,
                chat_credits,
                action_type="snap_tutor",
                description=f"MentifyAI reply: {session.get_education_level_display()} / {session.get_subject_display()}",
                usage=token_usage,
                model_name=model_used,
                metadata={
                    "provider": "deepseek",
                    "pricing": quote_summary(chat_quote, chat_credits),
                    "session_id": str(session.id),
                },
            )
        else:
            release_credit_reservation(reservation, reason="No billable chat token usage returned.")

    total_credits_charged = ocr_credits + chat_credits
    if wallet:
        wallet.refresh_from_db(fields=["credits_balance"])

    # 7. Atomic database persistence
    with transaction.atomic():
        # Save user message
        user_msg_record = PrepSnapMessage.objects.create(
            session=session,
            role="user",
            content=user_message.strip() or "[Image Upload Question]",
            credits_charged=0,
        )

        # Save assistant solution message with actual credits charged
        assistant_msg_record = PrepSnapMessage.objects.create(
            session=session,
            role="assistant",
            content=answer_content,
            model_used=model_used,
            token_usage=token_usage,
            credits_charged=total_credits_charged,
        )

        # Save upload records
        saved_uploads_metadata: list[dict[str, str]] = []
        for upload_item in extracted_uploads:
            from django.core.files.base import ContentFile
            upload_record = PrepSnapUpload(
                session=session,
                message=user_msg_record,
                original_name=upload_item["name"],
                content_type=upload_item["content_type"],
                extracted_text=upload_item["text"],
                visual_description=upload_item["visual_description"],
            )
            if upload_item.get("content"):
                upload_record.image_file.save(
                    upload_item["name"],
                    ContentFile(upload_item["content"]),
                    save=False,
                )
            upload_record.save()

            saved_uploads_metadata.append({
                "id": str(upload_record.id),
                "name": upload_record.original_name,
                "content_type": upload_record.content_type,
                "extracted_text": upload_record.extracted_text,
                "visual_description": upload_record.visual_description,
                "image_url": upload_record.image_file.url if upload_record.image_file else "",
            })

        # Update session title if default
        if session.title == "New Study Session":
            candidate_title = user_message.strip()
            if not candidate_title and extracted_uploads:
                first_text = extracted_uploads[0]["text"]
                first_line = first_text.split("\n")[0] if first_text else ""
                candidate_title = first_line[:60].strip() or f"{session.get_subject_display()} Problem"
            if candidate_title:
                session.title = candidate_title[:80]
        session.save(update_fields=["title", "updated_at"])

    return {
        "success": True,
        "answer": answer_content,
        "session_id": str(session.id),
        "session_title": session.title,
        "education_level": session.education_level,
        "subject": session.subject,
        "model_used": model_used,
        "uploads": saved_uploads_metadata,
        "message_id": str(assistant_msg_record.id),
        "credits_charged": total_credits_charged,
        "credits_balance": get_available_credits(wallet) if wallet else None,
    }


# ---------------------------------------------------------------------------
# Session & Conversation Helpers
# ---------------------------------------------------------------------------

def get_or_create_snap_session(
    user: Any,
    session_id: str | None = None,
    education_level: str = "secondary",
    subject: str = "general",
) -> PrepSnapSession:
    """Retrieve existing session or create a new one."""
    if session_id:
        try:
            lookup: dict[str, Any] = {"id": session_id}
            if user and user.is_authenticated:
                lookup["user"] = user
            return PrepSnapSession.objects.get(**lookup)
        except (PrepSnapSession.DoesNotExist, ValueError):
            pass

    return PrepSnapSession.objects.create(
        user=user if (user and user.is_authenticated) else None,
        education_level=education_level or "secondary",
        subject=subject or "general",
    )


def list_snap_sessions(user: Any) -> list[dict[str, Any]]:
    """List recent study sessions for the authenticated user."""
    if not user or not user.is_authenticated:
        return []

    sessions = PrepSnapSession.objects.filter(user=user).order_by("-updated_at")[:30]
    return [
        {
            "id": str(s.id),
            "title": s.title,
            "education_level": s.education_level,
            "education_level_display": s.get_education_level_display(),
            "subject": s.subject,
            "subject_display": s.get_subject_display(),
            "updated_at": s.updated_at.isoformat(),
        }
        for s in sessions
    ]


def get_snap_session_messages(session: PrepSnapSession) -> list[dict[str, Any]]:
    """Retrieve chronologically ordered messages and upload metadata for a session."""
    messages = session.messages.order_by("created_at").prefetch_related("uploads")
    payload = []
    for msg in messages:
        uploads_data = [
            {
                "id": str(u.id),
                "name": u.original_name,
                "content_type": u.content_type,
                "extracted_text": u.extracted_text,
                "visual_description": u.visual_description,
                "image_url": u.image_file.url if u.image_file else "",
            }
            for u in msg.uploads.all()
        ]
        payload.append({
            "id": str(msg.id),
            "role": msg.role,
            "content": msg.content,
            "model_used": msg.model_used,
            "created_at": msg.created_at.isoformat(),
            "uploads": uploads_data,
        })
    return payload
