from django.test import TestCase
from django.utils import timezone
from .models import Task


class TaskModelTests(TestCase):

    def test_task_creation(self):
        task = Task.objects.create(
            title="Test Task",
            description="Test Task Description",
            created_at=timezone.now()
        )
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Task Description")
        self.assertIsNotNone(task.created_at)
        self.assertFalse(task.completed)

    def test_str_method(self):
        task = Task.objects.create(
            title="Test Task",
            description="Test Task Description",
            created_at=timezone.now()
        )
        self.assertEqual(str(task), "Test Task")
