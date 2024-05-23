from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse_lazy


class UserTestCase(TestCase):
    User = get_user_model()

    def setUp(self):
        self.client = Client()
        self.test_user = self.User.objects.create(username='test', password='test1234')

    def dropDown(self):
        self.User.objects.clear()

    def test_registration(self):
        self.assertFalse(self.User.objects.filter(username='test3').exists())
        response = self.client.post(reverse_lazy('create_user'),
                                    {
                                        'username': 'test3',
                                        'first_name': 'test',
                                        'last_name': 'test',
                                        'password1': 'AIOWdBrA',
                                        'password2': 'AIOWdBrA'
                                    })
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertTrue(self.User.objects.filter(username='test3').exists())

    def test_update_user(self):
        user_id = self.test_user.id
        self.client.force_login(user=self.test_user)
        url = reverse_lazy('update_user', kwargs={"pk": user_id})
        response = self.client.post(url, {'username': self.test_user.username,
                                          'first_name': 'changed_name',
                                          'last_name': 'changed_name',
                                          'password1': 'AXQoKa31',
                                          'password2': 'AXQoKa31'})
        self.assertEqual(response.status_code, 302)
        user = self.User.objects.get(id=user_id)
        self.assertEqual(user.first_name, 'changed_name')

    def test_delete_user(self):
        user = self.User.objects.get(id=self.test_user.id)
        user_id = user.id
        self.client.force_login(user=self.test_user)
        url = reverse_lazy('delete_user', kwargs={"pk": user_id})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.User.objects.filter(id=user_id).exists())

    def test_action_to_other_user(self):
        test_user2 = self.User.objects.create(username='test2')
        test_user2_id = test_user2.id
        self.client.force_login(user=self.test_user)
        url = reverse_lazy('update_user', kwargs={"pk": test_user2_id})
        self.client.post(url, {'username':test_user2.username,
                                          'first_name': 'changed_name',
                                          'last_name': test_user2.last_name,
                                          'password1': 'AXQoKa31',
                                          'password2': 'AXQoKa31'})
        self.assertNotEqual(self.User.objects.get(id=test_user2_id).first_name, 'changed_name')
        url = reverse_lazy('delete_user', kwargs={"pk": test_user2_id})
        self.client.post(url)
        self.assertTrue(self.User.objects.filter(id=test_user2_id).exists())
