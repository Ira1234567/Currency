
from django.db import models


class Contact_us(models.Model):
    email_from = models.EmailField(max_length=40)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)


class Rate(models.Model):
    type = models.CharField(max_length=5)
    source = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    buy = models.DecimalField(max_digits=100, decimal_places=10)
    sale = models.DecimalField(max_digits=100, decimal_places=10)

class Source(models.Model):
    name = models.CharField(max_length=64)
    url = models.CharField(max_length=255)
    founded = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    contacts = models.EmailField(max_length=40)







