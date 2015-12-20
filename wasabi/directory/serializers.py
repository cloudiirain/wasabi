from rest_framework import serializers
from directory.models import Series, Page
from django.contrib.auth.models import User

class SeriesSerializer(serializers.ModelSerializer):
    pages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Series
        fields = ('id', 'title', 'pages')
        
class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'series', 'owner', 'title', 'order', 'body',)
        
class UserSerializer(serializers.ModelSerializer):
    pages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'pages')