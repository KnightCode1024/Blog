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


class RegisterUserForm(forms.ModelForm):
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
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control bg-dark text-white border-light",
                "placeholder": "Введите E-mail",
            }
        ),
    )
    first_name = forms.CharField(
        label="Имя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control bg-dark text-white border-light",
                "placeholder": "Введите имя",
            }
        ),
    )
    last_name = forms.CharField(
        label="Фамилия",
        widget=forms.TextInput(
            attrs={
                "class": "form-control bg-dark text-white border-light",
                "placeholder": "Введите фамилию",
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
    password2 = forms.CharField(
        label="Повторите пароль",
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control bg-dark text-white border-light",
                "placeholder": "Повторите пароль",
            }
        ),
    )

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password2",
        ]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return cd["password"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой email уже есть")
        return email
