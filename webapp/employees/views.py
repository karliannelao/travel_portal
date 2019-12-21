from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from .models import Employee
from .serializers import EmployeeSerializer

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id, 'username': token.user.username})
        
class ApprovingManagerView(ListAPIView):
    permission_classes = (IsAuthenticated, )

    queryset = Employee.objects.filter(position="Manager")
    serializer_class = EmployeeSerializer
