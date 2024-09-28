from django.contrib.auth import get_user_model
from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django import forms
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from django.utils.translation import gettext_lazy as _


class TaskFilter(FilterSet):
    label = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=_('Label'),
        label_suffix=""
    )

    own_tasks = BooleanFilter(
        label=_('Only own tasks'),
        widget=forms.CheckboxInput,
        method='get_own_tasks',
        label_suffix=""
    )

    executor = ModelChoiceFilter(
        queryset=get_user_model().objects.all(),
        label=_('Task Performer'),
        label_suffix=""
    )

    status = ModelChoiceFilter(
        queryset=Status.objects.all(),
        label=_('Status'),
        label_suffix=""
    )

    def get_own_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor']
