from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label


class LabelIndexView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/index.html'
    extra_context = {'title': "Labels"}


class LabelFormCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    fields = ['name',]
    template_name = 'form.html'
    success_url = reverse_lazy("labels")
    success_message = _("Label was created successfully")
    extra_context = {'title': "Create label", 'button_name': 'Create'}


class LabelFormUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    fields = ['name',]
    template_name = 'form.html'
    success_url = reverse_lazy("labels")
    success_message = _("Label was updated successfully")
    extra_context = {'title': "Edit label", 'button_name': 'Save'}


class LabelFormDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/label_delete.html'
    extra_context = {'title': "Delete labels"}

    def post(self, request, *args, **kwargs):
        label = self.get_object()
        if label.has_tasks():
            messages.error(self.request, 'Label is on active task')
            return redirect(reverse_lazy("labels"))
        else:
            label.delete()
            messages.success(self.request, 'Label was deleted successfully')
            return HttpResponseRedirect(reverse_lazy("labels"))
