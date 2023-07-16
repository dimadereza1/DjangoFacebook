from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('login/', views.LoginView.as_view()),
    # path('register/', views.RegisterView.as_view())
]
