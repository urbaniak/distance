from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('',
	url(r'^api/', include('api.urls')),
	url(r'^', include('website.urls')),
)
