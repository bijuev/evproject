from rest_framework import serializers
from .models import Trip, QuickTips


class QuickTipsSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')

    class Meta:
        model = QuickTips
        fields = ['id', 'title', 'content', 'image', 'video', 'posted_at', 'added_by']


class TripSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Trip
        fields = ['id', 'user', 'trip_name', 'start_location', 'end_location', 'notes', 'date_created']
        read_only_fields = ['user', 'date_created']
