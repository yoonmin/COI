from django.conf.urls import patterns, include, url
from app_coi import views

urlpatterns = patterns('',
	# Index page
 	url(r'^$', views.IndexView.as_view(), name='index'),

 	# About pages
 	url(r'^about$', views.AboutView.as_view(), name='about'),
 	
 	# People pages
 	url(r'^faculty$', views.FacultyView.as_view(), name='faculty'),
 	url(r'^student$', views.StudentView.as_view(), name='student'),
 	url(r'^scholar$', views.ScholarView.as_view(), name='scholar'),
 	url(r'^alumni$', views.AlumniView.as_view(), name='alumni'),

 	# Event pages
 	url(r'^event$', views.EventView.as_view(), name='event'),
)


