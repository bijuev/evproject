from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Blog
User = get_user_model()


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = [
            'title',
            'body',
            'image',
            'created_at',
            'author',
            'tags',
        ]
