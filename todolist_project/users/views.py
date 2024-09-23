from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login


class Login(LoginView):
    template_name = 'users/login.html'
    fields = ('username', 'password')
    redirect_authenticated_user = True

    def get_redirect_url(self):
        return reverse_lazy('homepage:tasks')


class RegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('homepage:tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            auth_login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('homepage:tasks')
        return super(RegisterView, self).get(*args, **kwargs)