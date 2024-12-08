from .forms import TaskForm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm  # Import the form for handling task creation
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

def task_list(request):
    # Ordering tasks by creation date (newest first)
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def toggle_task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            form.save()  # Save the task to the database
            # Redirect to the task list page after saving
            return redirect('task_list')
    else:
        form = TaskForm()  # Create an empty form for GET requests
    return render(request, 'task_form.html', {'form': form})


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')


def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')


# views.py


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Get the task by its ID

    if request.method == 'POST':
        # Bind form with existing task
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # Save the updated task
            return redirect('task_list')  # Redirect to task list after saving
    else:
        # If it's a GET request, show the form with existing task data
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form})


def toggle_task_status(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        
        # Toggle the completed status of the task
        task.completed = not task.completed
        task.save()
        
        # Return the updated task status as JSON
        return JsonResponse({'completed': task.completed})

    return JsonResponse({'error': 'Invalid request'}, status=400)
    
def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})
