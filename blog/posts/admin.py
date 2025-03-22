from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "summury",
        "content",
        "is_published",
    ]
    list_editable = [
        "summury",
        "content",
        "is_published",
    ]
    list_display_links = ["title"]

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
