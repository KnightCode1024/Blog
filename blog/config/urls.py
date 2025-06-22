from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.contrib.sitemaps.views import sitemap

from posts import views
from config.settings import DEBUG
from posts.sitemaps import PostSitemap, CategorySitemap

sitemaps = {
    "posts": PostSitemap,
    "cats": CategorySitemap,
}

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
        name="admin",
    ),
    path(
        "",
        cache_page(30)(views.Index.as_view()),
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
        "captcha/",
        include("captcha.urls"),
    ),
    path(
        "sitemap.xml",
        cache_page(86400)(sitemap),
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)


handler404 = views.PageNotFoundView.as_view()

if DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
