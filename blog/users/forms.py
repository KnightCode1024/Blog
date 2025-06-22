from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm

import datetime


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин или Почта",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control bg-dark text-white border-light"}
        ),
    )
    password = forms.CharField(
        label="Пароль",
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control bg-dark text-white border-light"}
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


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control bg-dark text-white border-light"}
        ),
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={"class": "form-control bg-dark text-white border-light"}
        ),
    )
    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(
            attrs={"class": "form-control bg-dark text-white border-light"}
        ),
    )
    last_name = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(
            attrs={"class": "form-control bg-dark text-white border-light"}
        ),
    )
    password1 = forms.CharField(
        label="Пароль",
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control bg-dark text-white border-light"}
        ),
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control bg-dark text-white border-light"}
        ),
    )

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]
        widgets = {
            "email": forms.TextInput(
                attrs={"class": "form-control bg-dark text-white border-light"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control bg-dark text-white border-light"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control bg-dark text-white border-light"}
            ),
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой email уже есть")
        return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(
        disabled=True,
        label="Логин",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control bg-dark text-white border-light"}
        ),
    )
    email = forms.EmailField(
        disabled=True,
        label="E-mail",
        required=False,
        widget=forms.EmailInput(
            attrs={"class": "form-control bg-dark text-white border-light"}
        ),
    )
    this_year = datetime.date.today().year
    date_birth = forms.DateField(
        widget=forms.SelectDateWidget(
            years=tuple(range(this_year - 100, this_year - 5))
        )
    )

    class Meta:
        model = get_user_model()
        fields = [
            "photo",
            "username",
            "email",
            "date_birth",
            "first_name",
            "last_name",
        ]
        labels = {
            "first_name": "Имя",
            "last_name": "Фамилия",
        }
        widgets = {
            "email": forms.TextInput(
                attrs={"class": "form-control bg-dark text-white border-light"}
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control bg-dark text-white border-light"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control bg-dark text-white border-light"}
            ),
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Старый пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control bg-dark text-white border-light",
            }
        ),
    )
    new_password1 = forms.CharField(
        label="Новый пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control bg-dark text-white border-light",
            }
        ),
    )
    new_password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control bg-dark text-white border-light",
            }
        ),
    )
