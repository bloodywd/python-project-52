from django.test import Client, TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from task_manager.statuses.models import Status


class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        user = get_user_model().objects.create_user("test")
        self.client.force_login(user)

    def dropDown(self):
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
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Status.objects.get(id=status_pk).name, 'UPDATETEST')

    def test_delete_status(self):
        status = Status.objects.create(name='UPDATE')
        status_pk = status.id
        url = reverse_lazy('delete_status', kwargs={"pk": status_pk})
        self.client.post(url)
        self.assertFalse(Status.objects.filter(id=status_pk).exists())

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('statuses'))
        self.assertEqual(response.status_code, 302)
