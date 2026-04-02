from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    """Form for creating and updating Note instances."""
    class Meta:
        model = Note
        fields = ['title', 'content']
        # Apply Bootstrap classes and placeholders to widgets
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Note Title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Write your note here...'
            }),
        }

