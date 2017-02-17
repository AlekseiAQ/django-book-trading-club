from django.conf.urls import url

from books.views import book_detail


urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/', book_detail, name='detail'),
]
