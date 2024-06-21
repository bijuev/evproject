from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


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