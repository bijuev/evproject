from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()


class LocationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Location(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=20, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=16, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    phone_number = PhoneNumberField(verbose_name='Phone Number',
                                    max_length=16,
                                    blank=True,
                                    null=True)
    added_by = models.ForeignKey(User,
                                 on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 related_name='locations_added')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
        ordering = ['name']


class Review(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    rating = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location.name

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ['-created_at']


class LocationSearch(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=16, blank=True, null=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=16, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    phone_number = PhoneNumberField(verbose_name='Phone Number',
                                    max_length=16,
                                    blank=True,
                                    null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Location Search'
        ordering = ['name']