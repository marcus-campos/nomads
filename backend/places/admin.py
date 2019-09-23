from django.contrib import admin
from .models import Place, PlaceFacility, PlaceComment, PlaceReview

class PlaceFacilityInline(admin.TabularInline):
    model = PlaceFacility
    extra = 1

class PlaceCommentInline(admin.TabularInline):
    model = PlaceComment
    extra = 1

class PlaceReviewInline(admin.TabularInline):
    model = PlaceReview
    extra = 1

class PlaceAdmin(admin.ModelAdmin):
    inlines = (PlaceFacilityInline, PlaceCommentInline, PlaceReviewInline,)

# Register your models here.

admin.site.register(Place, PlaceAdmin)