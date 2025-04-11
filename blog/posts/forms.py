from django import forms
from posts.models import Category, TagPost, Author


class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "form-control bg-dark text-white",
                "placeholder": "Введите заголовок",
            }
        ),
    )
    slug = forms.SlugField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "form-control bg-dark text-white",
                "placeholder": "URL-адрес поста",
            }
        ),
    )
    summury = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control bg-dark text-white",
                "rows": 3,
                "placeholder": "Краткое описание",
            }
        ),
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control bg-dark text-white",
                "rows": 5,
                "placeholder": "Основной текст",
            }
        ),
    )
    is_published = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={"class": "form-check-input bg-dark text-white"}
        ),
    )
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select bg-dark text-white"}),
    )
    co_author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select bg-dark text-white"}),
    )
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select bg-dark text-white"}),
    )
    tags = forms.ModelChoiceField(
        queryset=TagPost.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select bg-dark text-white"}),
    )
