from django.shortcuts import render, get_object_or_404

from .models import Book


def book_detail(request, slug=None):
    instance = get_object_or_404(Book, slug=slug)
    context = {
        "title": instance.title,
        "author": instance.author,
        "published_year": instance.published_year,
        "user": instance.user,
        "added_date": instance.added_date,
        "description": instance.description,
    }
    return render(request, "book_detail.html", context)


def book_list(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, 'book_list.html', context)
