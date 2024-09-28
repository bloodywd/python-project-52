from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, UpdateView,
                                  DeleteView, DetailView)
from django.utils.translation import gettext_lazy as _
from django_filters.views import FilterView

from task_manager.tasks.filters import TaskFilter
from task_manager.tasks.forms import TaskForm
from task_manager.tasks.models import Task


class BaseLabelView(LoginRequiredMixin):
    model = Task
    form_class = TaskForm
    template_name = 'form.html'


class TaskIndexView(BaseLabelView, FilterView):
    template_name = 'tasks/index.html'
    extra_context = {'title': _("Tasks")}
    filterset_class = TaskFilter


class TaskView(BaseLabelView, DetailView):
    context_object_name = 'task'
    template_name = 'tasks/task.html'
    extra_context = {'title': _("View task")}


class TaskFormCreateView(BaseLabelView, SuccessMessageMixin, CreateView):
    success_url = reverse_lazy("tasks")
    success_message = _("Task was created successfully")
    extra_context = {'title': _("Create task"), 'button_name': _('Create')}

    def form_valid(self, form):
        status = form.save(commit=False)
        status.author = self.request.user
        return super().form_valid(form)


class TaskFormUpdateView(BaseLabelView, SuccessMessageMixin,
                         UpdateView):
    success_url = reverse_lazy("tasks")
    success_message = _("Task was updated successfully")
    extra_context = {'title': _("Edit task"), 'button_name': _('Edit')}


class TaskFormDeleteView(PermissionRequiredMixin, SuccessMessageMixin,
                         DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy("tasks")
    extra_context = {'title': _("Delete tasks")}
    success_message = _("Task was deleted successfully")
    permission_denied_message = _('Task can be deleted only be it\'s author')

    def has_permission(self):
        task = Task.objects.get(id=self.kwargs['pk'])
        if task.author:
            return self.request.user.pk == task.author.id

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, _("You need to be logged in"))
            return redirect(self.get_login_url())
        else:
            messages.error(self.request, self.permission_denied_message)
            return redirect(reverse_lazy("tasks"))
