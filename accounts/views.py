from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import RegistrationForm


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('accounts:login')
