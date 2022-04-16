from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from currency.models import Contact_us, Source
from currency.forms import SourceForm


def contact_us_list(request):
    contact_data = Contact_us.objects.all()
    return render(request, 'contact_us_list.html', context={'contact_data': contact_data})

from currency.models import Rate

def rate_list(request):
    rates = Rate.objects.all()
    return render(request, 'rate_list.html', context={'rates': rates})

def index(request):
    return render(request, 'index.html')



def source_list(request):
    sources = Source.objects.all()
    return render(request, 'source_list.html', context={'sources': sources})

def source_create(request):
    if request.POST:
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sources/')
    else:
        form = SourceForm()
    return render(request, 'source_create.html', context={'form': form})

def source_update(request, pk):
    try:
        instance = Source.objects.get(pk=pk)
    except Source.DoesNotExist:
        raise Http404(f'Object does not exist.')

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sources/')
    else:
        form = SourceForm(instance=instance)
    return render(request, 'source_update.html', context={'form': form})

def source_delete(request, pk):
    instance = get_object_or_404(Source, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return HttpResponseRedirect('/sources/')
    else:
        return render(request, 'source_delete.html', context={'source': instance})
