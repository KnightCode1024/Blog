from django.contrib import admin
from django.urls import path, include

from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("blog/", include("blog.urls")),
]

handler404 = views.page_not_found
