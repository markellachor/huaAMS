from django.conf import settings
from django.db import models
from djmoney.models.fields import MoneyField


class ResearchProgram(models.Model):
    title = models.CharField(max_length=255, unique=True)
    researcher = models.CharField(max_length=100)
    description = models.TextField()


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    school = models.CharField(max_length=255)


class Building(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)


class Asset(models.Model):
    registration_number = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=255)
    pieces = models.IntegerField()
    serial_number = models.TextField()
    invoice_number = models.TextField()
    invoice_value = MoneyField(max_digits=14, decimal_places=2, default_currency="EUR")
    acquisition_value = MoneyField(
        max_digits=14, decimal_places=2, default_currency="EUR"
    )
    tax_value = MoneyField(max_digits=14, decimal_places=2, default_currency="EUR")
    supplier = models.TextField(max_length=255)
    building = models.ForeignKey(Building, on_delete=models.PROTECT)
    office = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    asset_manager = models.TextField()
    changes_additions = models.TextField()
    research_program = models.ForeignKey(ResearchProgram, on_delete=models.PROTECT)
    invoice_url = models.URLField()
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    qr_path = models.TextField(null=True, blank=True)

