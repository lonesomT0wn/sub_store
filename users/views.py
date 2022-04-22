from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.


def login(request):
    path = request.path
    method_items = {
        "login": "login",
        "sign_up": "sign_up",
        'path': path,
    }
    return render(request, "users/login.html", context=method_items)


def sign_up(request):
    path = request.path
    method_items = {
        "login": "login",
        "sign_up": "sign_up",
        'path': path,
    }
    return render(request, "users/sign-up.html", context=method_items)


def redirect(request):
    try:
        return HttpResponseRedirect(reverse("page"))
    except Exception as e:
        raise Http404("Page not found")
