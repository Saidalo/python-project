from __future__ import unicode_literals
from django.db import models


class Wiki(models.Model):
    name = models.TextField(max_length=200, blank=False, null=False)
    topic = models.TextField(max_length=1024, blank=False, null=False)
    createdAt = models.TimeField(auto_now_add=True, null=False)
