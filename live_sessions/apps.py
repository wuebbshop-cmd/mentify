from django.apps import AppConfig


class SessionsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "live_sessions"
    verbose_name = "Live Sessions"

    def ready(self):
        # Avoid clashing with Django's built-in sessions framework
        pass
