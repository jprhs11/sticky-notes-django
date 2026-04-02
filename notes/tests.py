from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteTestCase(TestCase):
    def setUp(self):
        # Create a sample note for testing
        self.note = Note.objects.create(
            title="Test Note", 
            content="This is a test content"
        )

    def test_note_content(self):
        """Test if the note was created with the correct title"""
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, "Test Note")

    def test_list_view(self):
        """Test if the home page loads correctly (Status 200)"""
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_create_note_view(self):
        """Test the POST request to create a new note"""
        response = self.client.post(reverse('note_create'), {
            'title': 'New Test',
            'content': 'New Content'
        })
        self.assertEqual(response.status_code, 302) # Redirects after success
        self.assertEqual(Note.objects.count(), 2)
