from django.conf.urls.defaults import *
from django.contrib.auth import views as auth_views

urlpatterns = patterns('profiles.views',
    url(r'^(?P<profile_id>[\d]+)/$',                        'profile_detail',       name="profiles-detail"),
    url(r'^browse/alphabetical/$',                          'list_alphabetical',    name="profiles-list-alphabetical"),
    url(r'^browse/alphabetical/(?P<first_letter>[\w-]+)/$', 'list_alphabetical',    name="profiles-list-alphabetical"),
    url(r'^browse/promotions/$',                            'list_promotions',      name='profiles-list-promotions'),
    url(r'^browse/promotions/(?P<promotion>[\d]{4})/$',     'list_promotions',      name='profiles-list-promotions'),

)


