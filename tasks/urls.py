from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('tasks/', views.task_list, name='task_list'),
    path('add/', views.task_add, name='task_add'),
    path('complete/<int:task_id>/', views.task_complete, name='task_complete'),
    path('toggle/<int:task_id>/', views.toggle_task_complete, name='toggle_task_complete'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),

]
