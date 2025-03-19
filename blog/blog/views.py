from django.shortcuts import render, get_object_or_404
from django import http

from blog.models import Post


cats_db = [
    {"id": 1, "name": "Спорт"},
    {"id": 2, "name": "Python"},
    {"id": 3, "name": "JavaScript"},
    {"id": 4, "name": "Жизнь"},
    {"id": 5, "name": "Наука"},
    {"id": 6, "name": "Школа"},
]


def index(request):
    return render(request, "index.html")


# TO DO: post and about views funcion dont DRY
def about(request):
    post = get_object_or_404(Post, slug="founder")
    return render(request, "post.html", {"post": post})


def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render(request, "post.html", {"post": post})


def page_not_found(request, exeption):
    return render(request, "404.html", status=http.HTTP_404_NOT_FOUND)


def category(request, cat_id):
    return render(request, "index.html")
