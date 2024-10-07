from django.shortcuts import render, redirect
from .models import Todo, Category
from .forms import UserRegisterForm, TaskForm
from django.contrib import messages

def todo_list(request):
    sort_by = request.GET.get('sort_by')
    category = request.GET.get('category')

    todos = Todo.objects.filter(user=request.user)

    if category:
        todos = todos.filter(category__name=category)

    if sort_by == 'due_date':
        todos = todos.order_by('due_date')
    elif sort_by == 'priority':
        todos = todos.order_by('-priority')
    else:
        todos = todos.order_by('-id')

    categories = Category.objects.all()  # To fetch categories for the dropdown
    return render(request, 'todo/index.html', {'todos': todos, 'categories': categories})

def create_todo(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TaskForm()
    return render(request, 'todo/create.html', {'form': form})

def complete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todo_list')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
