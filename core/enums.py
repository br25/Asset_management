from enum import Enum
from django.db import models 


class AssetsType(models.TextChoices):
    PHONE = "PHONE"
    TABLATE ="TABLATE"
    LAPTOP = "LAPTOP"
    GEAR = "GEAR"


class Status(models.TextChoices):
    NEW = "NEW"
    REFARBISHED = "REFARBISHED"
    OLD = "OLD"

class AssetDuration(models.TextChoices):
    TAKE = "TAKE"
    RETURN = "RETURN"

    

class Condition(models.TextChoices):
    GRANT = "GRANT"
    TEMPORARY = "TEMPORART"
    GIFT = "GIFT"
