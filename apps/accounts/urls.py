from django.conf.urls.defaults import *

urlpatterns = patterns('accounts.views',
    url(r'^$',                              'account_detail',           name="accounts-detail"),
    url(r'^update/$',                       'account_update',           name="accounts-update"),
    #url(r'^login/$',                        'account_login',           name="accounts-login"),
    url(r'^logout/$',                       'account_logout',           name="accounts-logout"),
    url(r'^bookmarks/$',                     'bookmarks_list',           name="accounts-bookmarks-list"),
    url(r'^bookmarks/delete/$',             'bookmarks_delete',         name="accounts-bookmarks-delete"),
    url(r'^bookmarks/add/(?P<profile_id>[\d]+)/$','bookmarks_add',      name="accounts-bookmarks-add"),
    url(r'^register/$',                     'register_initiate',        name="accounts-register-initiate"),
    url(r'^register/rules$',                     'register_rules',        name="accounts-register-rules"),
    url(r'^register/(?P<id_booster>[\d]+)/(?P<key>\w{40})/$',    'register_complete',         name="accounts-register-complete"),
)

urlpatterns += patterns('companies.views',
    url(r'^positions/add/$',     'position_add',        name="companies-positions-add"),
    url(r'^positions/$',  'position_manage',     name="companies-positions-manage"),
    url(r'^positions/delete/$',  'position_delete',     name="companies-positions-delete"),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^password/reset/$',             'password_reset',             name='accounts-forgot-password1'),
    url(r'^password/reset/done/$',        'password_reset_done',        name='accounts-forgot_password2'),
    url(r'^password/reset/complete/$',    'password_reset_complete',    name='accounts-forgot_password4'),
    url(r'^password/reset/confirm/(?P<uidb36>[-\w]+)/(?P<token>[-\w]+)/$','password_reset_confirm', name='accounts-forgot-password3'),
    url(r'^password/change/$',      'password_change',            name='accounts-password-change'),
    url(r'^password/change/done/$', 'password_change_done',       name='accounts-password-change-done'),
)