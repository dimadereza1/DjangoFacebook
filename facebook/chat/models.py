from facebook_app.models import New_user
from django.db import models


class Chat(models.Model):
    members = models.ManyToManyField(New_user)


class Messages(models.Model):
    user = models.ForeignKey(New_user, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    created_At = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=10000)

