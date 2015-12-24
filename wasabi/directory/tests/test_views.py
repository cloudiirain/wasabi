from django.test import TestCase, client

from django.contrib.auth.models import User

class RegistrationTest(TestCase):
    def setUp(self):
        User.objects.create(username="admin", email="admin@example.com", password="admin")

    def test_details(self):
        """
        # Issue a GET request.
        response = self.client.get('/customer/details/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.context['customers']), 5)
        """
        pass

