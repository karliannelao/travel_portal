from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Tour, Employee
from .serializers import TourSerializer

class TourView(APIView):
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
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.user
        data = request.data
        data['created_by_id'] = user.id
        serializer = TourSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = request.data
        serailizer = TourSerializer(data=data, partial=True)
        if serializer.is_valid():
            return Reponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        