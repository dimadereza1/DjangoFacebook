from django.db import models
from .new_user import New_user

class Friends_user(models.Model):
    user_fou = models.ForeignKey(New_user, on_delete=models.CASCADE)
    friends = models.ManyToManyField(New_user, related_name='friends', blank=True)
    following = models.ManyToManyField(New_user, related_name='following')