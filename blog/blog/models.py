from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    summury = models.TextField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    author = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-time_create"]
        indexes = [models.Index(fields=["-time_create"])]

    def get_absollute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
