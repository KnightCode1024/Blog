from django.urls import path

from posts import views

app_name = "posts"

urlpatterns = [
    path(
        "post/<slug:post_slug>/",
        views.ShowPost.as_view(),
        name="post",
    ),
    path(
        "category/<slug:cat_slug>/",
        views.Category.as_view(),
        name="category",
    ),
    path(
        "tag/<slug:tag_slug>/",
        views.Tag.as_view(),
        name="tag",
    ),
    path(
        "add/",
        views.AddPost.as_view(),
        name="add_post",
    ),
    path(
        "post/<slug:post_slug>/edit/",
        views.UpdatePost.as_view(),
        name="edit_post",
    ),
    path(
        "post/<slug:post_slug>/delete/",
        views.DeletePost.as_view(),
        name="delete_post",
    ),
    path(
        "search/",
        views.Search.as_view(),
        name="search",
    ),
]
