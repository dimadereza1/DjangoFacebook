from django.db import models
from .post import PostM
from .base import Abstract

class CommentM(Abstract):
    text = models.CharField(max_length=1000)
    post = models.ForeignKey(PostM, on_delete=models.CASCADE)