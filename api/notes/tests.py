from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from api.categories.models import Category
from api.notes.models import Note


class NoteTests(APITestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        User = get_user_model()
        user = User.objects.create(username='testuser1')
        self.url = reverse('note-list')
        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def create_note(self, title):
        category_name = 'Test category'
        category = Category.objects.create(name=category_name)
        data = {
            'title': title,
            'body': 'test',
            'category': category_name,
        }
        response = self.client.post(self.url, data, format='json')
        return response

    def test_create_and_retrieve_note(self):
        """
        Ensure we can create a new note and then retrieve it
        """
        new_note_title = 'New Note'
        response = self.create_note(new_note_title)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        note = Note.objects.get()
        self.assertEqual(note.title, new_note_title)

    def test_authorization_is_required(self):
        """
        Ensure we can't create a new note without authorization
        """
        new_client = APIClient()
        new_note_title = 'New Note'
        data = {'title': new_note_title, }
        response = new_client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_note_list(self):
        """
        Ensure we can retrieve notes
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)

    def test_update_note(self):
        """
        Ensure we can update a note
        """
        note_title = 'Test note'
        response = self.create_note(note_title)
        new_note_title1 = 'Test note new title 1'
        new_note_title2 = 'Test note new title 2'
        note_data = response.data
        url = reverse('note-detail', kwargs={'pk': note_data['uuid']})
        note_data.update({
            'title': new_note_title1,
        })
        response = self.client.put(url, data=note_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], new_note_title1)

        note_data = {
            'title': new_note_title2,
        }
        response = self.client.patch(url, data=note_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], new_note_title2)

    def test_delete_note(self):
        """
        Ensure we can delete a note
        """
        note_title = 'Test note'
        response = self.create_note(note_title)
        note_data = response.data
        url = reverse('note-detail', kwargs={'pk': note_data['uuid']})
        self.assertEqual(Note.objects.count(), 1)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 0)
