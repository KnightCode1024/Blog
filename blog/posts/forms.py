from django import forms
from django.utils.text import slugify
from django.db import IntegrityError

from posts.models import Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "summury",
            "content",
            "is_published",
            "author",
            "cat",
            "tags",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control bg-dark text-white",
                    "placeholder": "Введите заголовок",
                }
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
            "author": forms.Select(
                attrs={
                    "class": "form-select bg-dark text-white",
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
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        base_slug = slugify(instance.title)
        instance.slug = base_slug

        for i in range(100):
            try:
                if commit:
                    instance.save()
                    self.save_m2m()
                return instance
            except IntegrityError:
                instance.slug = (
                    f"{base_slug}-{i+1}" if i > 0 else f"{base_slug}-1"
                )

        return instance


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=255,
        label="",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-dark",
                "placeholder": "Поиск",
            }
        ),
    )
