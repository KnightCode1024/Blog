from django.shortcuts import render  # get_object_or_404
from django.contrib.auth.views import LoginView

# from django.views.generic import DetailView

from users.forms import LoginUserForm, RegisterUserForm


class Login(LoginView):
    form_class = LoginUserForm
    template_name = "login.html"


def register(request):

    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return render(
                request,
                "register_done.html",
                {"form": form},
            )
    else:
        form = RegisterUserForm()
    return render(
        request,
        "register.html",
        {"form": form},
    )


def profile(request):
    return render(request, "profile.html")


# class Profile(DetailView):
#     template_name = "profile.html"
#     slug_url_kwarg = "post_slug"
#     context_object_name = "post"
