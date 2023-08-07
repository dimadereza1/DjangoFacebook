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
import json

# Create your views here.

class Logout(LogoutView):
    pass



class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = PostM.objects.all().order_by('-created_at')
        context['user_img'] = New_user.objects.get(id=self.request.user.id).avatar.url


        context['following'] = Friends_user.objects.get(user_fou=self.request.user).following.all()

        friends = []


        for f in Friends_user.objects.get(user_fou=self.request.user).following.all():
            for foll in Friends_user.objects.get(user_fou=f).following.all():
                if foll == self.request.user:
                    friends.append(f)
        print(friends)


        post_likes_counts = []
        for post in posts:
            likes_count = LikeM.objects.filter(post=post).count()
            likes_count1 = LikeM.objects.filter(post=post)
            user = post.user


            for l in likes_count1:

                if l.user == self.request.user:
                    print('a2')
                    is_liked = 1
                    post_likes_counts.append([post, likes_count, 1, user])
                    break
            else:
                post_likes_counts.append([post, likes_count, 0, user])
            

        context['post_likes_counts'] = post_likes_counts

        context['friends'] = Friends_user.objects.filter(user_fou=self.request.user)

        return context
    
    def post(self, request):
        data = request.POST
        if 'vw_post' in data.keys():
            post = PostM.objects.get(id=data['vw_post'])
            comments = CommentM.objects.filter(post=post)
            return JsonResponse({'post_img':post.images,'post_text':post.text, 'user': request.user,  }, safe=False)
        
        elif 'id_o_post_i_d' in data.keys():
            post = PostM.objects.get(id=data['id_o_post_i_d'])
            comments = CommentM.objects.filter(post=post)
            response = render_to_string('post_for_dia.html', {'postt': post ,'img_post': post.images, 'text_post': post.text, 'post_user':post.user, 'img_user':post.user.avatar.url, 'user':self.request.user, 'comments': comments})
            return JsonResponse(response, safe=False)
        elif 'data_id' in data.keys():
            post = PostM.objects.get(id=data['data_id'])

            like = LikeM(post=post, user=self.request.user)
            like.save()

            response = {'id_o_ppost': post.id}
            return JsonResponse(response, safe=False)
        
        if 'delete_data_id' in data.keys():
            post= PostM.objects.get(id=data['delete_data_id'])

            like = LikeM.objects.get(post=post, user=self.request.user)
            like.delete()
            like.save()
            
            response = {'id_o_ppost': post.id}
            return JsonResponse(response, safe=False)
        return JsonResponse('ok', safe=False)

    

