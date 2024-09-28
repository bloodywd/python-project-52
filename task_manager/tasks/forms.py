from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'label']
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'label': _('Labels'),
            'status': _('Status'),
            'executor': _('Task perfomer'),
        }
