from django.shortcuts import render, get_object_or_404
from django import http
from django.db.models import Q
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    FormView,
    CreateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)


from posts.utils import PaginateByMixin
from posts.models import Post
from posts.forms import PostForm, SearchForm, ContactForm


class PageNotFoundView(View):
    def dispatch(self, request, exception=None, *args, **kwargs):
        return render(
            request,
            "404.html",
            status=http.HTTPStatus.NOT_FOUND,
        )


class Search(FormView):
    form_class = SearchForm
    template_name = "search.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["data"] = self.request.GET
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("search", "").strip()
        posts = Post.objects.all().order_by("-time_create")

        if query:
            posts = (
                posts.filter(
                    Q(title__icontains=query)
                    | Q(content__icontains=query)
                    | Q(summury__icontains=query)
                )
                .select_related("cat")
                .prefetch_related("tags")
            )

        context.update(
            {
                "posts": posts,
                "query": query,
                "count": posts.count(),
            }
        )
        return context


class AddPost(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = "add-post.html"
    success_url = reverse_lazy("index")
    permission_required = "post.add_post"

    def form_valid(self, form):
        p = form.save(commit=False)
        p.author = self.request.user
        return super().form_valid(form)


class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "add-post.html"
    success_url = reverse_lazy("index")
    slug_url_kwarg = "post_slug"
    slug_field = "slug"

    def has_permission(self):
        post = self.get_object()
        return post.author == self.request.user or super().has_permission()


class DeletePost(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("index")
    permission_required = "posts.delete_post"
    slug_url_kwarg = "post_slug"
    slug_field = "slug"

    def has_permission(self):
        post = self.get_object()
        return post.author == self.request.user or super().has_permission()


class Index(PaginateByMixin, ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return (
            Post.published.all()
            .order_by("-time_create")
            .select_related("cat")
            .prefetch_related("tags")
        )


class Category(PaginateByMixin, ListView):
    template_name = "posts_by_cat.html"
    context_object_name = "posts"
    allow_empty = False

    def get_queryset(self):
        return (
            Post.published.filter(cat__slug=self.kwargs["cat_slug"])
            .select_related("cat")
            .prefetch_related("tags")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Tag(ListView):
    template_name = "posts_by_tag.html"
    context_object_name = "posts"
    allow_empty = False
    paginate_by = 12

    def get_queryset(self):
        return (
            Post.published.filter(tags__slug=self.kwargs["tag_slug"])
            .select_related("cat")
            .prefetch_related("tags")
        )


class ShowPost(DetailView):
    template_name = "post.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    def get_object(self, queryset=None):
        return get_object_or_404(
            Post.published, slug=self.kwargs[self.slug_url_kwarg]
        )


class Contact(LoginRequiredMixin, FormView):
    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
