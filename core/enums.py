from enum import Enum
from django.db import models 


class AssetsType(models.TextChoices):
    PHONE = "PHONE"
    TABLATE ="TABLATE"
    LAPTOP = "LAPTOP"
    GEAR = "GEAR"


class Status(models.TextChoices):
    GOOD = "GOOD"
    REPAIR = "REPAIR"
    MISSING = "MISSING"

class HandoverStatus(models.TextChoices):
    TAKE = "TAKE"
    RETURN = "RETURN"

    

class ConditionStatus(models.TextChoices):
    GOOD = "GOOD"
    BROKEN = "BROKEN"
