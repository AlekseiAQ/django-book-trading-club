from django.conf.urls import url

from books.views import book_detail, book_list


urlpatterns = [
    url(r'^$', book_list, name='list'),
    url(r'^(?P<slug>[\w-]+)/', book_detail, name='detail'),
]
