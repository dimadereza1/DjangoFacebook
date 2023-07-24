from django.db import models
from .base import Abstract
from .new_user import New_user

class PostM(Abstract):
    text = models.TextField()
    images = models.ImageField(upload_to='media/post/')