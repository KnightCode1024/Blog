from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


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
    path(
        "password-change/",
        views.PasswordChange.as_view(),
        name="password_change",
    ),
    path(
        "password-change/done/",
        views.PasswordChangeDone.as_view(),
        name="password_change_done",
    ),
    path(
        "password-reset/",
        PasswordResetView.as_view(
            template_name="password_reset_form.html",
            email_template_name="password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(
            template_name="password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        PasswordResetCompleteView.as_view(
            template_name="password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
]
