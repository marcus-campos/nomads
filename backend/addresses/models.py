import uuid
from django.db import models


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    latitude = models.CharField(max_length=20, null=True, blank=True)
    longitude = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.line1