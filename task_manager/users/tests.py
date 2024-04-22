from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import Client, TestCase
from django.urls import reverse_lazy


class UserTestCase(TestCase):
    User = get_user_model()

    @classmethod
    def setUpTestData(cls):
        call_command('loaddata', 'testdata.json')

    def setUp(self):
        self.client = Client()

    def test_registration(self):
        self.assertFalse(self.User.objects.filter(username='test2').exists())
        response = self.client.post(reverse_lazy('create_user'),
                                    {
                                        'username': 'test2',
                                        'email': 'test2@mail.ru',
                                        'password1': 'test2',
                                        'password2': 'test2'
                                    })
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertTrue(self.User.objects.filter(username='test2').exists())
