from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def has_tasks(self):
        return (User.objects.get(id=self.id).tasks.exists() or
                User.objects.get(id=self.id).tasks_created.exists())
