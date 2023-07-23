from django.db import models
from .base import Abstract

class PostM(Abstract):
    text = models.TextField()
    images = models.ImageField(upload_to='media/post/')