from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django import forms
from task_manager.labels.models import Label
from task_manager.tasks.models import Task


class TaskFilter(FilterSet):
    label = ModelChoiceFilter(
        queryset = Label.objects.all(),
        label = 'Label'
    )

    own_tasks = BooleanFilter(
        label= 'Only own tasks',
        widget=forms.CheckboxInput,
        method='get_own_tasks',
    )

    def get_own_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'task_perfomer']
