from django.shortcuts import render, get_object_or_404, redirect, reverse
from django import http
from django.db.models import Q

from posts.models import Post, Category, TagPost
from posts.forms import AddPostForm, SearchForm


def index(request):
    posts = Post.published.all().select_related("cat").prefetch_related("tags")
    data = {
        "posts": posts,
    }
    return render(
        request,
        "index.html",
        data,
    )


def about(request):
    post = get_object_or_404(Post, slug="osnovatel")
    data = {
        "post": post,
    }
    return render(
        request,
        "post.html",
        data,
    )


def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    data = {
        "post": post,
    }
    return render(
        request,
        "post.html",
        data,
    )


def page_not_found(request, exeption):
    return render(
        request,
        "404.html",
        status=http.HTTP_404_NOT_FOUND,
    )


def category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = (
        Post.published.filter(cat_id=category.pk)
        .select_related("cat")
        .prefetch_related("tags")
    )

    data = {
        "title": f"Посты из категории: {category.name}",
        "posts": posts,
    }
    return render(
        request,
        "posts_by_cat.html",
        data,
    )


def tag(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = (
        tag.tags.filter(is_published=Post.Status.PUBLISHED)
        .select_related("cat")
        .prefetch_related("tags")
    )

    data = {
        "title": f"Посты с тегом: {tag.tag}",
        "posts": posts,
    }
    return render(
        request,
        "posts_by_tag.html",
        data,
    )


def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse("index"))
            except Exception as e:
                form.add_error(None, f"Ошибка добавления поста: {str(e)}")
    else:
        form = AddPostForm()

    data = {
        "form": form,
    }
    return render(
        request,
        "add-post.html",
        data,
    )


def search(request):
    form = SearchForm(request.GET or None)
    posts = []
    query = None
    count = 0

    if form.is_valid():
        query = form.cleaned_data["search"]
        if query:
            posts = (
                Post.objects.filter(
                    Q(title__icontains=query)
                    | Q(content__icontains=query)
                    | Q(summury__icontains=query)
                )
                .select_related("cat")
                .prefetch_related("tags")
                .order_by("-time_create")
            )
            count = len(posts)

    data = {
        "posts": posts,
        "query": query,
        "count": count,
        "form": form,
    }
    return render(
        request,
        "search.html",
        data,
    )
