from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from django.contrib import messages
from django.shortcuts import redirect


class BaseLabelView(LoginRequiredMixin):
    model = Status
    form_class = StatusForm
    template_name = 'form.html'


class StatusIndexView(BaseLabelView, ListView):
    template_name = 'statuses/index.html'
    extra_context = {'title': _("Status list")}


class StatusFormCreateView(BaseLabelView, SuccessMessageMixin,
                           CreateView):
    success_url = reverse_lazy("statuses")
    success_message = _("Status was created successfully")
    extra_context = {'title': _("Create status"), 'button_name': _('Create')}

    def form_valid(self, form):
        status = form.save(commit=False)
        status.creator = self.request.user
        return super().form_valid(form)


class StatusFormUpdateView(BaseLabelView, SuccessMessageMixin,
                           UpdateView):
    success_url = reverse_lazy("statuses")
    success_message = _("Status was updated successfully")
    extra_context = {'title': _("Edit status"), 'button_name': _('Edit')}

    def form_valid(self, form):
        status = form.save(commit=False)
        status.creator = self.request.user
        return super().form_valid(form)


class StatusFormDeleteView(BaseLabelView, SuccessMessageMixin,
                           DeleteView):
    template_name = 'statuses/status_delete.html'
    extra_context = {'title': _("Delete status")}

    def post(self, request, *args, **kwargs):
        status = self.get_object()
        if status.has_tasks():
            messages.error(self.request, _('Status is on use'))
            return redirect(reverse_lazy("statuses"))
        else:
            status.delete()
            messages.success(self.request,
                             _('Status was deleted successfully'))
            return HttpResponseRedirect(reverse_lazy("statuses"))
