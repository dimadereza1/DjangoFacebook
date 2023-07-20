from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class Abstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class PostM(Abstract):
    text = models.TextField()
    images = models.ImageField(upload_to='media/post_img/')

class Friends_user(models.Model):
    user_fou = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)

class Many_about_user(AbstractUser):
    avatar = models.ImageField(default='static/default/avatarka.jpg', upload_to='media/profile/avatar/')
    background = models.ImageField(default='static/default/background.jpg', upload_to='media/profile/background/') 


class ProfileM(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.IntegerField(blank=True)
    date_of_born = models.DateField(blank=True)
    modified_at = models.DateTimeField(auto_now=True)

class LikeM(Abstract):
    post = models.ForeignKey(PostM, on_delete=models.CASCADE)

class CommentM(Abstract):
    text = models.CharField(max_length=1000)
    post = models.ForeignKey(PostM, on_delete=models.CASCADE)

