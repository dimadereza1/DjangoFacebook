from django.db import models
from .new_user import New_user

class Chats(models.Model):
    members = models.ManyToManyField(New_user)