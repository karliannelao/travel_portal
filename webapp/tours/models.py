from django.db import models

from employees.models import Employee
    
class Tour(models.Model):
    TOUR_STATUS_CHOICES = (
        ("Draft", "Draft"),
        ("Submitted", "Submitted"),
        ("Submitted to Finance", "Submitted to Finance"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Request for Information", "Request for Information")
    )

    purpose = models.TextField(null=False)
    start_date = models.DateField(null=False) 
    end_date = models.DateField(null=False)   
    mode_of_travel = models.CharField(max_length=50, null=False)
    ticket_cost = models.CharField(max_length=10, null=False)
    origin_cab_fare =  models.CharField(max_length=10, null=False)
    destination_cab_fare = models.CharField(max_length=10, null=False)
    hotel_cost = models.CharField(max_length=10, null=False)
    hotel_receipt = models.ImageField(upload_to="images/", null=True, blank=True)
    conveyance = models.CharField(max_length=255)
    additional_information = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="created_tours")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    approving_manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="approved_tours", null=True, blank=True)
    status = models.CharField(max_length=25, choices=TOUR_STATUS_CHOICES, default="Draft")  
    feedback_date = models.DateTimeField(null=True, blank=True)
    financial_manager = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='financially_approved_tours', null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)