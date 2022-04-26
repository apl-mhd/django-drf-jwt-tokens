import email
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    #username = models.CharField(max_length = 64, blank = True, null = True, unique = True)
    username = None



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  []
    #REQUIRED_FIELDS =  ['username']
