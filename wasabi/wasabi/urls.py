from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url('^u/register/', CreateView.as_view(
            template_name = 'registration/register.html',
            form_class = UserCreationForm,
            success_url = '/'
    ), name='register'),
    url('^u/', include('django.contrib.auth.urls')),
    #url(r'^u/logout/$', views.logout, name='logout'),
    #url(r'^u/register/$', views.register, name='register'),
    #url(r'^u/account/$', views.dashboard, name='dashboard'),
    url(r'^api/', include('directory.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
