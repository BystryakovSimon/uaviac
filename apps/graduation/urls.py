from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('graduation.views',
    url(r'^$', 'graduation'),
    url(r'^(?P<year>\d+)/$', 'graduation_year'),
)