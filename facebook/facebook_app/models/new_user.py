from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class New_user(AbstractUser):
    avatar = models.ImageField(default='/static/default/avatarka.jpg', upload_to='./static/media_photo/profile/avatar/')
    background = models.ImageField(default='/static/default/background.jpg', upload_to='.static/media_photo/profile/background/') 
    telephone = models.IntegerField(null=True, blank=True)
    date_of_born = models.DateField(null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)