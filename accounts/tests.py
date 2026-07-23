from django.test import TestCase

from .models import User


class UsernameGenerationTests(TestCase):
    def test_build_username_from_email_sanitizes_and_normalizes(self):
        from .forms import build_username_from_email

        username = build_username_from_email("Test.User+Demo@example.com")
        self.assertEqual(username, "test.userdemo")

    def test_build_username_from_email_appends_suffix_for_duplicates(self):
        from .forms import build_username_from_email

        User.objects.create_user(username="test.user", email="existing@example.com", password="pass1234")

        username = build_username_from_email("test.user@example.com")
        self.assertEqual(username, "test.user2")
