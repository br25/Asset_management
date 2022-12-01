from django.db import models
from companies.models import Company
from employees.models import Employee
from core.enums import AssetsType, Status, HandoverStatus, ConditionStatus


class Asset(models.Model):
    title = models.CharField(max_length=255)
    serial_no = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    types = models.CharField(max_length=255, choices=AssetsType.choices)
    owner = models.ForeignKey(
        Company, related_name='company', on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=Status.choices)
    is_assigned = models.BooleanField(default=False)


class AssetDeligation(models.Model):
    handover_at = models.DateTimeField()
    handover_type = models.CharField(max_length=255, choices=HandoverStatus.choices)
    reason = models.TextField(max_length=255)
    condition = models.CharField(max_length=255, choices=ConditionStatus.choices)
    asset = models.ForeignKey(Asset, related_name="asset", on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name="employee_asset", on_delete=models.SET_NULL, null=True)