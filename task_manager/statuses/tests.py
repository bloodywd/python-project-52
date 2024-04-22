from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse_lazy

from task_manager.statuses.models import Status


class UserTestCase(TestCase):
    USERNAME = 'test1'
    PASSWORD = 'AIOWdBrA'
    User = get_user_model()

    def setUp(self):
        self.client = Client()
        self.test_user = self.User.objects.create(username=self.USERNAME)
        self.test_user.set_password(self.PASSWORD)
        self.test_user.save()
        self.client.login(username=self.USERNAME, password=self.PASSWORD)

    def dropDown(self):
        self.User.objects.clear()
        Status.objects.clear()

    def test_create_status(self):
        self.client.post(reverse_lazy('create_status'),
                                    {
                                        'name': 'TEST',
                                    })
        self.assertTrue(Status.objects.filter(name='TEST').exists())

    def test_update_status(self):
        status = Status.objects.create(name='UPDATE')
        status_pk = status.id
        url = reverse_lazy('update_status', kwargs={"pk": status_pk})
        response = self.client.post(url, {'name': 'UPDATETEST'})
        self.assertTrue(response.status_code, 302)
        self.assertTrue(Status.objects.get(id=status_pk).name, 'UPDATETEST')

    def test_delete_status(self):
        status = Status.objects.create(name='UPDATE')
        status_pk = status.id
        url = reverse_lazy('delete_status', kwargs={"pk": status_pk})
        response = self.client.post(url)
        self.assertFalse(Status.objects.filter(id=status_pk).exists())

    def test_login_required(self):
        response = self.client.post(reverse_lazy('logout'))
        self.assertTrue(response)
        response = self.client.get(reverse_lazy('statuses'))
        self.assertTrue(response.status_code, 403)
