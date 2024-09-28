from django.test import Client, TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class TaskTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user("test")
        self.status = Status.objects.create(name='NEW')
        self.client.force_login(self.user)

    def dropDown(self):
        Task.objects.clear()

    def test_create_task(self):
        self.assertFalse(Task.objects.filter(name='test').exists())
        response = self.client.post(reverse_lazy('create_task'),
                                    {
                                        'name': 'test',
                                        'status': self.status.id,
                                        'executor': self.user.id
                                    })
        print(response)
        self.assertTrue(Task.objects.filter(name='test').exists())

    def test_update_task(self):
        task = Task.objects.create(name='test', status=self.status,
                                   executor=self.user)
        task_pk = task.id
        url = reverse_lazy('update_task', kwargs={"pk": task_pk})
        response = self.client.post(url,
                                    {
                                        'name': 'updatetest',
                                        'status': self.status.id,
                                        'executor': self.user.id
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.get(id=task_pk).name, 'updatetest')

    def test_delete_status(self):
        task = Task.objects.create(name='test', status=self.status,
                                   author=self.user, executor=self.user)
        task_pk = task.id
        url = reverse_lazy('delete_task', kwargs={"pk": task_pk})
        self.client.post(url)
        self.assertFalse(Task.objects.filter(id=task_pk).exists())

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('tasks'))
        self.assertEqual(response.status_code, 302)
