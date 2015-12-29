from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import detail_route, list_route, permission_classes
from rest_framework.response import Response
from models import Series, Chapter
from django.contrib.auth.models import User
from serializers import SeriesSerializer, ChapterSerializer, UserSerializer

class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = (permissions.IsAuthenticated,)

"""
class SeriesViewSet(viewsets.ViewSet):

    queryset = Series.objects.all()

    @permission_classes([permissions.IsAdminUser, ])
    def list(self, request):
        queryset = Series.objects.all()
        serializer = SeriesSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
"""
"""
class SeriesList(generics.ListCreateAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SeriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
"""

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