import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'supalumni.settings.production'
import django.core.handlers.wsgi
    
application = django.core.handlers.wsgi.WSGIHandler()
