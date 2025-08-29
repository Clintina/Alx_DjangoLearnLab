from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post, Comment

User = get_user_model()

class PostCommentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(username='user1', password='pass123')
        self.user2 = User.objects.create_user(username='user2', password='pass123')
        self.client.force_authenticate(user=self.user1)

        self.post = Post.objects.create(author=self.user1, title='Test Post', content='Test Content')
        self.comment = Comment.objects.create(post=self.post, author=self.user1, content='Test Comment')

    def test_create_post(self):
        data = {'title': 'New Post', 'content': 'New Content'}
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Post')

    def test_update_own_post(self):
        data = {'title': 'Updated Title', 'content': 'Updated Content'}
        response = self.client.put(f'/api/posts/{self.post.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')

    def test_delete_own_post(self):
        response = self.client.delete(f'/api/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_cannot_edit_others_post(self):
        self.client.force_authenticate(user=self.user2)
        data = {'title': 'Hack Attempt'}
        response = self.client.put(f'/api/posts/{self.post.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_comment(self):
        data = {'post': self.post.id, 'content': 'New Comment'}
        response = self.client.post('/api/comments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['content'], 'New Comment')

    def test_filter_posts_by_title(self):
        response = self.client.get('/api/posts/?search=Test')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Test' in post['title'] for post in response.data['results']))
