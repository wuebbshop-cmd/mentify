import logging
import os
import sys
import threading
import time

from django.conf import settings
from django.core.management import call_command

logger = logging.getLogger(__name__)

_workers_started = False
_lock = threading.Lock()


def _run_worker_loop(command_name: str, poll_seconds: float = 3.0):
    logger.info(f"[Local Worker] Running background {command_name} loop...")
    while True:
        try:
            call_command(command_name, poll_seconds=poll_seconds)
        except Exception as exc:
            logger.warning(
                f"[Local Worker] {command_name} exited with error: {exc}. "
                "Restarting worker in 5 seconds..."
            )
            time.sleep(5.0)


def start_local_prep_workers():
    """
    Automatically start local background workers for note preparation and assessment
    question indexing when running the development server (runserver).

    This eliminates the need to manually run multiple worker commands in separate
    terminals during local development, while keeping Render's standalone worker
    services unchanged in production.
    """
    global _workers_started
    if _workers_started:
        return

    with _lock:
        if _workers_started:
            return

        # 1. Only run if enabled and in development mode (DEBUG=True)
        enabled = getattr(settings, "ENABLE_LOCAL_PREP_WORKERS", settings.DEBUG)
        if not enabled:
            return

        # 2. Never run inside production / Render (where dedicated worker services exist in render.yaml)
        if os.environ.get("RENDER") or not settings.DEBUG:
            return

        # 3. Only run when executing 'runserver', not tests, migrations, shell, etc.
        is_runserver = any("runserver" in arg for arg in sys.argv)
        if not is_runserver:
            return

        # 4. In autoreload mode, only run in the child process where the actual app runs
        if "--noreload" not in sys.argv and os.environ.get("RUN_MAIN") != "true":
            return

        _workers_started = True

        note_worker = threading.Thread(
            target=_run_worker_loop,
            args=("run_prep_note_worker", 3.0),
            name="LocalPrepNoteWorker",
            daemon=True,
        )
        note_worker.start()

        assessment_worker = threading.Thread(
            target=_run_worker_loop,
            args=("run_prep_assessment_worker", 3.0),
            name="LocalPrepAssessmentWorker",
            daemon=True,
        )
        assessment_worker.start()

        sys.stdout.write(
            "[Local Workers] Started background note generator and assessment question indexing workers.\n"
        )
        sys.stdout.flush()
