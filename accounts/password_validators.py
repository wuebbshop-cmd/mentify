"""Password validation rules shared by every Django password form."""

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class LetterAndNumberPasswordValidator:
    """Require passwords to contain both alphabetic and numeric characters."""

    message = _("Your password must include at least one letter and one number.")
    code = "password_requires_letter_and_number"

    def validate(self, password, user=None):
        # Keep this aligned with the browser check in static/js/password-rules.js.
        has_letter = any(character.isascii() and character.isalpha() for character in password)
        has_number = any(character.isascii() and character.isdigit() for character in password)
        if not (has_letter and has_number):
            raise ValidationError(self.message, code=self.code)

    def get_help_text(self):
        return _(
            "Your password must be at least 8 characters long and include at least one letter and one number."
        )
