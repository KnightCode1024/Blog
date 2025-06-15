from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control bg-dark text-white border-light",
                "placeholder": "Введите имя пользователя",
            }
        ),
    )
    password = forms.CharField(
        label="Пароль",
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control bg-dark text-white border-light",
                "placeholder": "Введите пароль",
            }
        ),
    )

    error_messages = {
        "invalid_login": (
            "Пожалуйста, введите правильныеимя пользователя и пароль."
        ),
        "inactive": "Этот аккаунт неактивен.",
    }

    class Meta:
        model = get_user_model()
