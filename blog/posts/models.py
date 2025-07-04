from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from transliterate import slugify as transliterate_slugify
from django.contrib.auth import get_user_model


class PublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(is_published=Post.Status.PUBLISHED)
        )


class Post(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True,
    )
    summury = models.TextField(
        max_length=255, blank=False, verbose_name="Краткое содержание"
    )
    content = models.TextField(blank=False, verbose_name="Пост")
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания"
    )
    time_update = models.DateTimeField(
        auto_now=True, verbose_name="Время последнего обновления"
    )
    is_published = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
        default=Status.PUBLISHED,
        verbose_name="Статус",
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name="posts",
        null=True,
        default=None,
    )
    cat = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        related_name="posts",
        verbose_name="Категория",
    )
    tags = models.ManyToManyField(
        "TagPost", blank=True, related_name="tags", verbose_name="Тэги"
    )
    file = models.FileField(
        upload_to="files/%Y/%m/%d/",
        blank=True,
        null=True,
        verbose_name="Файл",
    )
    image = models.ImageField(
        upload_to="images/%Y/%m/%d/",
        blank=True,
        null=True,
        verbose_name="Изображение",
    )

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:post", kwargs={"post_slug": self.slug})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def save(self, *args, **kwargs):
        if not self.slug:
            try:
                self.slug = transliterate_slugify(self.title)
            except Exception:
                self.slug = slugify(self.title)

            if not self.slug:
                self.slug = "post"

            counter = 1
            original_slug = self.slug
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Категория",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("posts:category", kwargs={"cat_slug": self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse("posts:tag", kwargs={"tag_slug": self.slug})

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
