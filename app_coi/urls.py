from django.conf.urls import patterns, include, url
from app_coi import views

urlpatterns = patterns('',
	# Index page
 	url(r'^$', views.IndexView.as_view(), name='index'),
)


