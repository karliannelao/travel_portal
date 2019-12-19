from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Tour, Employee
from .serializers import TourSerializer

class TourView(APIView):
    #authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )
    
    def get(self, request):
        user = request.user
        
        if(user.position == "manager"):
            queryset = Tour.objects.filter(approving_manager=user)
        elif(user.position == "finance_manager"):
            queryset = Tour.objects.filter(status="approved")
        else:
            queryset = Tour.objects.filter(created_by=user)
            
        serializer = TourSerializer(queryset, many=True)
        print(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_200_OK, content_type="application/json")
        #return Response(status=status.HTTP_200_OK)