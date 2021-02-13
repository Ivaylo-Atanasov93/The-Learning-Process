from django.db import models


# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=20, blank=False)
    surname = models.CharField(max_length=20, blank=False)
    phone = models.CharField(max_length=11, blank=False)
    email = models.CharField(max_length=30, blank=False)
    day = models.CharField(max_length=20, blank=False)
    time = models.CharField(max_length=20, blank=False)
    message = models.TextField(max_length=300, blank=False)
