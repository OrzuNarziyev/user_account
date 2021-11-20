from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField('email adress', unique=True)
    image = models.ImageField('user_photo',blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager

    def __str__(self):
        return self.username
