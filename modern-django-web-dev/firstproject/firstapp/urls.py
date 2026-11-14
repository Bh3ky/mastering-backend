from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("books/", views.books, name="books"),
    path("book/<int:id>/", views.book, name="book"),
    path("user/<name>/", views.user, name="user"),
]