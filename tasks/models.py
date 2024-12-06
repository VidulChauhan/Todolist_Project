
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    # Add this line to include description
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    # Automatically set when task is created
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
