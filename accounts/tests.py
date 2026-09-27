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


class PasswordValidationTests(TestCase):
    def registration_form(self, password):
        from .forms import LearnerRegistrationForm

        return LearnerRegistrationForm(
            data={
                "first_name": "Password",
                "last_name": "Tester",
                "email": "password-tester@example.com",
                "phone": "",
                "password1": password,
                "password2": password,
                "agree_to_terms": True,
            }
        )

    def test_registration_rejects_password_without_a_number(self):
        form = self.registration_form("LettersOnly")

        self.assertFalse(form.is_valid())
        self.assertIn(
            "at least one letter and one number",
            form.errors["password2"].as_text(),
        )

    def test_registration_rejects_password_shorter_than_eight_characters(self):
        form = self.registration_form("Abc123")

        self.assertFalse(form.is_valid())
        self.assertIn("at least 8 characters", form.errors["password2"].as_text())

    def test_registration_accepts_a_password_with_letters_numbers_and_eight_characters(self):
        form = self.registration_form("Cobalt7Mango")

        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.fields["password1"].widget.attrs["minlength"], 8)
        self.assertEqual(form.fields["password1"].widget.attrs["autocomplete"], "new-password")

    def test_password_reset_enforces_the_same_rules(self):
        from .forms import MentifySetPasswordForm

        user = User.objects.create_user(
            username="password.reset",
            email="password-reset@example.com",
            password="Existing7Password",
        )
        form = MentifySetPasswordForm(
            user,
            data={
                "new_password1": "LettersOnly",
                "new_password2": "LettersOnly",
            },
        )

        self.assertFalse(form.is_valid())
        self.assertIn(
            "at least one letter and one number",
            form.errors["new_password2"].as_text(),
        )
