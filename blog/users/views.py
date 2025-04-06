from django.shortcuts import render


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def lk(request):
    return render(request, "lk.html")
