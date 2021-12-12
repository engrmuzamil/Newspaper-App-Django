from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CreateForm


class SignupView(CreateView):
    form_class = CreateForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
