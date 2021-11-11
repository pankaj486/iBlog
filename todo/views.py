from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
# Create your views here.



def create_todo(request):
    user = request.user
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            form = TodoForm()
        else:
            raise ValueError('Something went wrong!')
    else:
        form = TodoForm()

    todos = Todo.objects.filter(user=user)

    context = {
        'form': form,
        'todos': todos,
    }


    return render(request, 'todo/create_todo.html', context)


def edit_todo(request, id):
    to = Todo.objects.get(pk=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=to)
        if form.is_valid():
            form.save()
            form = TodoForm()
        else:
            raise ValueError('Something went wrong!')
    else:
        to = Todo.objects.get(pk=id)
        form = TodoForm(instance=to)

    context = {
        'form': form,
    }
    return render(request, 'todo/edit_todo.html', context)


def remove(request, id):
    if request.method == 'POST':
        deltodo = Todo.objects.get(pk=id)
        deltodo.delete()
        return redirect('todo')
