from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
# Create your views here.

@login_required
def index (request):
    tasks = Task.objects.filter(creator=request.user)
    form =Taskform()

    if request.method =='POST':

        form = Taskform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.creator = request.user
            task.save()
        return redirect('/')


    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    if task.creator != request.user:
        return redirect('/')

    form = Taskform(instance=task)

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'tasks/update_task.html', context)

def deletetask(request, pk):
    item = Task.objects.get(id=pk)
    if item.creator != request.user:
        return redirect('/')

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item' : item}
    return render(request, 'tasks/delete.html',context)

def indexhtml(request):
    if request.user.is_authenticated:
        return redirect('list')
    return render(request,'tasks/index.html')
        
def abouthtml(request):
    return render(request,'tasks/about.html')