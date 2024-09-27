from django.contrib import admin

from task_manager.tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ['name', 'creator', 'time_create']
    readonly_fields = ['time_create']
    list_display = ('id', 'name', 'time_create', 'author',
                    'task_perfomer', 'status')
    ordering = ['time_create']
