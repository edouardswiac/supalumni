from django.conf.urls.defaults import *

urlpatterns = patterns('companies.views',
    url(r'^(?P<company_id>[\d]+)/$',    'company_detail',   name="companies-detail"),
    url(r'^add/$',                      'company_add',      name="companies-add"),

    url(r'^browse/alphabetical/$',      'company_list_alphabetical',                    name="companies-list-alphabetical"),
    url(r'^browse/alphabetical/(?P<first_letter>[\w-]+)/$', 'company_list_alphabetical',name="companies-list-alphabetical"),
    
    url(r'^browse/map/$',               'company_list_map',         name="companies-list-map"),
    

)