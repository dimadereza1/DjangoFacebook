from typing import Any, Dict
from django import http
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import Chat, Messages
from pathlib import Path
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView, RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse, JsonResponse
# Create your views here.


class ChatsView(TemplateView):
    template_name = 'chats_c.html'

    
