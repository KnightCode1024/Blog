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
        choices=Status,
        default=Status.PUBLISHED,
    )
    author = models.CharField(
        max_length=50,
        blank=True,
    )
    co_author = models.OneToOneField(
        "Author",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="author",
    )
    cat = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        related_name="posts",
    )
    tags = models.ManyToManyField(
        "TagPost",
        blank=True,
        related_name="tags",
    )

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ["time_create"]
        indexes = [models.Index(fields=["-time_create"])]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post", kwargs={"post_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
    )
    slug = slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("posts:category", kwargs={"cat_slug": self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse("posts:tag", kwargs={"tag_slug": self.slug})


class Author(models.Model):
    name = models.CharField(
        max_length=100,
    )
    count_publish = models.IntegerField(
        null=True,
    )
    citation_count = models.IntegerField(
        blank=True,
        default=0,
    )

    def __str__(self):
        return self.name
