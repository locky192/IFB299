from django.conf.urls import url
from CityApp import views
<<<<<<< Updated upstream
from django.contrib.auth import views as auth_views


=======
from django.contrib import admin
from django.contrib.auth import views as auth_views

>>>>>>> Stashed changes

urlpatterns = [
    url(r'^$', views.index, name='index'),
# <<<<<<< Updated upstream
    url(r'^register/$', views.register,
    name='register'),
<<<<<<< Updated upstream
	url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'CityApp/login.html'}, name='login'),
=======
    url(r'^login/$', auth_views.login, {'template_name':'CityApp/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name':'/CityApp/logout.html'},  name='logout'),
	# url(r'^user_login/$', views.user_login,
    # name='user_login'),
>>>>>>> Stashed changes
	url(r'^admin_login/$', views.admin_login,
    name='admin_login')
# =======
#     url(r'^login/$', auth_views.login, {'template_name':'CityApp/login.html'}, name='login'),
#     url(r'^logout/$', auth_views.logout, {'template_name':'/CityApp/logout.html'},  name='logout'),
#     url(r'^register/$', views.register_user,
#     name='register'),
#     url(r'^admin/', admin.site.urls),
#
# >>>>>>> Stashed changes
]
