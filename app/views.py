from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    task = Task.objects.all()
    form = TaskForm()
    return render(request, 'index.html', {'task': task, 'form': form})

def update_task(request, key):
    task = Task.objects.get(id = key)
    form = TaskForm(instance = task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'update_task.html', {'form': form})

def delete_task(request, key):
    task = Task.objects.get(id = key)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete_task.html', {'task': task})