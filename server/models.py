from django.db import models


class Occurrence(models.Model):
    """
    This class represents a Occurrence.
    """
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    plan = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    description = models.TextField()
    traffic_ticket = models.TextField()
    drivers_licence = models.TextField()
    dut_copy = models.TextField()
    value = models.FloatField(default=0.0)
