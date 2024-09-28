from django.contrib.auth import get_user_model
from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                                related_name='statuses_created', null=True,
                                default=None)

    def has_tasks(self):
        return Status.objects.get(id=self.id).tasks.exists()

    def __str__(self):
        return self.name
