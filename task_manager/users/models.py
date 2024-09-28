from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def has_tasks(self):
        return (User.objects.get(id=self.id).tasks.exists() or
                User.objects.get(id=self.id).tasks_created.exists())

    def __str__(self):
        return self.get_full_name()
