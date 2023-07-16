from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Abstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class PostM(Abstract):
    text = models.TextField()
    images = models.ImageField(upload_to='media/post_img/')

class ProfileM(Abstract):
    avatar = models.ImageField(upload_to='media/profile/')
    city = models.TextField()
    telephone = models.IntegerField()
    date_of_born = models.DateField()
    # follovers = models.ManyToOneRel(User, related_name='follovers')
    friends = models.ManyToManyField(User, related_name='friends')
    modified_at = models.DateTimeField(auto_now=True)

class LikeM(Abstract):
    post = models.ForeignKey(PostM, on_delete=models.CASCADE)

class CommentM(Abstract):
    text = models.CharField(max_length=1000)
    post = models.ForeignKey(PostM, on_delete=models.CASCADE)