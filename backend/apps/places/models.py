import uuid
from django.db import models
from apps.facilities.models import Facility
from apps.comments.models import Comment
from apps.reviews.models import Review
from apps.addresses.models import Address

# Create your models here.

class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    facilities = models.ManyToManyField(Facility, through='PlaceFacility')
    comments = models.ManyToManyField(Comment, through='PlaceComment')
    review = models.ManyToManyField(Review, through='PlaceReview')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PlaceFacility(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       unique_together = ("place", "facility")
    
class PlaceComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       unique_together = ("place", "comment")

class PlaceReview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       unique_together = ("place", "review")