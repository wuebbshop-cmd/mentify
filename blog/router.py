from django.conf import settings


class BlogDatabaseRouter:
    """
    Routes blog app models (Category, Post) to the substitute database
    when SUB_DB credentials are configured, falling back gracefully to default.
    """

    route_app_labels = {"blog"}

    def _target_db(self):
        return "substitute" if "substitute" in getattr(settings, "DATABASES", {}) else "default"

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self._target_db()
        return "default"

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self._target_db()
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, **hints):
        if app_label in self.route_app_labels:
            target = self._target_db()
            return db == target
        return db == "default"
