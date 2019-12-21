from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from employees.models import Employee

# Create your tests here.


class EmployeesTest(TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/approving_managers/"
        self.employee = Employee.objects.create(
            first_name="Employee",
            last_name="1",
            username="Employee1",
            position="Regular")
        self.client = APIClient()
        self.token = Token.objects.get(user=self.employee)
        self.authtoken = "Token " + self.token.key
        self.client.credentials(HTTP_AUTHORIZATION=self.authtoken)

    def test_get_all_approving_managers(self):
        r = self.client.get(self.url, content_type="application/json")
        self.assertEquals(r.status_code, 200)
