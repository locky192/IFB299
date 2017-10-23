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
    url(r'^infopage/$', views.info_page, name='infopage'),
    url(r'^landmark/(?P<landmark_name_slug>[\w\-]+)/$', views.show_landmark, name='show_landmark'),
	url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'CityApp/login.html'}, name='login'),
	url(r'^admin/login/$', auth_views.login, {'template_name': 'CityApp/admin_login.html'}, name='admin_login'),
    url(r'^admin/', admin.site.urls),url(r'^button/$',views.button, name='button'),
	url(r'^button_function/$',views.button_function, name= 'button_function'),
    url(r'^xml_page/$',views.xml_page, name= 'xml'),
    url(r'^account/update/$', views.update_profile, name='update'),
]
