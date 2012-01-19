#############################################
# PRODUCTION SETTINGS (overrides common.py) #
#############################################
#from .common import *
from . import common; common._merge(vars())

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SEND_BROKEN_LINK_EMAILS = True
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

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT =  PROJECT_ROOT / "static"   

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
