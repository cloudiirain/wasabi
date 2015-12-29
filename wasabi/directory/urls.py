from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as authviews
from . import views

router = routers.SimpleRouter()
router.register(r'series', views.SeriesViewSet)

urlpatterns = [
    #url(r'^series/$', views.SeriesList.as_view()),
    #url(r'^series/(?P<pk>[0-9]+)/$', views.SeriesDetail.as_view()),
    url(r'^chapter/$', views.ChapterList.as_view()),
    url(r'^chapter/(?P<pk>[0-9]+)/$', views.ChapterDetail.as_view()),
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)