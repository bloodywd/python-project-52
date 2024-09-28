from django.test import Client, TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from task_manager.labels.models import Label


class LabelTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(username="test",
                                                         password="test1234")
        self.client.force_login(self.user)

    def test_create_label(self):
        response = self.client.post(reverse_lazy('create_label'),
                                    {'name': 'TEST'})
        self.assertRedirects(response, reverse_lazy('labels'))
        self.assertTrue(Label.objects.filter(name='TEST').exists())

    def test_update_label(self):
        label = Label.objects.create(name='UPDATE')
        label_pk = label.id
        url = reverse_lazy('update_label', kwargs={"pk": label_pk})
        response = self.client.post(url, {'name': 'UPDATETEST'})
        self.assertRedirects(response, reverse_lazy('labels'))
        self.assertEqual(Label.objects.get(id=label_pk).name, 'UPDATETEST')

    def test_delete_label(self):
        label = Label.objects.create(name='DELETE_ME')
        label_pk = label.id
        url = reverse_lazy('delete_label', kwargs={"pk": label_pk})
        response = self.client.post(url)
        self.assertRedirects(response, reverse_lazy('labels'))
        self.assertFalse(Label.objects.filter(id=label_pk).exists())

    def test_login_required(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('labels'))
        self.assertEqual(response.status_code, 302)
