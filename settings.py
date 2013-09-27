# -*- encoding: utf-8 -*-
import os

from wafer.settings import *

try:
    from localsettings import *
except ImportError:
    pass

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

pyconzadir = os.path.dirname(__file__)


STATICFILES_DIRS = (
    os.path.join(pyconzadir, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(pyconzadir, 'templates'),
) + TEMPLATE_DIRS


WAFER_MENUS += (
    {"menu": "about", "label": _("About"),
     "items": []},
    {"menu": "sponsors", "label": _("Sponsors"),
     "items": [
         {"name": "praekelt", "label": _(u"» Praekelt ★"),
          "url": reverse_lazy("wafer_sponsor", args=(5,))},
         {"name": "sponsors", "label": _("Our sponsors"),
          "url": reverse_lazy("wafer_sponsors")},
         {"name": "packages", "label": _("Sponsorship packages"),
          "url": reverse_lazy("wafer_sponsorship_packages")},
     ]},
    {"menu": "talks", "label": _("Talks"),
     "items": [
         {"name": "schedule", "label": _("Schedule"),
          "url": reverse_lazy("wafer_page", args=('talks/schedule',))},
         {"name": "accepted-talks", "label": _("Accepted Talks"),
          "url": reverse_lazy("wafer_users_talks")},
     ]},
    {"menu": "news", "label": _("News"),
     "items": []},
    {"name": "contact", "label": _("Contact"),
     "url": reverse_lazy("wafer_page", args=('contact',))},
    {"menu": "previous-pycons", "label": _("Past PyConZAs"),
     "items": [
         {"name": "pyconza2012", "label": _("PyConZA 2012"),
          "url": "http://za.pycon.org/2012/"},
     ]},
    {"name": "twitter", "label": "Twitter",
     "image": "/static/img/twitter.png",
     "url": "https://twitter.com/pyconza"},
)

INSTALLED_APPS = (
    'disqus',
) + INSTALLED_APPS

DISQUS_WEBSITE_SHORTNAME = "pyconza"
