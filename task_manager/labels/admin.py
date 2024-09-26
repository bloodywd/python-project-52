from django.contrib import admin
from task_manager.labels.models import Label


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('name', 'time_create', 'time_update')
    fields = ['name', ]
