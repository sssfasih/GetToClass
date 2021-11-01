from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)

class UserImage(models.Model):
    user = models.ForeignKey(User, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_pics')