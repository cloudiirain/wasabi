from rest_framework import generics, permissions
from models import Series, Page
from django.contrib.auth.models import User
from serializers import SeriesSerializer, PageSerializer, UserSerializer

class SeriesList(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
class PageList(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)