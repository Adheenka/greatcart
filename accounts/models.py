from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.
class Account(AbstractBaseUser):
    firest_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    username =models.CharField(max_length=50,unique=True)
    email =models.EmailField(max_length=100,unique=True)

    #requres
    date_joined =models.DateTimeField(auto_now_add=True)
    last_login =models.DateTimeField(auto_now_add=True)