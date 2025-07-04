from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
)


from users.forms import (
    LoginUserForm,
    RegisterUserForm,
    ProfileUserForm,
    UserPasswordChangeForm,
)


class Login(LoginView):
    form_class = LoginUserForm
    template_name = "login.html"


class Register(CreateView):
    form_class = RegisterUserForm
    template_name = "register.html"
    success_url = reverse_lazy("users:login")


class Profile(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = "profile.html"
    success_url = reverse_lazy("users:profile")

    def get_success_url(self):
        return reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user


class PasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "password_change_form.html"

    def dispatch(self, request, *args, **kwargs):
        if (
            hasattr(request.user, "social_auth")
            and request.user.social_auth.exists()
        ):
            messages.error(
                request,
                (
                    "Смена пароля недоступна для аккаунтов,"
                    "вошедших через социальные сети."
                ),
            )
            return redirect("users:profile")
        return super().dispatch(request, *args, **kwargs)


class PasswordChangeDone(PasswordChangeDoneView):
    template_name = "password_change_done.html"
