from django.conf.urls import url
from CityApp import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.admin import AdminSite

AdminSite.login_template = 'CityApp/admin_login.html'
# admin.site.login_template = '/CityApp/admin_login.html'
# admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register,
    name='register'),
    url(r'^signed/$', views.signed, name='signed'),
	url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'CityApp/login.html'}, name='login'),
	url(r'^admin/login/$', auth_views.login, {'template_name': 'CityApp/admin_login.html'}, name='admin_login'),
    url(r'^admin/', admin.site.urls),
]
