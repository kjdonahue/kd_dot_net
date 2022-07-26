from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from enum import Enum

# rich text editor!
from ckeditor_uploader.fields import RichTextUploadingField

# Model manager for published posts
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = 'published', ('Published')
        DRAFT = 'draft', ('Draft')

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = RichTextUploadingField()
    image = models.ImageField(upload_to='great_divide/featured_image/%Y/%m/%d/')

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)

    objects = models.Manager() # default manager
    published = PublishedManager() # custom manager for published posts

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])