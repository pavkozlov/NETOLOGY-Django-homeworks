from django.shortcuts import render
from .models import Book
from datetime import date, datetime


def books_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)


def all_books_view(request, pub_date=None):
    if pub_date:
        book_pd = datetime.strptime(pub_date, '%Y-%m-%d').date()
        books = Book.objects.filter(pub_date=book_pd)
        try:
            link_next = date(year=book_pd.year, month=book_pd.month, day=book_pd.day + 1).strftime('%Y-%m-%d')
        except ValueError:
            link_next = None
        try:
            link_prev = date(year=book_pd.year, month=book_pd.month, day=book_pd.day - 1).strftime('%Y-%m-%d')
        except ValueError:
            link_prev = None
    else:
        link_next = link_prev = None
        books = Book.objects.all()

    template = 'books/books_list.html'

    result = list()
    for book in books:
        res = {
            'name': book.name,
            'author': book.author,
            'pub_date': book.pub_date
        }
        result.append(res)
    context = {
        'books': result,
        'prev_link': link_prev,
        'next_link': link_next
    }
    return render(request, template, context)
