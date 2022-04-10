from django.shortcuts import render
from django.http import HttpResponse

from currency.models import Contact_us

def contact_us_list(request):
    contact_data = Contact_us.objects.all()
    return render(request, 'contact_us_list.html', context={'contact_data': contact_data})



from currency.models import Rate

def rate_list(request):
    rates = Rate.objects.all()
    return render(request, 'rate_list.html', context={'rates': rates})

def index(request):
    return render(request, 'index.html')


