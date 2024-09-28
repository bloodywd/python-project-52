from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'task_perfomer', 'label']
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'label': _('Label'),
            'status': _('Status'),
            'task_perfomer': _('Task perfomer'),
        }
