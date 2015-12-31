from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as authviews
from . import views

router = routers.SimpleRouter()
router.register(r'series', views.SeriesViewSet)
router.register(r'chapters', views.ChapterViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^api-token-auth/', authviews.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)