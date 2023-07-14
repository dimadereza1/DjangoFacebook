from typing import Any, Dict
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import PostM, User
from django.core.files import File
from pathlib import Path
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse


# Create your views here.

class Logout(LoginView):
    pass

class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def post(self, **kwargs):
        return JsonResponse('ok', safe=False)