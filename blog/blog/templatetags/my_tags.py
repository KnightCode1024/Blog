from django import template

from blog import views

register = template.Library()


@register.simple_tag(name="getcats")
def get_categories():
    return views.cats_db


@register.inclusion_tag("list_categories.html")
def show_categories():
    cats = views.cats_db
    return {
        "cats": cats,
    }
