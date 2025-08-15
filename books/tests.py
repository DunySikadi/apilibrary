from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Un bon titre",
            subtitle="Un excellent sous-titre",
            author="Tom Christie",
            isbn="1234567890123",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "Un bon titre")
        self.assertEqual(self.book.subtitle, "Un excellent sous-titre")
        self.assertEqual(self.book.author, "Tom Christie")
        self.assertEqual(self.book.isbn, "1234567890123")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "excellent sous-titre")
        self.assertTemplateUsed(response, "books/book_list.html")