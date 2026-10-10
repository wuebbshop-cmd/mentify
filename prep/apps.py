from django.apps import AppConfig


class PrepConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prep'
    verbose_name = 'Mentify Prep'

    def ready(self):
        import prep.signals  # noqa: F401
        from services.local_prep_worker import start_local_prep_workers
        start_local_prep_workers()
