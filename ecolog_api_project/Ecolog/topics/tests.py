from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from categories.models import Category
from topics.models import Topic
from rest_framework_simplejwt.tokens import AccessToken # <-- NEW IMPORT

class TopicTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword'
        )
        # Create a test category
        self.category = Category.objects.create(name='Geology', description='Study of Earth')
        # Create a test topic linked to the user and category
        self.topic = Topic.objects.create(
            title='Test Topic',
            content='This is a test topic.',
            owner=self.user,
            category=self.category
        )
        # Get the URL for the topic list endpoint
        self.topic_list_url = reverse('topic-list')
        
        # --- NEW CODE FOR JWT AUTHENTICATION ---
        # Obtain a token for the test user
        token = AccessToken.for_user(self.user)
        # Set the token in the client's Authorization header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_authenticated_user_can_create_topic(self):
        """
        Ensure an authenticated user can create a new topic.
        """
        data = {
            'title': 'New Topic',
            'content': 'Content of the new topic.',
            'category': self.category.id
        }
        response = self.client.post(self.topic_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Topic.objects.count(), 2)
        self.assertEqual(Topic.objects.get(title='New Topic').owner, self.user)

    def test_unauthenticated_user_cannot_create_topic(self):
        """
        Ensure an unauthenticated user cannot create a topic.
        """
        # Remove the credentials to simulate an unauthenticated user
        self.client.credentials() 
        data = {
            'title': 'Another Topic',
            'content': 'Some content.',
            'category': self.category.id
        }
        response = self.client.post(self.topic_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Topic.objects.count(), 1)