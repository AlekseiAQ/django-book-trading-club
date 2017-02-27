from django.test import TestCase
from django.contrib.auth import get_user_model

from books.models import Book

User = get_user_model()


class BookModelTest(TestCase):
    
    def setUp(self):
        self.user = User()
        self.user.save()
        self.book = Book.objects.create(
            title='Some Title',
            author='Some Author',
            published_year=1900,
            user=self.user,
            slug='some-title-some-author',
        )

    def test_string_representation(self):
        self.assertEqual(str(self.book), '"Some Title" - Some Author')

    def test_get_absolute_url(self):
        self.assertEqual(self.book.get_absolute_url(), "/books/%s/" % (self.book.slug,))
