from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Task
from django.contrib.auth.models import User


class TaskViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')

    def test_task_list_view(self):
        task = Task.objects.create(
            title="Test Task",
            description="Test Task Description",
            created_at=timezone.now()
        )
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
        self.assertTemplateUsed(response, 'tasks/task_list.html')

    def test_add_task_view(self):
        response = self.client.get(reverse('add_task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_form.html')

    def test_add_task_post(self):
        data = {
            'title': "New Task",
            'description': "New Task Description"
        }
        response = self.client.post(reverse('add_task'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))
        self.assertTrue(Task.objects.filter(title="New Task").exists())

    def test_edit_task_view(self):
        task = Task.objects.create(
            title="Editable Task",
            description="Editable Task Description",
            created_at=timezone.now()
        )
        response = self.client.get(
            reverse('edit_task', kwargs={'task_id': task.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_form.html')
        self.assertContains(response, task.title)

    def test_edit_task_post(self):
        task = Task.objects.create(
            title="Task to Edit",
            description="Task Description",
            created_at=timezone.now()
        )
        data = {
            'title': "Updated Task",
            'description': "Updated Task Description"
        }
        response = self.client.post(
            reverse('edit_task', kwargs={'task_id': task.id}), data)
        task.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))
        self.assertEqual(task.title, "Updated Task")
        self.assertEqual(task.description, "Updated Task Description")

    def test_toggle_task_complete(self):
        task = Task.objects.create(
            title="Task to Toggle",
            description="Task Description",
            created_at=timezone.now()
        )
        response = self.client.post(
            reverse('toggle_task_complete', kwargs={'task_id': task.id}))
        task.refresh_from_db()
        self.assertTrue(task.completed)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))

    def test_delete_task(self):
        task = Task.objects.create(
            title="Task to Delete",
            description="Task Description",
            created_at=timezone.now()
        )
        response = self.client.post(
            reverse('delete_task', kwargs={'task_id': task.id}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('task_list'))
        self.assertFalse(Task.objects.filter(id=task.id).exists())
