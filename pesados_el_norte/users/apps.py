from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "pesados_el_norte.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import pesados_el_norte.users.signals  # noqa F401
        except ImportError:
            pass
