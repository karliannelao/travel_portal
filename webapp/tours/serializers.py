from rest_framework import serializers

from .models import Tour
from employees.serializers import EmployeeSerializer

class TourSerializer(serializers.ModelSerializer):
    approving_manager_id = serializers.IntegerField(write_only=True)
    created_by_id = serializers.IntegerField(write_only=True)
    financial_manager_id = serializers.IntegerField(write_only=True)
    approving_manager = EmployeeSerializer(read_only=True)
    created_by = EmployeeSerializer(read_only=True)
    financial_manager = EmployeeSerializer(read_only=True)


    class Meta:
        model = Tour
        fields = ["id", "purpose", "start_date", "end_date", "mode_of_travel", "ticket_cost", "origin_cab_fare", "destination_cab_fare",
                  "hotel_cost", "hotel_receipt", "conveyance", "approving_manager_id", "approving_manager", "status", "additional_information",
                  "modified_date", "feedback_date", "created_by_id", "created_by", "created_date", "financial_manager_id", "remarks"]

    