class CreatePostView(TemplateView):
    template_name = 'create_post.html'
    

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['user_img'] = New_user.objects.get(id=self.request.user.id).avatar.url
        return context

    def post(self, request, **kwargs):
        data = request.POST
        if 'data_post_text' in data.keys():
            path = Path('media/post/upload.png')
            with path.open(mode='rb') as file:
                image = File(file, name=file.name)
                post = PostM(user=self.request.user, text=data['data_post_text'], images=image)
                post.save()
                reverse_lazy('home')
                
                return JsonResponse('ok', safe=False)
        else:
            files = request.FILES['file']
            with open('media/post/upload.png', 'wb') as img:
                img.write(files.read())

        return JsonResponse('ok', safe=False)

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = New_user.objects.get(id=self.request.user.id)
        context['user_img'] = user.avatar.url
        context['user_bg'] = user.background.url
        context['p_o_u'] = PostM.objects.filter(user=user)
        context['user'] = self.request.user
        try:
            context['len_friends'] = len(Friends_user.objects.get(user_fou=user).friends.all())
        except Friends_user.DoesNotExist:
            context['len_friends'] = 0
        return context
    
    def post(self, request, **kwargs):
        data = request.POST
        print(data.keys())
        if 'delete_post' in data.keys():
            post = PostM.objects.get(id=data['delete_post'])
            post.delete()

        elif 'form_dataa' in data.keys():
            post = PostM.objects.get(id=data['data_forma_id'])
            user = request.user
            comment = CommentM(text=data['form_dataa'], post=post, user=user)
            comment.save()
            response = render_to_string('new_comment.html', {'text_comment': data['form_dataa'], 'user': user})
            return JsonResponse(response, safe=False)

        elif 'id_o_post_i_d' in data.keys():
            post = PostM.objects.get(id=data['id_o_post_i_d'])
            comments = CommentM.objects.filter(post=post)
            response = render_to_string('post_for_dia.html', {'postt': post ,'img_post': post.images, 'text_post': post.text, 'post_user':post.user, 'img_user':post.user.avatar.url, 'user':self.request.user, 'comments': comments})
            return JsonResponse(response, safe=False)
        
        elif 'backgg' in data.keys():
            files = request.FILES['file']
            with open('facebook_app/static/media_photo/profile/background/upload.png', 'wb') as img:
                img.write(files.read())

            path = Path('facebook_app/static/media_photo/profile/background/upload.png')
            with path.open(mode='rb') as file:
                image = File(file, name=file.name)
                user = New_user.objects.get(id=request.user.id)
                user.background = image
                user.save()
            return JsonResponse({'new_background': str(user.background.url)}, safe=False)
        
        elif 'data_edit_username' in data.keys():
            user = New_user.objects.get(id=request.user.id)
            user.username = data['data_edit_username']
            user.save()
            return JsonResponse({'new_username': str(user.username)}, safe=False)
        
        elif 'vw_post' in data.keys():
            post = PostM.objects.get(id=data['vw_post'])
            comments = CommentM.objects.filter(post=post)
            return JsonResponse({'post_w_img':str(post.images),'post_text':post.text, 'user_username': request.user.username, 'user_id': request.user.id  }, safe=False)
        
        elif 'ava' in request.POST:
            files = request.FILES['file']
            with open('facebook_app/static/media_photo/profile/avatar/upload.png', 'wb') as img:
                img.write(files.read())

            path = Path('facebook_app/static/media_photo/profile/avatar/upload.png')
            with path.open(mode='rb') as file:
                image = File(file, name=file.name)
                user = New_user.objects.get(id=request.user.id)
                user.avatar = image
                user.save()

            return JsonResponse({'new_avatar': str(user.avatar.url)})
        
        elif 'cr_user' in data.keys():
            curr_user = New_user.objects.get(username=data['cr_user'])
            return JsonResponse({'user_username': curr_user.username})
        return JsonResponse('ok', safe=False)

    

    
class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    form_class = LoginForm

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form_two'] = RegisterForm
        return context
    
class VProfileView(TemplateView):
    template_name = 'vprofile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = New_user.objects.get(id=kwargs['id'])
        context['user_data'] = user
        context['user_img'] = New_user.objects.get(id=self.request.user.id).avatar.url
        context['p_o_u'] = PostM.objects.filter(user=user)
        try:
            context['len_friends'] = len(Friends_user.objects.get(user_fou=user).friends.all())
        except Friends_user.DoesNotExist:
            context['len_friends'] = 0


        try:
            for i in Friends_user.objects.get(user_fou=user).friends.all():
                if i == self.request.user:
                    print('work')
                    context['is_subscribed'] = 1
                else:
                    context['is_subscribed'] = 0
            else:
                if len(Friends_user.objects.get(user_fou=user).friends.all()) == 0:
                    context['is_subscribed'] = 0
        except Friends_user.DoesNotExist:
            print('doew not work')
            context['is_subscribed'] = 0

        return context
    
    def post(self, request, **kwargs):
        data = request.POST

        if 'friend' in data.keys():
            user = request.user
            a = New_user.objects.get(id=kwargs['id'])
            m = New_user.objects.get(id=user.id)
            b, t =Friends_user.objects.get_or_create(user_fou=a)

            c, g = Friends_user.objects.get_or_create(user_fou=m)

            c.following.add(a)
            c.save()
            
            
            b.friends.add(user)
            b.save()
            return JsonResponse('ok', safe=False)
        
        if 'ofriend' in data.keys():
            user = request.user
            a = New_user.objects.get(id=kwargs['id'])
            b =Friends_user.objects.get(user_fou=a)
            b.friends.remove(user)
            b.save()
    
            
        return JsonResponse('ok', safe=False)

    


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