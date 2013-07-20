import os

from wafer.settings import *

try:
    from localsettings import *
except ImportError:
    pass

pyconzadir = os.path.dirname(__file__)

STATICFILES_DIRS = (
    os.path.join(pyconzadir, 'static'),
) + STATICFILES_DIRS
