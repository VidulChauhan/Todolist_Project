from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    active_tasks = Task.objects.filter(completed=False)
    completed_tasks = Task.objects.filter(completed=True)
    return render(request, 'tasks/task_list.html', {
        'active_tasks': active_tasks,
        'completed_tasks': completed_tasks
    })

def toggle_task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')


def task_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'tasks/task_add.html')


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')


def task_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')
