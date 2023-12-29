from .form import CustomUserCreationForm
from django.shortcuts import render
from django.views import generic
# Create your views here.
from django.urls import reverse_lazy


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

