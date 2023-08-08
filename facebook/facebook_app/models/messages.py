from django.db import models
from .new_user import New_user
from .chats import Chats

class Messages(models.Model):
    user = models.ForeignKey(New_user, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chats, on_delete=models.CASCADE)
    created_At = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=10000)