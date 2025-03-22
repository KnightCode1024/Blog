from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(is_published=Post.Status.PUBLISHED)
        )


class Post(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"

    title = models.CharField(
        max_length=255,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
    )
    summury = models.TextField(
        max_length=255,
        blank=False,
    )
    content = models.TextField(
        blank=False,
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
    )
    time_update = models.DateTimeField(
        auto_now=True,
    )
    is_published = models.BooleanField(
        choices=Status.choices,
        default=Status.PUBLISHED,
    )
    author = models.CharField(
        max_length=50,
        blank=True,
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["-time_create"]
        indexes = [models.Index(fields=["-time_create"])]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
