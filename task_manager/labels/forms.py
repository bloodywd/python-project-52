from django import forms
from .models import Label
from django.utils.translation import gettext_lazy as _

class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name', ]
        labels = {
            'name': _('Name'),
            'time_create': _('Time Created'),
            'time_update': _('Time Updated'),
        }
