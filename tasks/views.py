from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Task

def index(request):
    return render(request, 'tasks/index.html', {
        'tasks': Task.objects.all(),
        'msg': messages
    })

def add(request):
    if request.method == "POST":
        f = TaskForm(request.POST)
        if f.is_valid():
            # allow duplicate entries
            f.save()
            messages.success(request, f'Task {f.cleaned_data["title"]} added.')
            return redirect('tasks:index')
        else:
            return render(request, 'tasks/add.html', {"form": f})
    else:
        return render(request, "tasks/add.html", {"form": TaskForm()})
    
def delete(request):
    if request.method == "POST":
        f = DeleteTaskForm(request.POST)
        if f.is_valid():
            t = f.cleaned_data["title"]
            task_list = Task.objects.filter(title=t)
            if len(task_list) > 0:
                # delete 1st task matching title
                task_list[0].delete()
                messages.success(request, f'Task {t} removed.')
                return redirect('tasks:index')
            else:
                messages.error(request, f'Task {t} does not exist')
                return redirect('tasks:index')
        else:
            return render(request, 'tasks/delete.html', {"form": f})
    else:
        return render(request, "tasks/delete.html", {"form": DeleteTaskForm()})


