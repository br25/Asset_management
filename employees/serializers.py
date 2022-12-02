from rest_framework import serializers
from .models import Employee



class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source="company.name", read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

