from django.db import models


class Note(models.Model):
    """Model representing a simple text-based note."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Automatically set the field to now when the object is first created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the Note object."""
        return self.title

