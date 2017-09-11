from django.conf.urls import url
from CityApp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register,
    name='register'),
	url(r'^user_login/$', views.user_login,
    name='user_login'),
	url(r'^admin_login/$', views.admin_login,
    name='admin_login')
]
