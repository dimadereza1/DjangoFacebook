from typing import Any, Dict
from django import http
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import PostM, LikeM, CommentM,  New_user, Friends_user
from .forms import LoginForm, RegisterForm
from django.core.files import File
from pathlib import Path
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView, RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse, JsonResponse

# Create your views here.

class Logout(LoginView):
    pass

class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = PostM.objects.all().order_by('-created_at')
        context['user_img'] = New_user.objects.get(id=self.request.user.id).avatar
        context['all_posts'] = posts
        likes_count = {}
        for post in posts:
            likes_count[post.id] = len(LikeM.objects.filter(post=post))

        print(likes_count)
        context['likes'] = likes_count
        return context
    
    def post(self, request):


        return JsonResponse('ok', safe=False)
    

class CreatePostView(TemplateView):
    template_name = 'create_post.html'
    

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['user_img'] = New_user.objects.get(id=self.request.user.id).avatar
        return context

    def post(self, request, **kwargs):
        data = request.POST
        if 'data_post_text' in data.keys():
            path = Path('media/post/upload.png')
            with path.open(mode='rb') as file:
                image = File(file, name=file.name)
                post = PostM(user=self.request.user, text=data['data_post_text'], images=image)
                post.save()
                return reverse_lazy('/')
        else:
            files = request.FILES['file']
            with open('media/post/upload.png', 'wb') as img:
                img.write(files.read())

        return JsonResponse('ok', safe=False)

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_img'] = New_user.objects.get(id=self.request.user.id).avatar
        context['user_bg'] = New_user.objects.get(id=self.request.user.id).background
        context['user'] = self.request.user
        try:    
            context['len_friends'] = len(Friends_user.objects.get(user_fou=self.request.user).friends)
        except Friends_user.DoesNotExist:
            context['len_friends'] = 0
        return context
    

    
class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    form_class = LoginForm

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form_two'] = RegisterForm
        return context
    


    


class RegisterView(CreateView):
    template_name = 'login.html'
    success_url = reverse_lazy('login')

    def post(self, request, **kwargs):
        data = request.POST
        for i in New_user.objects.all():
            if i.username == data['data_username']:
                return JsonResponse('такий користувач уже існує', safe=False)
            else:
                new_user = New_user.objects.create_user(username=data['data_username'], email=data['data_email'], password=data['data_password'])
                new_user.save()
        return JsonResponse('', safe=False)