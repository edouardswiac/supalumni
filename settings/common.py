#############################################
# COMMON SETTINGS                           #
#############################################

import sys
from path import path

PROJECT_ROOT = path(__file__).abspath().dirname().dirname()
SITE_ROOT = PROJECT_ROOT.dirname()

sys.path.append(SITE_ROOT)
sys.path.append(PROJECT_ROOT / 'apps')
#sys.path.append(PROJECT_ROOT / 'libs')

ADMINS = (
    ('Edouard SWIAC', 'teh.fluffy.cat@gmail.com'),
)
MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'i*l6q#=00vt3bq4y0k=5v15raf$_v4_iygq^9w!0c7+9mjhvlo'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'accounts.middleware.loginrequired.LoginRequiredMiddleware',
    'accounts.middleware.ssl.SSLRedirect',
)

ROOT_URLCONF = 'supalumni.urls'

TEMPLATE_DIRS = (
    PROJECT_ROOT / "templates",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    #"django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    #'django.contrib.webdesign',
    'tinymce',
    'companies',
    'profiles',
    'addresses',
    #'board',
    'accounts',
    'django_countries',
)

AUTH_PROFILE_MODULE = "users.Profile"
LOGIN_URL = "/"
LOGIN_EXEMPT_URLS = (
    r'^static/', 
    r'^nimda/',
    r'^$',
    r'^accounts/register/',
    r'^accounts/password/',
)

DEFAULT_FROM_EMAIL = "contact@supalumni.net"
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'edouard'
#EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25
#EMAIL_USE_TLS = True

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,spellchecker,paste,searchreplace",
    'theme': "advanced",
    'theme_advanced_buttons1' : "bold,italic,underline,link,unlink,bullist,numlist",
    'theme_advanced_buttons2' : "",
    'theme_advanced_buttons3' : "",
    'theme_advanced_toolbar_location' : "top",
}
TINYMCE_SPELLCHECKER = False

def _merge(local_vars):
    local_vars.update((k, v) for k, v in globals().items() if k[0] != '_')
