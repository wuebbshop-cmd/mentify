from unittest.mock import patch

from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from .models import Profile, User


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


class ContactFormEmailTests(TestCase):
    def test_contact_form_delivers_to_contact_recipient_email(self):
        with patch("accounts.views.EmailMessage") as mock_email_message:
            mock_email_message.return_value.send.return_value = 1
            response = self.client.post(
                reverse("accounts:contact"),
                {
                    "name": "Jane Doe",
                    "email": "jane@example.com",
                    "message": "Hello from the contact form",
                    "consent": True,
                },
            )

        self.assertEqual(response.status_code, 302)
        mock_email_message.assert_called_once_with(
            subject="Contact form message from Jane Doe",
            body="Name: Jane Doe\nEmail: jane@example.com\n\nHello from the contact form",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_RECIPIENT_EMAIL],
            reply_to=["jane@example.com"],
        )
        mock_email_message.return_value.send.assert_called_once_with(fail_silently=False)


class ProfileViewTests(TestCase):
    def test_profile_view_sets_up_profile_for_new_user(self):
        user = User.objects.create_user(
            username="profile.user",
            email="profile@example.com",
            password="pass1234",
            first_name="Profile",
            last_name="User",
        )
        self.client.force_login(user)

        response = self.client.get(reverse("accounts:profile"))

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Profile.objects.filter(user=user).exists())
