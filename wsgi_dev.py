import os, sys
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'supalumni.settings.development'
#sys.path.append('/Users/zed/programmation/python/supalumni-net')
application = django.core.handlers.wsgi.WSGIHandler() 