from __future__ import unicode_literals

from django.db import models
from datetime import datetime, timedelta


# Create your models here.
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=75)
    password = models.CharField(max_length=10)


class Todo(models.Model):
    todo_job = models.TextField()
    user = models.ForeignKey('User')
    deadline_date = models.DateTimeField(default=timezone.now)
