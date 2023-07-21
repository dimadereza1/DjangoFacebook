from django.db import models
from .post import PostM
from .base import Abstract

class LikeM(Abstract):
    post = models.ForeignKey(PostM, on_delete=models.CASCADE)