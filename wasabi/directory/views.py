from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import detail_route, list_route, permission_classes
from rest_framework.response import Response

from models import Series, Chapter
from django.contrib.auth.models import User
from serializers import SeriesSerializer, ChapterSerializer, UserSerializer
from permissions import IsStaffOrReadOnly, ChapterPermissions

"""
API endpoint for the User class
Users should not register or change their information through the API.
"""
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

"""API endpoing for the Series Class"""
class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = (IsStaffOrReadOnly,)

"""
API endpoint for the Chapter Class
The "Order" attribute has special behavior -- it always inserts into the list
of chapters.
"""
class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = (ChapterPermissions,)
    
    def perform_create(self, serializer):
        chapter = serializer.save()
        chapter.insertAt(serializer.validated_data['order'])

    def perform_update(self, serializer):
        chapter = serializer.save()
        chapter.insertAt(serializer.validated_data['order'])