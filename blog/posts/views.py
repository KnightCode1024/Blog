from django.shortcuts import render, get_object_or_404
from django import http

from posts.models import Post, Category, TagPost


def index(request):
    posts = Post.published.all()
    data = {
        "posts": posts,
    }
    return render(request, "index.html", data)


# TO DO: post and about views funcion dont DRY
def about(request):
    post = get_object_or_404(Post, slug="osnovatel")
    data = {
        "post": post,
    }
    return render(request, "post.html", data)


def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    data = {
        "post": post,
    }
    return render(request, "post.html", data)


def page_not_found(request, exeption):
    return render(request, "404.html", status=http.HTTP_404_NOT_FOUND)


def category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Post.published.filter(cat_id=category.pk)

    data = {
        "title": f"Посты из категории: {category.name}",
        "posts": posts,
    }
    return render(request, "posts_by_cat.html", data)


def tag(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Post.Status.PUBLISHED)

    data = {
        "title": f"Посты с тегом: {tag.tag}",
        "posts": posts,
        # "current_tag": tag
    }
    return render(request, "posts_by_tag.html", data)
