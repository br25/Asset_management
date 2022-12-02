from rest_framework import generics, status, views

from rest_framework.response import Response

from companies.models import Company
from .models import Employee
from .serializers import EmployeeSerializer
from .permissions import IsCompanyEmployee


class EmployeeList(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


    def get_queryset(self):
        queryset = super(EmployeeList, self).get_queryset()
        queryset = queryset.filter(company__owner=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        user = self.request.user
        company = Company.objects.get(owner=user)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(company=company)
        return Response(serializer.data)


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsCompanyEmployee]
