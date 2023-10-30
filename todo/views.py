from django.shortcuts import render
from django.shortcuts import HttpResponse
from.models import ToDo


def homepage(request):
    return render(request, "index.html")


def test(request):
    todo_list = ToDo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, "test.html", context)
