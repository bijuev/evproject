from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Trip, QuickTips


@admin.register(QuickTips)
class QuickTipsAdmin(ModelAdmin):
    list_display = ('title', 'posted_at', 'added_by')
    search_fields = ('title',)


@admin.register(Trip)
class TripAdmin(ModelAdmin):
    list_display = ('trip_name', 'user', 'start_location', 'end_location', 'date_created')
    list_filter = ('user', 'start_location', 'end_location', 'date_created')