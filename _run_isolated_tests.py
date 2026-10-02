import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django

django.setup()

from django.conf import settings
from django.core.management import call_command
from django.db import connections
from django.test.utils import override_settings

test_databases = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "TEST": {"NAME": ":memory:"},
    },
}

with override_settings(DATABASES=test_databases):
    connections.close_all()
    print("Test database engine:", connections["default"].settings_dict["ENGINE"])
    call_command(
        "test",
        "prep.tests.test_document_visual_extraction",
        "prep.tests.test_course_profiles",
        "prep.tests.test_note_math_validation",
        verbosity=2,
        interactive=False,
        keepdb=False,
        parallel=1,
    )
