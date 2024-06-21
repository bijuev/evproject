from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()


class BlogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_author',
        blank=True,
        null=True
    )
    tags = TaggableManager()
    objects = BlogManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-created_at']
