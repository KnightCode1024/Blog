from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    summury = models.TextField(max_length=30, blank=False)
    content = models.TextField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-time_create"]
        indexes = [models.Index(fields=["-time_create"])]
