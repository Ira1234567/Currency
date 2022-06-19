
from django.db import models



class Source(models.Model):
    name = models.CharField(max_length=64, unique=True)
    url = models.CharField(max_length=255)
    founded = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    contacts = models.EmailField(max_length=40)


class Rate(models.Model):
    type = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    buy = models.DecimalField(max_digits=100, decimal_places=10)
    sale = models.DecimalField(max_digits=100, decimal_places=10)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='rates')

class Contact_us(models.Model):
    name = models.CharField(max_length=130)
    reply_to = models.EmailField()
    subject = models.CharField(max_length=130)
    body = models.CharField(max_length=1500)
    raw_content = models.TextField()








