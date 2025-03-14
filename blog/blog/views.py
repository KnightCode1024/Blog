from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    data = {
        "title": "Об авторе",
        "author_name": "Кирилл Никитин",
        "text": "Какой-то текст об авторе",
    }
    return render(request, "about.html", data)


def post(request, post_id):
    data = {
        "title": "Пост об разработчике",
        "content": "Что-то делал. Как-то учился. И докатился",
        "author": "Основатель",
    }
    return render(request, "post.html", data)


def page_not_found(request, exeption):
    return render(request, "404.html", status=404)
