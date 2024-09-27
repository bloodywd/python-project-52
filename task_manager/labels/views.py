from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label


class BaseLabelView(LoginRequiredMixin):
    model = Label
    form_class = LabelForm
    template_name = 'form.html'


class LabelIndexView(BaseLabelView, ListView):
    template_name = 'labels/index.html'
    extra_context = {'title': _("Labels")}


class LabelFormCreateView(BaseLabelView, SuccessMessageMixin, CreateView):
    success_url = reverse_lazy("labels")
    success_message = _("Label was created successfully")
    extra_context = {'title': _("Create label"), 'button_name': _('Create')}


class LabelFormUpdateView(BaseLabelView, SuccessMessageMixin, UpdateView):
    success_url = reverse_lazy("labels")
    success_message = _("Label was updated successfully")
    extra_context = {'title': _("Edit label"), 'button_name': _('Save')}


class LabelFormDeleteView(BaseLabelView, DeleteView):
    template_name = 'labels/label_delete.html'
    extra_context = {'title': _("Delete labels")}

    def post(self, request, *args, **kwargs):
        label = self.get_object()
        if label.has_tasks():
            messages.error(self.request, _('Label is on active task'))
            return redirect(reverse_lazy("labels"))
        else:
            label.delete()
            messages.success(self.request, _('Label was deleted successfully'))
            return HttpResponseRedirect(reverse_lazy("labels"))
