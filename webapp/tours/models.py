from django.db import models
from django.contrib.auth.models import AbstractUser



class Employee(AbstractUser):
    EMPLOYEE_TYPE_CHOICES = (
        ("regular", "Regular"),
        ("manager", "Manager"),
        ("finance_manager", "Finance Manager")
    )

    position = models.CharField(max_length=20, choices=EMPLOYEE_TYPE_CHOICES, default="regular")
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Tour(models.Model):
    TOUR_STATUS_CHOICES = (
        ("draft", "Draft"),
        ("submitted", "Submitted"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
        ("request_for_information", "Request for Information")
    )

    purpose = models.TextField(null=False)
    start_date = models.DateField(null=False) 
    end_date = models.DateField(null=False)   
    mode_of_travel = models.CharField(max_length=50, null=False)
    ticket_cost = models.CharField(max_length=10, null=False)
    origin_cab_fare =  models.CharField(max_length=10, null=False)
    destination_cab_fare = models.CharField(max_length=10, null=False)
    hotel_cost = models.CharField(max_length=10, null=False)
    hotel_receipt = models.ImageField(upload_to="images/", null=True)
    conveyance = models.CharField(max_length=255)
    approving_manager = models.ForeignKey(Employee, null=True, on_delete=models.CASCADE, related_name="approved_tours")
    status = models.CharField(max_length=25, choices=TOUR_STATUS_CHOICES, default="draft")
    additional_information = models.TextField(null=True)
    modified_date = models.DateTimeField()
    feedback_date = models.DateTimeField(null=True)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="created_tours")
    created_date = models.DateTimeField(auto_now_add=True)
    
