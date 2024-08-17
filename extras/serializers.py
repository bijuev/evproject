from rest_framework import serializers
from .models import Trip, QuickTips


class QuickTipsSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')

    class Meta:
        model = QuickTips
        fields = ['id', 'title', 'content', 'image', 'video', 'posted_at', 'added_by']


class TripSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='user.username')
    origin = serializers.StringRelatedField()
    destination = serializers.StringRelatedField()

    class Meta:
        model = Trip
        fields = ['id', 'user', 'trip_name', 'origin', 'destination', 'notes', 'date_created', 'added_by']
        read_only_fields = ['user', 'date_created']
