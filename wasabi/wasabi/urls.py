from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from . import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url('^accounts/register/', CreateView.as_view(
            template_name = 'registration/register.html',
            form_class = UserCreationForm,
            success_url = '/'
    ), name='register'),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/dashboard/$', views.dashboard, name='dashboard'),
    url(r'^accounts/draft/$', views.chapter, name='chapter-create'),
    url(r'^accounts/draft/(?P<pk>\d+)/$', views.chapter, name='chapter-update'),
    url(r'^api/', include('directory.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
