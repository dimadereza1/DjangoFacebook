from typing import Any, Dict
from django import http
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import PostM, User, ProfileM, LikeM, CommentM
from .forms import LoginForm, RegisterForm
from django.core.files import File
from pathlib import Path
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView, RedirectView
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
    
    def post(self, request,**kwargs):
        user = self.request.user
        if not user.is_authenticated:
            return redirect('/login/')
        return JsonResponse('ok', safe=False)
    
    def get(self, request, **kwargs):
        user = self.request.user
        if not user.is_authenticated:
            return redirect('/login')
        return JsonResponse('ok', safe=False)

class CreatePostView(TemplateView):
    template_name = 'create_post.html'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)

    def post(self, **kwargs):

        return JsonResponse('ok', safe=False)
    
class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    form_class = LoginForm
    


class RegisterView(CreateView):
    template_name = 'index.html'
    success_url = reverse_lazy('login')
    model = User

    def get_context_data(self, request,**kwargs):
        context = super().get_context_data(**kwargs)
        context['reg_form'] = RegisterForm()
        return context