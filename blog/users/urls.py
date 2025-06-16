from django.urls import path
from django.contrib.auth.views import LogoutView

from users import views

app_name = "users"

urlpatterns = [
    path(
        "login/",
        views.Login.as_view(),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    path(
        "register/",
        views.Register.as_view(),
        name="register",
    ),
    path(
        "profile/",
        views.Profile.as_view(),
        name="profile",
    ),
]
