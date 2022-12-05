from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import DeleteView, CreateView, UpdateView

from apps.models import Task


# Create your views here.
class CustomRegistrationView(FormView):
    template_name = 'apps/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(CustomRegistrationView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(CustomRegistrationView, self).get(*args, **kwargs)

class CustomLoginView(LoginView):
    template_name = 'apps/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    # success_url = reverse_lazy('tasks')


class TaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'apps/task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['serach_input'] = search_input
        return context


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'apps/task_detail.html'
    context_object_name = 'task'


class CreateDetailView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'apps/task_form.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateDetailView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
