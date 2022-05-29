from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from currency.models import Source, Rate, Contact_us
from currency.forms import SourceForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings

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

class ContactUsCreateView(CreateView):
    model = Contact_us
    template_name = 'contact_us_create.html'
    success_url = reverse_lazy('home')
    fields = (
        'name',
        'reply_to',
        'subject',
        'body'
    )
    def _send_email(self):
        subject = 'Contact_Us user'
        body = f'''
        Request From: {self.object.name}
        Email to reply: {self.object.reply_to}
        Subject: {self.object.subject}
        Body: {self.object.body}
        '''
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently = False,
        )
    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_email()
        return redirect
