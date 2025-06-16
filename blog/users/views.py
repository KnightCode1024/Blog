from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from users.forms import (
    LoginUserForm,
    RegisterUserForm,
    ProfileEditForm,
)
from posts.models import Post


class Login(LoginView):
    form_class = LoginUserForm
    template_name = "login.html"


class Register(CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"
    success_url = reverse_lazy("users:login")


class Profile(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ProfileEditForm(instance=self.request.user)
        context["posts"] = Post.objects.filter(
            author=self.request.user
        ).order_by("-time_create")
        return context

    def post(self, request, *args, **kwargs):
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("users:profile"))
        return self.render_to_response(self.get_context_data(form=form))
