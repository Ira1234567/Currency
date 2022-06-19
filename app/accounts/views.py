from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.utils.translation import gettext_lazy

from accounts.models import User

class MyProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'my_profile.html'
    success_url = reverse_lazy('home')
    fields = (
        'first_name',
        'last_name'
    )
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.request.user.id)
        return queryset





