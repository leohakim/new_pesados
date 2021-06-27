from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreAppConfig(AppConfig):
    name = 'pesados_el_norte.core_app'
    verbose_name = _("Core App")

    def ready(self):
        try:
            import pesados_el_norte.users.signals  # noqa F401
        except ImportError:
            pass
