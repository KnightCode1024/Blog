from django.contrib import admin, messages
from posts.models import Post, Category, TagPost
from django.db.models.functions import Length
from unfold.admin import ModelAdmin


class CoAuthorFilter(admin.SimpleListFilter):
    title = "Наличие соавтора"
    parameter_name = "соавтора"

    def lookups(self, request, model_admin):
        return [
            ("co-author", "Есть соавтор"),
            ("single", "Нет соавтора"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "co-author":
            return queryset.filter(co_author__isnull=False)
        else:
            return queryset.filter(co_author__isnull=True)


class ContentFilter(admin.SimpleListFilter):
    title = "Сортировка по статьям"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return [
            ("short", "Короткие статьи"),
            ("middle", "Средние статьи"),
            ("long", "Большие статьи"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "short":
            return queryset.annotate(length=Length("content")).filter(
                length__lt=1000
            )
        elif self.value() == "middle":
            return queryset.annotate(length=Length("content")).filter(
                length__gte=1000, length__lt=5000
            )
        elif self.value() == "long":
            return queryset.annotate(length=Length("content")).filter(
                length__gte=5000
            )
        else:
            return queryset


@admin.register(Post)
class PostAdmin(ModelAdmin):
    exclude = [
        "is_published",
    ]
    # readonly_fields = ["slug"]
    list_display = [
        "title",
        "time_create",
        "is_published",
        "cat",
        "brief_info",
    ]
    list_display_links = [
        "title",
    ]
    ordering = [
        "-time_create",
        "title",
    ]
    list_editable = [
        "is_published",
        "cat",
    ]
    list_per_page = 10
    actions = [
        "set_publish_to_all_posts",
        "set_draft_to_all_posts",
    ]
    search_fields = [
        "title",
        "cat__name",
    ]
    list_filter = [
        CoAuthorFilter,
        ContentFilter,
        "cat__name",
        "is_published",
    ]
    prepopulated_fields = {"slug": ["title"]}
    filter_horizontal = ["tags"]
    # filter_vertical = ["tags"]

    @admin.display(description="Краткое описание")
    def brief_info(self, post: Post):
        return f"Описание {len(post.content)} символов."

    @admin.action(description="Опубликовать выбранные записи")
    def set_publish_to_all_posts(self, request, queryset):
        count = queryset.update(is_published=Post.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записи(ей).")

    @admin.action(description="Сделать черновиком выбранные записи")
    def set_draft_to_all_posts(self, request, queryset):
        count = queryset.update(is_published=Post.Status.DRAFT)
        self.message_user(
            request,
            f"Изменено {count} записи(ей).",
            messages.WARNING,
        )

    # class Meta:
    #     verbose_name = "Пост"
    #     verbose_name_plural = "Посты"


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    list_display_links = [
        "id",
        "name",
    ]
    prepopulated_fields = {
        "slug": ("name",),
    }

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


@admin.register(TagPost)
class TagPostAdmin(ModelAdmin):
    list_display = [
        "tag",
        "slug",
    ]
    list_display_links = ["tag"]
    prepopulated_fields = {"slug": ("tag",)}

    # class Meta:
    #     verbose_name = "Тэг"
    #     verbose_name_plural = "Тэги"
