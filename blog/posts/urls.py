from django.urls import path

from posts import views

app_name = "posts"

urlpatterns = [
    path(
        "about/",
        views.about,
        name="about",
    ),
    path(
        "post/<slug:post_slug>/",
        views.post,
        name="post",
    ),
    path(
        "category/<slug:cat_slug>/",
        views.category,
        name="category",
    ),
    path(
        "tag/<slug:tag_slug>/",
        views.tag,
        name="tag",
    ),
    path(
        "add/",
        views.add_post,
        name="add_post",
    ),
]
