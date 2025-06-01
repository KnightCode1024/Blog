from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from posts import views
from config.settings import DEBUG

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", views.index, name="index"),
    path("posts/", include("posts.urls")),
    path("users/", include("users.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.page_not_found

if DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
