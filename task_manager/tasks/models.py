from django.contrib.auth import get_user_model
from django.db import models
from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,
                               related_name='tasks_created', null=True,
                               default='')
    status = models.ForeignKey(Status, on_delete=models.PROTECT,
                               related_name='tasks')
    executor = models.ForeignKey(get_user_model(), on_delete=models.PROTECT,
                                 related_name='tasks', null=True, default='')
    labels = models.ManyToManyField(Label, blank=True, related_name='tasks')

    def __str__(self):
        return self.name
