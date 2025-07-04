from django import forms
from django.core.validators import MinLengthValidator
from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from posts.models import Post


@deconstructible
class BanWordValidator:
    BAN_WORD = "хуй"
    code = "ban_word"

    def __init__(self, msg=None):
        self.msg = msg if msg else "Не должно быть слова 'хуй'"

    def __call__(self, value, *args, **kwargs):
        if self.BAN_WORD in value.lower():
            raise ValidationError(self.msg, self.code)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "summury",
            "content",
            "is_published",
            "cat",
            "file",
            "image",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control bg-dark text-white",
                    "placeholder": "Введите заголовок",
                },
            ),
            "summury": forms.Textarea(
                attrs={
                    "class": "form-control bg-dark text-white",
                    "rows": 3,
                    "placeholder": "Краткое описание",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control bg-dark text-white",
                    "rows": 5,
                    "placeholder": "Основной текст",
                }
            ),
            "is_published": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input bg-dark text-white",
                }
            ),
            "cat": forms.Select(
                attrs={
                    "class": "form-select bg-dark text-white",
                }
            ),
            "tags": forms.SelectMultiple(
                attrs={
                    "class": "form-select bg-dark text-white",
                }
            ),
            "file": forms.FileInput(
                attrs={
                    "class": "form-control bg-dark text-white",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "form-control bg-dark text-white",
                    "accept": "image/*",
                }
            ),
        }
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        permissions = [
            ("change_post", "Can change post"),
            ("delete_post", "Can delete post"),
        ]

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) > 50:
            raise ValidationError("Длина привышает 50 символов")
        return title


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=255,
        required=False,
        validators=[
            MinLengthValidator(2, message="Минимум 2 символа"),
        ],
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-dark",
                "placeholder": "Поиск",
            }
        ),
    )

    def clean_search(self):
        search = self.cleaned_data.get("search", "").strip()
        if "хуй" in search.lower():
            raise ValidationError("Не должно быть запрещённых слов")
        return search


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Имя",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control bg-dark text-white border-light",
            }
        ),
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control bg-dark text-white border-light",
            }
        ),
    )
    content = forms.CharField(
        label="Обращение",
        widget=forms.Textarea(
            attrs={
                "class": "form-control bg-dark text-white border-light",
                "rows": 5,
            }
        ),
    )
    captcha = CaptchaField()
