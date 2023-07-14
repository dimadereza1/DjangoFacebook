from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Abstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class PostM(Abstract):
    text = models.TextField()
    images = models.ImageField(upload_to='media/post_img/')
    city = models.TextField()

class ProfileM(Abstract):
    avatar = models.ImageField(upload_to='media/profile/')

