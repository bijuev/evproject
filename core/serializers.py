from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Location, LocationSearch, UserProfile
User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'bio', 'profile_picture', 'phone_number']
        read_only_fields = ['user']


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['id', 'name', 'city', 'phone_number', 'latitude', 'longitude']


class LocationSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationSearch
        fields = ['id', 'name', 'city', 'phone_number', 'latitude', 'longitude']
