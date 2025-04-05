from django.db import models
from django.contrib.auth.models import User # Import the built-in User model

# Create your models here.

class TodoItem(models.Model):
    # Define status choices
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    # Link to the user who owns this todo item
    # If the User is deleted, also delete their TodoItems (CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

    # The main title/text of the todo
    title = models.CharField(max_length=200)

    # Optional longer description
    description = models.TextField(blank=True, null=True)

    # Status of the todo item, using the choices defined above
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING' # Default status when a new item is created
    )

    # Timestamp when the item was created (automatically set)
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp when the item was last updated (automatically updated on save)
    updated_at = models.DateTimeField(auto_now=True)

    # --- Optional Image Field ---
    # Uncomment the following lines if you want to add image uploads
    # Make sure to install Pillow first: pip install Pillow
    # And configure MEDIA_ROOT and MEDIA_URL in settings.py
    # image = models.ImageField(upload_to='todo_images/', blank=True, null=True)
    # -----------------------------

    def __str__(self):
        # How the object will be represented as a string (e.g., in the admin site)
        return f"{self.title} ({self.user.username})"

    class Meta:
        # Optional: Define default ordering for querysets
        ordering = ['-created_at'] # Show newest items first by default