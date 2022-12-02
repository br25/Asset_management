from django.db import models
from companies.models import Company
from employees.models import Employee
from core.enums import AssetsType, Status, Condition


class Asset(models.Model):
    title = models.CharField(max_length=255)
    serial_no = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    types = models.CharField(max_length=255, choices=AssetsType.choices)
    owner = models.ForeignKey(
        Company, related_name='company', on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=Status.choices, default=Status.NEW)
    is_assigned = models.BooleanField(default=False)


class AssetDelegation(models.Model):
    given_at = models.DateField(auto_now_add=True)
    expire_at = models.DateField(blank=True, null=True)
    reason = models.TextField(max_length=255)
    condition = models.CharField(max_length=255, choices=Condition.choices)
    asset = models.ForeignKey(Asset, related_name="asset", on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name="employee_asset", on_delete=models.SET_NULL, null=True)
    is_returned = models.BooleanField(default=False)
