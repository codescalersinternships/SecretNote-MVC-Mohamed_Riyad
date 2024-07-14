import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    pass


class Note(models.Model):
    title = models.TextField(max_length=10, default="ryad")
    content = models.TextField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    view_count = models.IntegerField(default=0)
    max_count = models.IntegerField(default=3)
    creation_date = models.DateField(default=timezone.now)



