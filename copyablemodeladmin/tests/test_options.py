from __future__ import unicode_literals

from django.test import TestCase

from wagtail.tests.utils import WagtailTestUtils

from copyablemodeladmin.tests.copyabletestapp.models import Author
from model_mommy import mommy


class TestCopyableModelAdmin(TestCase, WagtailTestUtils):

    def setUp(self):
        self.author = mommy.make(Author, name="J. R. R. Tolkien")
        self.login()

    def test_author_copyable(self):
        response = self.client.get('/admin/copyabletestapp/author/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Copy this author')

    def test_copy_author(self):
        self.assertEqual(Author.objects.count(), 1)

        num_authors = Author.objects.count()

        existing_url = (
            '/admin/copyabletestapp/author/copy/' +
            str(self.author.pk) +
            '/'
        )
        response = self.client.get(existing_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Author.objects.count(), num_authors + 1)
