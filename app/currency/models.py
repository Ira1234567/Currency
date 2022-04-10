
from django.db import models


class Contact_us(models.Model):
    email_from = models.EmailField(max_length=40)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)


class Rate(models.Model):
    type = models.CharField(max_length=5)
    source = models.CharField(max_length=50)
    created = models.DateTimeField()
    buy = models.DecimalField(max_digits=100, decimal_places=10)
    sale = models.DecimalField(max_digits=100, decimal_places=10)




