from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, unique=True)
    biography = models.TextField(null=True, blank=True, default=None)
    linkedin_link = models.CharField(max_length=200, null=True, blank=True, default=None)
    githab_link = models.CharField(max_length=200, null=True, blank=True, default=None)
    twitter_link = models.CharField(max_length=200, null=True, blank=True, default=None)
    facebook_link = models.CharField(max_length=200, null=True, blank=True, default=None)
