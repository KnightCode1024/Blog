from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from posts import views
from config.settings import DEBUG

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
        name="admin",
    ),
    path(
        "",
        views.Index.as_view(),
        name="index",
    ),
    path(
        "posts/",
        include("posts.urls"),
    ),
    path(
        "users/",
        include("users.urls"),
        name="users",
    ),
    path(
        "social-auth/",
        include(
            "social_django.urls",
            namespace="social",
        ),
    ),
    path(
        'captcha/',
        include('captcha.urls'),
        name="captcha",
        ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.PageNotFoundView.as_view()

if DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
