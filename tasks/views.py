from django.shortcuts import render, redirect
from .models import *

from .forms import *

def index(request):
  tasks = Task.objects.all()

  forms = TaskForm()

  if request.method == 'POST':
    forms = TaskForm(request.POST)
    if forms.is_valid():
      forms.save()
    return redirect('/')

  context = {'tasks':tasks, 'forms':forms}
  return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
  task = Task.objects.get(id=pk)

  forms = TaskForm(instance=task)
  
  if request.method == 'POST':
    forms = TaskForm(request.POST, instance=task)
    if forms.is_valid():
      forms.save()
    return redirect('/')

  context = {'forms':forms}
  return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
  items = Task.objects.get(id=pk)

  if request.method == 'POST':
    items.delete()
    return redirect('/')

  context = {'items':items}
  return render(request, 'tasks/delete.html', context)