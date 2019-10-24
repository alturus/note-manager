from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UsersTests(APITestCase):

    def test_create_user(self):
        """
        Ensure we can create a new user object.
        """
        url = reverse('user-list')
        data = {
            'username': 'testuser1',
            'password': 'testpassword1',
        }
        response = self.client.post(url, data, format='json')
        User = get_user_model()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser1')
        self.assertIsNotNone(response.data.get('access'))
        self.assertIsNotNone(response.data.get('refresh'))
