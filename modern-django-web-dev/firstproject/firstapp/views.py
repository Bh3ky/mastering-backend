from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("<h2>Hello, World. This is the home page of FirstApp.</h2>")


def about(request):
    return HttpResponse("<h2>Know more about FirstApp.</h2>")


def user(request, name):
    return HttpResponse(f"<h2>Hello, {name}. Welcome to the home page of FirstApp.</h2>")