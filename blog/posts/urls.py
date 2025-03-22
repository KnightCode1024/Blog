from django.urls import path

from posts import views

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
        "category/<int:cat_id>",
        views.category,
        name="category",
    ),
]
