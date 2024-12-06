from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Task
from django.contrib.auth.models import User


class TaskIntegrationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_full_task_flow(self):
        # Add a new task
        add_task_data = {
            'title': "Full Task Flow",
            'description': "Full Task Flow Description"
        }
        response = self.client.post(reverse('add_task'), add_task_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))
        task = Task.objects.get(title="Full Task Flow")

        # Edit the task
        edit_task_data = {
            'title': "Updated Full Task",
            'description': "Updated Description"
        }
        response = self.client.post(
            reverse('edit_task', kwargs={'task_id': task.id}), edit_task_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))
        task.refresh_from_db()
        self.assertEqual(task.title, "Updated Full Task")
        self.assertEqual(task.description, "Updated Description")

        # Toggle the task as completed
        response = self.client.post(
            reverse('toggle_task_complete', kwargs={'task_id': task.id}))
        task.refresh_from_db()
        self.assertTrue(task.completed)

        # Delete the task
        response = self.client.post(
            reverse('delete_task', kwargs={'task_id': task.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))
        self.assertFalse(Task.objects.filter(id=task.id).exists())
