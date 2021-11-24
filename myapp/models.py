from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()

    # the required fields to enable a generic relation
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.author


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title


class Profile(models.Model):
    about = models.TextField()
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    comments = GenericRelation(Comment)

    def __str__(self):
        return f'profile of {self.user.username}'
