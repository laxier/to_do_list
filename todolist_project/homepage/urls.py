from django.urls import path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.TaskList.as_view(), name='tasks'),
    path('task-update/<int:pk>/', views.TaskEdit.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', views.TaskDelete.as_view(), name='task-delete'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
]
