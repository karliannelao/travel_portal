import requests
import json
from django.test import TestCase
from django.conf import settings
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from employees.models import Employee
from tours.models import Tour


# Create your tests here.
class ToursTest(TestCase):

    def setUp(self):
        self.url = settings.WEBAPP_DOMAIN + "/tours/"
        self.employee = Employee.objects.create(
            first_name="Employee",
            last_name="1",
            username="employee1",
            position="Regular")
        self.manager = Employee.objects.create(
            first_name="Manager",
            last_name="1",
            username="manager1",
            position="Manager")
        self.tour = Tour.objects.create(
            purpose="Convention",
            start_date="2019-12-08",
            end_date="2019-12-28",
            mode_of_travel="plane",
            ticket_cost="$400.00",
            origin_cab_fare="$200.00",
            destination_cab_fare="$200.00",
            hotel_cost="$500.00",
            conveyance="bus",
            created_by_id=self.employee.id)
        self.client = APIClient()
        self.token = Token.objects.get(user=self.employee)
        self.authtoken = "Token " + self.token.key
        self.client.credentials(HTTP_AUTHORIZATION=self.authtoken)

    def test_add_tours(self):
        data = {
            "purpose": "Business Meeting",
            "start_date": "2019-12-21",
            "end_date": "2019-12-30",
            "mode_of_travel": "plane",
            "ticket_cost": "$200.00",
            "origin_cab_fare": "$75.00",
            "destination_cab_fare": "$80.00",
            "hotel_cost": "$150.00",
            "conveyance": "train",
            "created_by_id": self.employee.id
        }
        r = self.client.post(
            self.url,
            json.dumps(data),
            content_type="application/json")
        self.assertEquals(r.status_code, 201)

    def test_get_all_tours(self):
        r = self.client.get(self.url, content_type="application/json")
        self.assertEquals(r.status_code, 200)

    def test_get_a_tour(self):
        r = self.client.get(self.url + str(self.tour.pk) +
                            "/", content_type="application/json")
        self.assertEquals(r.status_code, 200)

    def test_put_tours(self):
        data = {
            "status": "Submitted",
            "approving_manager_id": self.manager.id,
        }
        r = self.client.put(self.url + str(self.tour.pk) + "/",
                            data=json.dumps(data), content_type="application/json")
        self.assertEquals(r.status_code, 200)
