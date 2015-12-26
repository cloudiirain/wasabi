from rest_framework import generics, permissions
from models import Series, Chapter
from django.contrib.auth.models import User
from serializers import SeriesSerializer, ChapterSerializer, UserSerializer

class SeriesList(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ChapterList(generics.ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    """
    Save method is overridden so insertion behavior is the default
    """
    def perform_create(self, serializer):
        chapter = serializer.save()
        chapter.insertAt(serializer.validated_data['order'])

class ChapterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    """
    Save method is overridden so insertion behavior is the default
    """
    def perform_update(self, serializer):
        chapter = serializer.save()
        chapter.insertAt(serializer.validated_data['order'])