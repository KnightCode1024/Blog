from django.contrib import admin
from django.urls import path, include

from posts import views
from config.settings import DEBUG

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", views.index, name="index"),
    path("posts/", include("posts.urls")),
    path("users/", include("users.urls")),
]

handler404 = views.page_not_found

if DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
