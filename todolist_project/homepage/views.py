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
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('homepage:tasks')


class TaskList(RestrictedMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()
        return context

class TaskEdit(RestrictedMixin, FormMixin, UpdateView):
    pass

class TaskCreate(RestrictedMixin, FormMixin, CreateView):
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskDelete(RestrictedMixin, FormMixin, DeleteView):
    context_object_name = 'task'