from django.urls import path
from .views import task_list, add_task

app_name = 'tasks'

urlpatterns = [
    path('task/', task_list, name='task_list'),
    path('add_task/', add_task, name='add_task'),
]