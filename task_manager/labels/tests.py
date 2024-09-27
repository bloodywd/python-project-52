from django.test import Client, TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from task_manager.labels.models import Label


class UserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        user = get_user_model().objects.create_user("test")
        self.client.force_login(user)

    def dropDown(self):
        Label.objects.clear()

    def test_create_status(self):
        self.client.post(reverse_lazy('create_label'),
                         {'name': 'TEST', })
        self.assertTrue(Label.objects.filter(name='TEST').exists())

    def test_update_status(self):
        label = Label.objects.create(name='UPDATE')
        label_pk = label.id
        url = reverse_lazy('update_label', kwargs={"pk": label_pk})
        response = self.client.post(url, {'name': 'UPDATETEST'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Label.objects.get(id=label_pk).name, 'UPDATETEST')

    def test_delete_status(self):
        label = Label.objects.create(name='UPDATE')
        label_pk = label.id
        url = reverse_lazy('delete_label', kwargs={"pk": label_pk})
        self.client.post(url)
        self.assertFalse(Label.objects.filter(id=label_pk).exists())

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('labels'))
        self.assertEqual(response.status_code, 302)
