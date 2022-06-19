from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('currency/', include('currency.urls')),
    path('auth/', include('django.contrib.auth.urls')),




]
