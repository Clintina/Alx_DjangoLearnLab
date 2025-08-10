from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import Book, Author

class BookViewTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2020,
            author=self.author
        )

    def test_list_books_returns_200(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book_returns_200(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_returns_201(self):
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book_returns_200(self):
        url = reverse('book-update')
        data = {
            'id': self.book.id,
            'title': 'Updated Title',
            'publication_year': 2025,
            'author': self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book_returns_204(self):
        url = reverse('book-delete')
        data = {'id': self.book.id}
        response = self.client.delete(url, data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)