from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import RegistrationForm
from django.contrib.auth import login
# Create your views here.
@login_required
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todoapp/index.html', {'todos' : todos, 'title' : 'Главная страница'})

@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    user = request.user
    todo = Todo(title=title, user=user)
    todo.save()
    return redirect('index')

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Перенаправьте на вашу домашнюю страницу
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})