from django.utils.translation import ugettext_lazy as _

from .common import Asset


class Host(Asset):
    class Meta:
        verbose_name = _("Host")
