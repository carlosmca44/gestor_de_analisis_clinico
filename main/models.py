from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    category = models.CharField(max_length=20)


class Pacient(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    ci = models.CharField(max_length=11)
    age = models.IntegerField(default=0, blank=True, null=True)
    sex = models.CharField(max_length=1, default='')
    sicks = models.CharField(max_length=500, default='')
    diagnosis = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.name + ' ' + self.last_name


class AnalysisRequest(models.Model):
    pacient = models.ForeignKey(Pacient, on_delete=models.CASCADE)
    kind = models.CharField(max_length=50)
    denied = models.BooleanField(default=False)
