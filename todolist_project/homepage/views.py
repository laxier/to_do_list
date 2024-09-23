from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
# Create your views here.

class TaskListView():
    pass

def taskList(request):
    return HttpResponse("12")