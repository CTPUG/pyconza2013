import os

from wafer.settings import *

try:
    from localsettings import *
except ImportError:
    pass

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

pyconzadir = os.path.dirname(__file__)


STATICFILES_DIRS = (
    os.path.join(pyconzadir, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(pyconzadir, 'templates'),
) + TEMPLATE_DIRS


WAFER_MENUS += (
    {"name": "sponsors", "label": _("Sponsors"),
     "items": [
         {"name": "sponsors", "label": _("Our sponsors"),
          "url": reverse("wafer_sponsors")},
         {"name": "packages", "label": _("Sponsorship packages"),
          "url": reverse("wafer_sponsorship_packages")},
     ]},
    {"name": "talks", "label": _("Talks"),
     "url": reverse("wafer_users_talks")},
    {"name": "contact", "label": _("Contact"),
     "url": reverse("wafer_page", args=('contact',))},
)
