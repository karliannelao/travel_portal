from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    EMPLOYEE_TYPE_CHOICES = (
        ("Regular", "Regular"),
        ("Manager", "Manager"),
        ("Finance Manager", "Finance Manager")
    )

    position = models.CharField(
        max_length=20,
        choices=EMPLOYEE_TYPE_CHOICES,
        default="Regular")

    def __str__(self):
        return self.first_name + " " + self.last_name
