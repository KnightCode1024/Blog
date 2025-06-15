from django.shortcuts import render
from django.contrib.auth.views import LoginView

from users.forms import LoginUserForm


class Login(LoginView):
    form_class = LoginUserForm
    template_name = "login.html"


def register(request):
    return render(request, "register.html")


def profile(request):
    return render(request, "profile.html")
