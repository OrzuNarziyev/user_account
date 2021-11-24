import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager

# from io import BytesIO
# from django.core.files import File
# from PIL import Image, ImageDraw, ImageFont


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField('email adress', unique=True)
    image = models.ImageField('user_photo', blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager

    # def save(self, *args, **kwargs):
    #     try:
    #         if len(self.image) > 0:
    #             img = Image.new('RGB', (400, 400), color=(73, 109, 137))
    #             d = ImageDraw.Draw(img)
    #             fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", size=150)
    #             d.text((80, 120), 'H W', fill=(255, 255, 255), font=fnt)
    #             fname = f"{self.username}" + ".png"
    #             buffer = BytesIO()
    #             img.save(buffer, 'PNG')
    #             self.image.save(fname, File(buffer), save=False)
    #             img.close()
    #     except:
    #         pass

    def __str__(self):
        return self.username
