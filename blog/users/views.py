from django.shortcuts import render  # get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView

from users.forms import LoginUserForm


class Login(LoginView):
    form_class = LoginUserForm
    template_name = "login.html"


def register(request):
    return render(request, "register.html")


def profile(request):
    return render(request, "profile.html")


class Profile(DetailView):
    template_name = "profile.html"
    slug_url_kwarg = "post_slug"
    context_object_name = "post"

    # def get_object(self, queryset=None):
    #     return get_object_or_404(
    #         Post.published, slug=self.kwargs[self.slug_url_kwarg]
    #     )
