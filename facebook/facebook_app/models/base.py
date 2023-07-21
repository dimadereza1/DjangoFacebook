from django.db import models
from .new_user import New_user

class Abstract(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(New_user, on_delete=models.CASCADE)

    class Meta:
        abstract = True