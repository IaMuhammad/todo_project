"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps import views
from apps.views import TaskView, TaskDetailView, CreateDetailView, TaskUpdate, DeleteTaskView, CustomLoginView, \
    CustomRegistrationView

urlpatterns = [
    path('', TaskView.as_view(), name='tasks'),
    path('register', CustomRegistrationView.as_view(), name='register'),
    path('login', CustomLoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='tasks'), name='logout'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task'),
    path('task-edit/<int:pk>', TaskUpdate.as_view(), name='task_update'),
    path('task-create/', CreateDetailView.as_view(), name='create_task'),
    path('task-delete/<int:pk>', DeleteTaskView.as_view(), name='delete_task'),
]
