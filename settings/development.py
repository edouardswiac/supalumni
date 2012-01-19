#############################################
# DEVELOPMENT SETTINGS (overrides common.py)#
#############################################
#from .common import *
from . import common; common._merge(vars())

HOSTNAME = "http://localhost:8000"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# for debug-toolbar
INTERNAL_IPS = ('127.0.0.1',)

#################
# DATABASE
#################
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME' : 'supalumni',                     # Or path to database file if using sqlite3.
        'USER' : 'supalumni',                            # Not used with sqlite3.
        'PASSWORD' : 'supalumni',                        # Not used with sqlite3.
        'HOST' : 'localhost',                                # Set to empty string for localhost. Not used with sqlite3.
        'PORT' : '',                                # Set to empty string for default. Not used with sqlite3.
    }
}

# MEDIAS
# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_ROOT / "static"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES +(
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
TEMPLATE_DIRS = TEMPLATE_DIRS + (
    '/Users/zed/programmation/python/debug_toolbar/templates',
)
INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

LOGIN_EXEMPT_URLS = LOGIN_EXEMPT_URLS + (r'^__debug__/', )
