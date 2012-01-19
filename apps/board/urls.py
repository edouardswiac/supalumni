from django.conf.urls.defaults import *

urlpatterns = patterns('board.views',
    url(r'^$',                                 'post_list',    name="board_post_list"),
    url(r'^post/(?P<post_id>[\d]+)/$',         'post_detail',  name="board_post_detail"),
    url(r'^post/add/$',                        'post_create',  name="board_post_create"),
    url(r'^post/(?P<post_id>[\d]+)/edit$',     'post_update',  name="board_post_update"),
    url(r'^post/(?P<post_id>[\d]+)/delete/$',  'post_delete',  name="board_post_delete"),
    url(r'^posts/$',                           'manage_posts', name="board_post_manage"),
)