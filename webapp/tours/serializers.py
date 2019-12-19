from rest_framework import serializers

from .models import Tour

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ["id", "purpose", "start_date", "end_date", "mode_of_travel", "ticket_cost", "origin_cab_fare", "destination_cab_fare",
                  "hotel_cost", "hotel_receipt", "conveyance", "approving_manager", "status", "additional_information",
                  "modified_date", "feedback_date", "created_by", "created_date"]
    