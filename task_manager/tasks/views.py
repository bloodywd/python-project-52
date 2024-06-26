from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils.translation import gettext_lazy as _

from task_manager.tasks.models import Task


class TaskIndexView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'
    extra_context = {'title': "Tasks"}


class TaskView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks/task.html'
    extra_context = {'title': "View task"}


class TaskFormCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'label', 'status', 'task_perfomer', ]
    template_name = 'form.html'
    success_url = reverse_lazy("tasks")
    success_message = _("Task was created successfully")
    extra_context = {'title': "Create task", 'button_name': 'Create'}

    def form_valid(self, form):
        status = form.save(commit=False)
        status.author = self.request.user
        return super().form_valid(form)


class TaskFormUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'label', 'status', 'task_perfomer', ]
    template_name = 'form.html'
    success_url = reverse_lazy("tasks")
    success_message = _("Task was updated successfully")
    extra_context = {'title': "Edit task", 'button_name': 'Save'}


class TaskFormDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy("tasks")
    extra_context = {'title': "Delete tasks"}
    success_message = _("Task was deleted successfully")
    permission_denied_message = 'Task can be deleted only be it\'s author'

    def has_permission(self):
        task = Task.objects.get(id=self.kwargs['pk'])
        if task.author:
            return self.request.user.pk == task.author.id

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, "You need to be logged in")
            return redirect(self.get_login_url())
        else:
            messages.error(self.request, self.permission_denied_message)
            return redirect(reverse_lazy("tasks"))
