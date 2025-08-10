from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from books.models import Book
from django.contrib.auth.models import User

class BookAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create user if endpoints are protected
        self.user = User.objects.create_user(username='tester', password='pass123')
        self.client.force_authenticate(user=self.user)

        # Sample books
        self.book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
        self.book2 = Book.objects.create(title="Brave New World", author="Aldous Huxley", publication_year=1932)
        self.book3 = Book.objects.create(title="The Road", author="Cormac McCarthy", publication_year=2006)

        self.list_url = reverse('book-list')  # update if you're using routers

class BookViewTests(APITestCase):
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        data = {"title": "Dune", "author": "Frank Herbert", "publication_year": 1965}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], "Dune")

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        data = {"title": "Nineteen Eighty-Four", "author": "George Orwell", "publication_year": 1949}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Nineteen Eighty-Four")

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Book.objects.filter(id=self.book2.id).exists())

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 2)

    def test_filter_title_icontains(self):
        response = self.client.get(self.list_url, {'title__icontains': 'road'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['title'], "The Road")

    def test_search_books(self):
        response = self.client.get(self.list_url, {'search': 'orwell'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any("1984" in book['title'] for book in response.data))

    def test_ordering_books_by_year_desc(self):
        response = self.client.get(self.list_url, {'ordering': '-publication_year'})
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))