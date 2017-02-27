from django.shortcuts import render, get_object_or_404

from .models import Book


def book_detail(request, slug=None):
    book = get_object_or_404(Book, slug=slug)
    context = {
        "book": book,
    }
    return render(request, "book_detail.html", context)


def book_list(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'book_list.html', context)
