from django.conf.urls.defaults import patterns, url
from .views import calculate_distance


urlpatterns = patterns('',
	url(r'calculate', calculate_distance),
)
