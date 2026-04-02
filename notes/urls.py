from django.urls import path
from .views import (
    NoteListView, NoteCreateView, NoteUpdateView, NoteDeleteView
)

# URL patterns for Note CRUD operations
urlpatterns = [
    # List all notes
    path('', NoteListView.as_view(), name='note_list'),
    # Create a new note
    path('new/', NoteCreateView.as_view(), name='note_create'),
    # Update an existing note by its primary key
    path('edit/<int:pk>/', NoteUpdateView.as_view(), name='note_update'),
    # Delete a specific note
    path('delete/<int:pk>/', NoteDeleteView.as_view(), name='note_delete'),
]
