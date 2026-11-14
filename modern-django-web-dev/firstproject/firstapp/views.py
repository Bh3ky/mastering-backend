import sqlite3

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("<h2>Know more about FirstApp.</h2>")


def user(request, name):
    return HttpResponse(f"<h2>Hello, {name}. Welcome to the home page of FirstApp.</h2>")


def books(request):
    conn=sqlite3.connect("mydata.sqlite3")

    try: 
        cur = conn.cursor()
        cur.execute("SELECT * FROM Books" )
        books = cur.fetchall()

    finally: 
        conn.close()
    
    return HttpResponse(str(books))


def book(request, id):
    conn = sqlite3.connect("mydata.sqlite3")

    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM Books WHERE id = ?", (id,))
        book = cur.fetchone()

    finally:
        conn.close()

    if book is None:
        return HttpResponse("Book not found", status=404)

    return HttpResponse(str(book))