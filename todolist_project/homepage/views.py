from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskEdit(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('homepage:tasks')


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('homepage:tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('homepage:tasks')