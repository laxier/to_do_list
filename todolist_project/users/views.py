from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class Login(LoginView):
    template_name = 'users/login.html'
    fields = ('username', 'password')
    redirect_authenticated_user = True

    def get_redirect_url(self):
        return reverse_lazy('homepage:tasks')

