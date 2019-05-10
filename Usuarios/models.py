from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Usuario_admin(models.Model):
  name=models.CharField(max_length=200)
  app_paterno= models.CharField(max_length=50, blank=True, null=True)
  app_materno = models.CharField(max_length=50, blank=True, null=True)
  isAdmin = models.BooleanField(default=True)
  password=models.CharField(max_length=50)

