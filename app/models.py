from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Todo(models.Model):
    todo_job = models.TextField()
    author = models.ForeignKey(User)
    deadline_date = models.DateTimeField(default=timezone.now)
