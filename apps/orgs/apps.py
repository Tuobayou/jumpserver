from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class OrgsConfig(AppConfig):
    name = 'orgs'
    verbose_name = _('App organizations')

    def ready(self):
        from . import tasks
        from . import signal_handlers
