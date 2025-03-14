from django.urls import path

from blog import views

urlpatterns = [
    path(
        "about/",
        views.about,
        name="about",
    ),
    path(
        "post/<int:post_id>/",
        views.post,
        name="post",
    ),
]
