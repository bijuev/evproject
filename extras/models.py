from django.contrib.auth.models import User
from django.db import models
from core.models import Location


class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    origin = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='start_trips')
    destination = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='end_trips')
    date_created = models.DateTimeField(auto_now_add=True)
    trip_name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trip"

    def __str__(self):
        return f"{self.trip_name} by {self.user.username}"


class QuickTips(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='quick_tips/images/', blank=True, null=True)
    video = models.FileField(upload_to='quick_tips/videos/', blank=True, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User,
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='quick_tip_added')

    class Meta:
        verbose_name = "Quick Tips"
        verbose_name_plural = "Quick Tips"

    def __str__(self):
        return self.title


class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['-created_at']


class Tips(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tip'
        verbose_name_plural = 'Tips'
        ordering = ['-created_at']
