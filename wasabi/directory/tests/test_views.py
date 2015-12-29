from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from .. views import SeriesViewSet

class SeriesTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user(username='admin', email='admin@example.com', password='top_secret')
        self.token = Token.objects.get(user=self.user).key
        self.header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token)}

    def test_list_series_anonymous(self):
        request = self.factory.get('/api/series/')
        response = SeriesViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 401)

    def test_list_series_authenticated(self):
        request = self.factory.get('/api/series/')
        force_authenticate(request, user=self.user)
        response = SeriesViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)

    def test_create_series_anonymous(self):
        request = self.factory.post('/api/series/', {'title': 'OreShura'})
        response = SeriesViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 401)

    def test_create_series_authenticated(self):
        request = self.factory.post('/api/series', data={'title': 'OreShura'})
        force_authenticate(request, user=self.user)
        response = SeriesViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 201)


"""
class RegistrationTest(TestCase):
    def test_registration_anyuser(self):
        factory = APIRequestFactory()
        request = factory.post('/api/user/', {'username': 'john', 'password': 'smith'})
        response = UserList.as_view()(request)
        self.assertEqual(response.status_code, 201)

    def test_registration_anyuser_username_already_exists(self):
        User.objects.create(username="admin", email="admin@example.com", password="admin")
        factory = APIRequestFactory()
        request = factory.post('/api/user/', {'username': 'admin', 'password': 'smith'})
        response = UserList.as_view()(request)
        self.assertEqual(response.status_code, 400)

class ListUserTest(TestCase):
    def setUp(self):
        User.objects.create(username="admin", email="admin@example.com", password="admin")

    def test_listusers_anyuser(self):
        factory = APIRequestFactory()
        request = factory.get('/api/user/')
        response = UserList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_details(self):

        # Issue a GET request.
        response = self.client.get('/customer/details/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.context['customers']), 5)
    if new_form.is_valid:
    payload= {"createNewUser":
              { "users": request.POST["newusers"],
                "email": request.POST["newemail"]
                }
              }

    headers =  {'content-type' : 'application/json',
                'Authorization': 'Token 6b929e47f278068fe6ac8235cda09707a3aa7ba1'}

    r = requests.post('http://localhost:8000/api/v1.0/user_list',
                      data=json.dumps(payload),
                      headers=headers, verify=False)
"""

