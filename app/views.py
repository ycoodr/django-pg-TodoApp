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
