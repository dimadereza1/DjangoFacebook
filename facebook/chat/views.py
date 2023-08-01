from typing import Any, Dict
from django import http
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import Chat, Messages
from facebook_app.models import New_user
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chats'] = Chat.objects.all()
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        data = request.POST
        searched = New_user.objects.filter(username__contains=data['input'])
        response = render_to_string('searched.html', {'users':searched})
        return JsonResponse(response, safe=False)
    
class SeachView(TemplateView):
    template_name ='search.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        chats = New_user.objects.filter(username__contains=data['search_input'])
        response = render_to_string('searched.html', {'chat':chats})
        return JsonResponse(response, safe=False)
