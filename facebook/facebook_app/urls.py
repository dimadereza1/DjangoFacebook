from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.HomeView.as_view()), name='home'),
    path('login/', views.LoginView.as_view()),
    path('reg/', views.RegisterView.as_view()),
    path('logout/', views.Logout.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('view_profile/<int:id>/', views.VProfileView.as_view()),
    path('create_post/', views.CreatePostView.as_view())
]
