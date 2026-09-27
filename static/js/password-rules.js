(function () {
  "use strict";

  var message = "Use at least 8 characters with at least one letter and one number.";

  function isValidPassword(value) {
    return value.length >= 8 && /[A-Za-z]/.test(value) && /[0-9]/.test(value);
  }

  function addFeedback(form, passwordField) {
    var group = passwordField.closest(".form-group") || passwordField.parentElement;
    var feedback = document.createElement("p");
    feedback.className = "form-text password-rule-feedback";
    feedback.id = passwordField.id + "-rules";
    feedback.setAttribute("aria-live", "polite");
    feedback.textContent = message;
    group.appendChild(feedback);

    var describedBy = passwordField.getAttribute("aria-describedby");
    passwordField.setAttribute(
      "aria-describedby",
      describedBy ? describedBy + " " + feedback.id : feedback.id
    );

    return feedback;
  }

  function setFeedback(feedback, valid, hasValue) {
    feedback.textContent = valid || !hasValue ? message : message + " Password does not meet this requirement yet.";
    feedback.style.color = valid ? "var(--green)" : "";
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("form[data-password-rules]").forEach(function (form) {
      var passwordField = form.querySelector('input[name="password1"], input[name="new_password1"]');
      var confirmationField = form.querySelector('input[name="password2"], input[name="new_password2"]');
      if (!passwordField) {
        return;
      }

      var feedback = addFeedback(form, passwordField);

      function validatePassword() {
        var valid = isValidPassword(passwordField.value);
        passwordField.setAttribute("aria-invalid", passwordField.value && !valid ? "true" : "false");
        setFeedback(feedback, valid, Boolean(passwordField.value));
        return valid;
      }

      function passwordsMatch() {
        if (!confirmationField || !confirmationField.value) {
          return true;
        }
        return passwordField.value === confirmationField.value;
      }

      passwordField.addEventListener("input", validatePassword);
      if (confirmationField) {
        confirmationField.addEventListener("input", function () {
          confirmationField.setAttribute("aria-invalid", passwordsMatch() ? "false" : "true");
        });
      }

      form.addEventListener("submit", function (event) {
        var passwordValid = validatePassword();
        var confirmationValid = passwordsMatch();
        if (passwordValid && confirmationValid) {
          return;
        }

        event.preventDefault();
        if (!passwordValid) {
          passwordField.focus();
        } else if (confirmationField) {
          confirmationField.focus();
        }
      });
    });
  });
})();
