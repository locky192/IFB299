from django.conf.urls import url
from CityApp import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register,
    name='register'),
	url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'CityApp/login.html'}, name='login'),
	url(r'^admin_login/$', views.admin_login,
    name='admin_login')
]
