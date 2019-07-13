from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    is_subscribe = models.BooleanField(default=False)


class Article(models.Model):
    name = models.CharField(max_length=200, default='')
    image = models.ImageField(default='')
    text = models.TextField(default='')
    premium = models.BooleanField(default=False)