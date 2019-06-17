
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

from .widget import *

default_app_config = 'team.Config'

try:
    from local_settings import APPS
except ImportError:
    pass

class Default(object):

    optgroup = 'Team'

    if 'team' in APPS:
        apps = [
            'team',
        ]

        widgets = [
            TeamWidget,
        ]

        plugins = [
            ('team.apps.team', _('Team members')),
        ]


class Config(AppConfig, Default):
    name = 'team'
    verbose_name = _("Team")

default = Default()
