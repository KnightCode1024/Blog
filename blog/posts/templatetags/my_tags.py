from django import template

from posts.models import Category


register = template.Library()


@register.inclusion_tag("list_categories.html")
def show_categories():
    cats = Category.objects.all()
    return {
        "cats": cats,
    }
