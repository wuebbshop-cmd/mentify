"""Run the official PDF job processor with automatic database reconnect retries."""

from __future__ import annotations

import io
import os
import sys
import time
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))
os.chdir(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

import django  # noqa: E402

django.setup()

from django.db import close_old_connections, connection  # noqa: E402
from django.utils import timezone  # noqa: E402

from prep.models import PrepTopicPdfArtifact  # noqa: E402
from services.prep_pdf_artifacts import process_next_pdf_artifact  # noqa: E402


def recover_stale_running_jobs() -> int:
    cutoff = timezone.now() - timedelta(minutes=30)
    return PrepTopicPdfArtifact.objects.filter(
        status="running",
        started_at__lt=cutoff,
    ).update(
        status="pending",
        started_at=None,
        next_attempt_at=timezone.now(),
        last_error="Recovered after the resilient PDF pipeline detected a disconnected worker.",
    )


def wait_for_database(max_wait_seconds: float = 30.0) -> bool:
    deadline = time.monotonic() + max_wait_seconds
    delay = 2.0
    while time.monotonic() < deadline:
        close_old_connections()
        try:
            connection.ensure_connection()
            if connection.connection is not None:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    cursor.fetchone()
                return True
        except Exception:
            pass
        time.sleep(delay)
        delay = min(delay * 1.5, 15.0)
    return False


def main() -> None:
    print("Resilient PDF pipeline starting", flush=True)
    processed = 0
    database_waits = 0

    while True:
        try:
            close_old_connections()
            if connection.connection is None:
                connection.ensure_connection()

            recovered = recover_stale_running_jobs()
            if recovered:
                print(f"recovered stale running jobs={recovered}", flush=True)

            if process_next_pdf_artifact():
                processed += 1
                if processed % 5 == 0:
                    ready = PrepTopicPdfArtifact.objects.filter(status="ready").count()
                    pending = PrepTopicPdfArtifact.objects.filter(status="pending").count()
                    failed = PrepTopicPdfArtifact.objects.filter(status="failed").count()
                    print(
                        f"progress processed={processed} ready={ready} pending={pending} failed={failed}",
                        flush=True,
                    )
                time.sleep(0.25)
                continue

            pending_or_running = PrepTopicPdfArtifact.objects.filter(
                status__in=("pending", "running")
            ).count()
            if pending_or_running == 0:
                print(
                    f"queue complete: processed={processed}, "
                    f"ready={PrepTopicPdfArtifact.objects.filter(status='ready').count()}",
                    flush=True,
                )
                return

            time.sleep(5)
        except Exception as exc:
            database_waits += 1
            print(
                f"connection interruption #{database_waits}: "
                f"{type(exc).__name__}: {str(exc)[:300]}; reconnecting and retrying",
                flush=True,
            )
            close_old_connections()
            connection.close()
            recovered_connection = False
            while not recovered_connection:
                recovered_connection = wait_for_database(max_wait_seconds=30.0)
                if not recovered_connection:
                    print(
                        "database still unavailable; waiting 10 seconds and retrying indefinitely",
                        flush=True,
                    )
                    time.sleep(10)


if __name__ == "__main__":
    main()
