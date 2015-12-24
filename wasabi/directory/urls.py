from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^series/$', views.SeriesList.as_view()),
    url(r'^series/(?P<pk>[0-9]+)/$', views.SeriesDetail.as_view()),
    url(r'^chapter/$', views.ChapterList.as_view()),
    url(r'^chapter/(?P<pk>[0-9]+)/$', views.ChapterDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)