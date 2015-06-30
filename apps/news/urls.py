from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('news.views',
    url(r'^$', 'news'),
    url(r'^(?P<news_id>\d+)/$', 'news_id'),
)