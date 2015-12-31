from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .. views import SeriesViewSet

class UserTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_superuser(username='admin', email='admin@example.com', password='top_secret')
        self.token = Token.objects.get(user=self.user).key
        self.header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
    
    def test_list_users_anonymous(self):
        pass
    
    def test_get_user_anonymous(self):
        pass
    
    def test_create_user_superuser(self):
        pass
    
    def test_update_user_superuser(self):
        pass
    
    def test_delete_user_superuser(self):
        pass

class SeriesTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_superuser(username='admin', email='admin@example.com', password='top_secret')
        self.token = Token.objects.get(user=self.user).key
        self.header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}

    def test_list_series_anonymous(self):
        request = self.factory.get('/api/series/')
        response = SeriesViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)

    def test_get_series_anonymous(self):
        pass

    def test_create_series_anonymous(self):
        request = self.factory.post('/api/series/', {'title': 'OreShura'})
        response = SeriesViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 401)

    def test_create_series_authenticated(self):
        request = self.factory.post('/api/series', data={'title': 'OreShura'})
        force_authenticate(request, user=self.user)
        response = SeriesViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 201)

    def test_update_user_superuser(self):
        pass
    
    def test_delete_user_superuser(self):
        pass
    
class ChapterTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_superuser(username='admin', email='admin@example.com', password='top_secret')
        self.token = Token.objects.get(user=self.user).key
        self.header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
    
    def test_list_chapters_anonymous(self):
        pass
    
    def test_get_chapters_anonymous(self):
        pass
    
    def test_create_chapter_authenticated(self):
        pass
    
    def test_update_chapter_superuser(self):
        pass
    
    def test_delete_chapter_superuser(self):
        pass