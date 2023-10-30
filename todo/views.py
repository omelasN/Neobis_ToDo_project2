from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from.models import ToDo


def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, "test.html", context)

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)
