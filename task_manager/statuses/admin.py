from django.contrib import admin

from task_manager.statuses.models import Status


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    fields = ['name', 'creator', 'time_create']
    readonly_fields = ['time_create']
    list_display = ('id', 'name', 'time_create', 'creator')
    ordering = ['time_create']
