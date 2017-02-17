from django.test import TestCase
from django.contrib.auth import get_user_model

from books.models import Book

User = get_user_model()


class BookModelTest(TestCase):
    
    def setUp(self):
        self.user = User()
        self.user.save()
    
    def test_string_representation(self):
        book = Book.objects.create(
            title='Some Title',
            author='Some Author',
            published_year=1900,
            user=self.user,
            slug='some-title-some-author',
        )
        self.assertEqual(str(book), '"Some Title" - Some Author')
