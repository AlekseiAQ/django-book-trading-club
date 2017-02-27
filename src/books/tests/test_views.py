from django.test import TestCase
from django.contrib.auth import get_user_model

from books.models import Book

User = get_user_model()


class BookListViewTest(TestCase):

    def test_book_list_empty(self):
        response = self.client.get('/books/')
        self.assertEqual(list(response.context['books']), [])

    def test_book_list_not_empty(self):
        user = User()
        user.save()
        book_one = Book.objects.create(
            title='First Title',
            author='First Author',
            published_year=1900,
            user=user,
            slug='first-title-first-author',
        )
        book_two = Book.objects.create(
            title='Second Title',
            author='Second Author',
            published_year=1920,
            user=user,
            slug='second-title-second-author',
        )
        response = self.client.get('/books/')
        self.assertEqual(list(response.context['books']), [book_one, book_two])
    
    def test_book_detail(self):
        pass
