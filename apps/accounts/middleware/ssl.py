
"""
SSL Middleware
Stephen Zabel

This middleware answers the problem of redirecting to (and from) a SSL secured path
by stating what paths should be secured in urls.py file. To secure a path, add the
additional view_kwarg 'SSL':True to the view_kwargs.

For example

urlpatterns = patterns('some_site.some_app.views',
    (r'^test/secure/$','test_secure',{'SSL':True}),
     )

All paths where 'SSL':False or where the kwarg of 'SSL' is not specified are routed
to an unsecure path.

For example

urlpatterns = patterns('some_site.some_app.views',
    (r'^test/unsecure1/$','test_unsecure',{'SSL':False}),
    (r'^test/unsecure2/$','test_unsecure'),
     )

Gotcha's : Redirects should only occur during GETs; this is due to the fact that
POST data will get lost in the redirect.

A major benefit of this approach is that it allows you to secure django.contrib views
and generic views without having to modify the base code or wrapping the view.

This method is also better than the two alternative approaches of adding to the
settings file or using a decorator.

It is better than the tactic of creating a list of paths to secure in the settings
file, because you DRY. You are also not forced to consider all paths in a single
location. Instead you can address the security of a path in the urls file that it
is resolved in.

It is better than the tactic of using a @secure or @unsecure decorator, because
it prevents decorator build up on your view methods. Having a bunch of decorators
makes views cumbersome to read and looks pretty redundant. Also because the all
views pass through the middleware you can specify the only secure paths and the
remaining paths can be assumed to be unsecure and handled by the middleware.

This package is inspired by Antonio Cavedoni's SSL Middleware
"""

__license__ = "Python"
__copyright__ = "Copyright (C) 2007, Stephen Zabel"
__author__ = "Stephen Zabel"


from django.conf import settings
from django.http import HttpResponseRedirect, get_host

SSL = 'SSL'

class SSLRedirect:
    def process_view(self, request, view_func, view_args, view_kwargs):
        if SSL in view_kwargs:
            asked_secure = view_kwargs[SSL]
            del view_kwargs[SSL]
        else:
            asked_secure = False
        
        request_is_https = False
        if request.META['UWSGI_SCHEME'] == "https":
            request_is_https = True
        
        if asked_secure and not request_is_https:
            return self._redirect_secure(request, asked_secure)
        
        if not asked_secure and request_is_https:
            return self._redirect_not_secure(request, asked_secure)
            
    def _redirect_not_secure(self, request, asked_secure):
        protocol = "http"
        newurl = "%s://%s%s" % (protocol, get_host(request),
										  request.get_full_path())
        return HttpResponseRedirect(newurl)
        
    def _redirect_secure(self, request, asked_secure):
        protocol = "https"
        newurl = "%s://%s%s" % (protocol, get_host(request),
										  request.get_full_path())
        
        return HttpResponseRedirect(newurl)
