from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from currency.models import Contact_us, Source, Rate
from currency.forms import SourceForm

class RateList(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'

class SourceList(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'

class ContactUsList(ListView):
    queryset = Contact_us.objects.all()
    template_name = 'contact_us_list.html'

class SourceCreate(CreateView):
    model = Source
    template_name = 'source_create.html'
    form_class = SourceForm
    success_url = '/currency/source_list/'

class SourceUpdate(UpdateView):
    model = Source
    template_name = 'source_update.html'
    form_class = SourceForm
    success_url = '/currency/source_list/'

class SourceDetail(DetailView):
    model = Source
    template_name = 'source_detail.html'

class SourceDelete(DeleteView):
    model = Source
    template_name = 'source_delete.html'
    success_url = '/currency/source_list/'

