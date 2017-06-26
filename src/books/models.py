from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):

    title = models.CharField(max_length=120)
    author = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    published_year = models.IntegerField()
    added_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    # image =
    user = models.ForeignKey(User)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return '"%s" - %s' % (self.title, self.author)

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"slug": self.slug})
