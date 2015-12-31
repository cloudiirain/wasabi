from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .. views import SeriesViewSet
from rest_framework.authtoken import views as authviews

class AuthenticationTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_superuser(username='admin', email='admin@example.com', password='top_secret')
        self.token = Token.objects.get(user=self.user).key
        self.header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}
        
    def test_get_token(self):
        request = self.factory.post('/api/api-token-auth/', {'username': 'admin', 'password': 'top_secret'})
        response = authviews.obtain_auth_token(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, { 'token' : self.token })

    def test_create_series_authenticated(self):
        response = self.client.post('/api/series/', data={'title': 'OreShura'}, **self.header)
        self.assertEqual(response.status_code, 201)