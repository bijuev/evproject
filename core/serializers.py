from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Location, LocationSearch
User = get_user_model()


# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ['id', 'image', 'username', 'email', 'first_name', 'last_name']


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['id', 'name', 'city', 'phone_number', 'latitude', 'longitude']


class LocationSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = LocationSearch
        fields = ['id', 'name', 'city', 'phone_number', 'latitude', 'longitude']
