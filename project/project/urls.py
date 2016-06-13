from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from app.views import main, order, info	

urlpatterns = patterns('',
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^order/?$', order),
    #url(r'^(\d{1,10})/(\w{1,10})/$', sorted_main),
    #url(r'^$', f_main),
    url(r'^info/$', info),
    url(r'^(\d)*/?(\w{0,10})/?$', main),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
