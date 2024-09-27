from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def has_tasks(self):
        return Label.objects.get(id=self.id).tasks.exists()

    def __str__(self):
        return self.name
