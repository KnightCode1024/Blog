from django.contrib import admin
from posts.models import Post, Category, TagPost


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "summury",
        "is_published",
        "cat",
        "display_tags",
    ]
    list_editable = [
        "summury",
        "is_published",
        "cat",
    ]
    list_display_links = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ["tags"]

    def display_tags(self, obj):
        return ", ".join([tag.tag for tag in obj.tags.all()])

    display_tags.short_description = "Tags"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
    ]
    list_display_links = ["name"]
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    list_display = [
        "tag",
        "slug",
    ]
    list_display_links = ["tag"]
    prepopulated_fields = {"slug": ("tag",)}

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
