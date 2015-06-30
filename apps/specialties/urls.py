from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('specialties.views',
    url(r'^$', 'specialty'),
    url(r'^(?P<cipher>\d+)/$', 'specialty_cipher'),
)