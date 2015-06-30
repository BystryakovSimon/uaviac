from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('media.views',
    url(r'^$', 'gallery'),
    url(r'^(?P<gallery_id>\d+)/$', 'gallery_id'),
)