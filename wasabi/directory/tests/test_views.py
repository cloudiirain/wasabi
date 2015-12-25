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

    """
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

