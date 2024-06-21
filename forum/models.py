from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
User = get_user_model()


class Forum(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='forum_author',
        blank=True,
        null=True
    )
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Forum'
        verbose_name_plural = 'Forums'
        ordering = ['-created_at']


class Comment(models.Model):
    forum = models.ForeignKey(
        Forum,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True
    )
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comment_author',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at']


class Reply(models.Model):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='replies',
        blank=True,
        null=True
    )
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reply_author',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'
        ordering = ['-created_at']


class Like(models.Model):
    forum = models.ForeignKey(
        Forum,
        on_delete=models.CASCADE,
        related_name='likes',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='like_author',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
        ordering = ['-created_at']


class Dislike(models.Model):
    forum = models.ForeignKey(
        Forum,
        on_delete=models.CASCADE,
        related_name='dislikes',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='dislike_author',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = 'Dislike'
        verbose_name_plural = 'Dislikes'
        ordering = ['-created_at']
