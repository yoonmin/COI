from django.conf.urls import patterns, include, url
from app_coi import views

urlpatterns = patterns('',
	# Index page
 	url(r'^$', views.IndexView.as_view(), name='index'),

 	# About pages
 	url(r'^about$', views.AboutView.as_view(), name='about'),
 	url(r'^papers$', views.PaperListView.as_view(), name='papers'),
 	url(r'^featured$', views.FeaturedView.as_view(), name='featured'),
	url(r'^featured/(?P<slug>.*)$', views.FeaturedDetailView.as_view(), name='featured_detail'),
 	
 	# People pages
 	url(r'^faculty$', views.FacultyView.as_view(), name='faculty'),
 	url(r'^student$', views.StudentView.as_view(), name='student'),
 	url(r'^scholar$', views.ScholarView.as_view(), name='scholar'),

 	# Event pages
 	url(r'^event$', views.EventView.as_view(), name='event'),

 	# Contact page
 	url(r'^contact$', views.ContactView.as_view(), name='contact'),
)


