import sys
from unittest.mock import patch

from django.test import SimpleTestCase, override_settings

import services.local_prep_worker as local_worker


class LocalWorkerLifecycleTests(SimpleTestCase):
    def setUp(self):
        local_worker._workers_started = False

    def tearDown(self):
        local_worker._workers_started = False

    @override_settings(DEBUG=False, ENABLE_LOCAL_PREP_WORKERS=False)
    def test_workers_do_not_start_when_disabled_or_production(self):
        with patch("threading.Thread") as mock_thread:
            local_worker.start_local_prep_workers()
            mock_thread.assert_not_called()

    @override_settings(DEBUG=True, ENABLE_LOCAL_PREP_WORKERS=True)
    def test_workers_do_not_start_outside_runserver(self):
        with patch.object(sys, "argv", ["manage.py", "test"]):
            with patch("threading.Thread") as mock_thread:
                local_worker.start_local_prep_workers()
                mock_thread.assert_not_called()

    @override_settings(DEBUG=True, ENABLE_LOCAL_PREP_WORKERS=True)
    def test_workers_start_on_runserver_main_process(self):
        with patch.object(sys, "argv", ["manage.py", "runserver"]):
            with patch.dict("os.environ", {"RUN_MAIN": "true"}):
                with patch("threading.Thread") as mock_thread:
                    local_worker.start_local_prep_workers()
                    self.assertEqual(mock_thread.call_count, 2)
                    thread_names = [call.kwargs.get("name") for call in mock_thread.call_args_list]
                    self.assertIn("LocalPrepNoteWorker", thread_names)
                    self.assertIn("LocalPrepAssessmentWorker", thread_names)
