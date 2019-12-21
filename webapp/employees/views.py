from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Employee
from .serializers import EmployeeSerializer


class ApprovingManagerView(ListAPIView):
    permission_classes = (IsAuthenticated, )

    queryset = Employee.objects.filter(position="Manager")
    serializer_class = EmployeeSerializer
