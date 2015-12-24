from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

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

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ChapterList(APIView):
    """
    List all chapters, or create a new chapter.
    Note that specifying an order causes the other chapters in the series to be reordered automatically.
    """
    def get(self, request, format=None):
        snippets = Chapter.objects.all()
        serializer = ChapterSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChapterSerializer(data=request.data)
        if serializer.is_valid():
            chapter = serializer.save()
            chapter.insertAt(serializer.validated_data['order'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChapterDetail(APIView):
    """
    Retrieve, update or delete a chapter instance.
    Note that specifying an order causes the other chapters in the series to be reordered automatically
    """
    def get_object(self, pk):
        try:
            return Chapter.objects.get(pk=pk)
        except Chapter.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        chapter = self.get_object(pk)
        serializer = ChapterSerializer(chapter)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ChapterSerializer(snippet, data=request.data)
        if serializer.is_valid():
            chapter = serializer.save()
            chapter.insertAt(serializer.validated_data['order'])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        series = self.get_object(pk)
        series.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)