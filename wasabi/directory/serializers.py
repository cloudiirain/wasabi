from rest_framework import serializers
from models import Series, Chapter
from django.contrib.auth.models import User

class SeriesSerializer(serializers.ModelSerializer):
    pages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Series
        fields = ('id', 'title', 'chapters')
        
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'series', 'owner', 'title', 'order', 'body',)
        
class UserSerializer(serializers.ModelSerializer):
    chapters = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'chapters')