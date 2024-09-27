from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


class StatusIndexView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/index.html'
    extra_context = {'title': _("Statuses")}


class StatusFormCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    template_name = 'form.html'
    success_url = reverse_lazy("statuses")
    success_message = _("Status was created successfully")
    extra_context = {'title': _("Create status"), 'button_name': _('Create')}

    def form_valid(self, form):
        status = form.save(commit=False)
        status.creator = self.request.user
        return super().form_valid(form)


class StatusFormUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'form.html'
    success_url = reverse_lazy("statuses")
    success_message = _("Status was updated successfully")
    extra_context = {'title': _("Edit status"), 'button_name': _('Save')}

    def form_valid(self, form):
        status = form.save(commit=False)
        status.creator = self.request.user
        return super().form_valid(form)


class StatusFormDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/status_delete.html'
    success_url = reverse_lazy("statuses")
    extra_context = {'title': _("Delete status")}
    success_message = _("Status was deleted successfully")
