from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns(''
    , url(r'^$', 'books.views.books')
    , url(r'^logout_user/$', 'lib.views.logout_user')
    , url(r'^auth/', 'lib.views.auth')
#    , url(r'^literatura/', 'lib.views.auth')
)