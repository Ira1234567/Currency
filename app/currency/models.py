
from django.db import models


class Contact_us(models.Model):
    email_from = models.EmailField(max_length=40)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)



