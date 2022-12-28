from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    category = models.CharField(max_length=20)


class Paciente(models.Model):
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=50)
    ci = models.CharField(max_length=11)
