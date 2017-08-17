from django.conf.urls import url, include
from . import views
urlpatterns = [
	url(r'^$', views.home_page, name='home_page'),
	url(r'^add/$', views.add_entry, name='add_entry'),
	url(r'^about/$', views.about_page, name='about_page'),
]
