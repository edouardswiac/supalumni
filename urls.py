from django.conf.urls.defaults import *
from settings import development

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$',             'accounts.views.account_login', {'SSL':True}),
    (r'^account/',     include('accounts.urls'),  {'SSL':True}),
    (r'^profiles/',     include('profiles.urls')),
    (r'^companies/',    include('companies.urls')),
    #(r'^board/',        include('board.urls')),
    (r'^nimda/',        include(admin.site.urls), {'SSL':True}),
    (r'^tinymce/',      include('tinymce.urls'),),
    (r'^robots\.txt$', 'django.views.generic.simple.direct_to_template', {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/img/favicon.ico'}),
)

if development.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
                                   {'document_root': development.MEDIA_ROOT, 'show_indexes' : True}),
    )
