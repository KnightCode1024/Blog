from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
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


class ProfileEditForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]
        labels = {
            "username": "Логин",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "email": "Email",
        }

        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control bg-dark text-white border-light"}
            ),
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
