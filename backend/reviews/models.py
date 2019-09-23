import uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    rate = models.DecimalField(max_digits=3, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
