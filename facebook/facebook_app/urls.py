from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', login_required(views.LoginView.as_view())),
    path('reg/', views.RegisterView.as_view()),
]
