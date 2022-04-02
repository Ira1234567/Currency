from django.shortcuts import render
from django.http import HttpResponse

from currency.models import Contact_us

def contact_us_list(request):
    contact_data = []
    for i in Contact_us.objects.all():
        contact_data.append([i.id, i.email_from, i.subject, i.message])
    return HttpResponse(str(contact_data))

#def hello_world(request):
    #return HttpResponse('Hello world')

# Create your views here.
