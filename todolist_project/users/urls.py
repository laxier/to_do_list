from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
]
