from django.db import models
from companies.models import Company

# from .enums import ConditionStatus

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    contact = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    company = models.ForeignKey(
        Company, related_name='company_name', on_delete=models.CASCADE)


