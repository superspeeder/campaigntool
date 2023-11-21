import uuid

from django.db import models


# Create your models here.
class Campaign(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Character(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    player = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

