from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task

class RestrictedMixin(LoginRequiredMixin):
    pass

class FormMixin:
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('homepage:tasks')


class TaskList(RestrictedMixin, ListView):
    model = Task
    context_object_name = 'tasks'

class TaskEdit(RestrictedMixin, FormMixin, UpdateView):
    pass

class TaskCreate(RestrictedMixin, FormMixin, CreateView):
    pass

class TaskDelete(RestrictedMixin, FormMixin, DeleteView):
    context_object_name = 'task'