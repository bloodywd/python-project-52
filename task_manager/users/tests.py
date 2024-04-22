from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse_lazy


class UserTestCase(TestCase):
    USERNAME = 'test1'
    PASSWORD = 'AIOWdBrA'
    User = get_user_model()

    def setUp(self):
        self.client = Client()
        self.test_user = self.User.objects.create(username=self.USERNAME)
        self.test_user.set_password(self.PASSWORD)
        self.test_user.save()

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
        user = self.User.objects.get(id=self.test_user.id)
        user_id = user.id
        response = self.client.login(username=self.USERNAME, password=self.PASSWORD)
        self.assertTrue(response)
        url = reverse_lazy('update_user', kwargs={"pk": user_id})
        response = self.client.post(url, {'username':user.username, 'first_name': 'changed_name', 'last_name': user.last_name, 'password1': self.PASSWORD, 'password2': self.PASSWORD})
        self.assertTrue(response.status_code, 302)
        user = self.User.objects.get(id=user_id)
        self.assertTrue(user.first_name, 'changed_name')

    def test_delete_user(self):
        user_id = self.User.objects.get(id=self.test_user.id).id
        response = self.client.login(username=self.USERNAME, password=self.PASSWORD)
        self.assertTrue(response)
        url = reverse_lazy('delete_user', kwargs={"pk": user_id})
        response = self.client.post(url)
        self.assertTrue(response.status_code, 302)
        self.assertFalse(self.User.objects.filter(id=user_id).exists())

    def test_action_to_other_user(self):
        test_user2 = self.User.objects.create(username='test2')
        test_user2_id = test_user2.id
        test_user2.set_password(self.PASSWORD)
        test_user2.save()
        response = self.client.login(username=self.USERNAME, password=self.PASSWORD)
        self.assertTrue(response)
        url = reverse_lazy('update_user', kwargs={"pk": test_user2_id})
        response = self.client.post(url, {'username':test_user2.username,
                                          'first_name': 'changed_name',
                                          'last_name': test_user2.last_name,
                                          'password1': self.PASSWORD,
                                          'password2': self.PASSWORD})
        self.assertFalse(self.User.objects.get(id=test_user2_id).first_name == 'changed_name')
        url = reverse_lazy('delete_user', kwargs={"pk": test_user2_id})
        response = self.client.post(url)
        self.assertTrue(self.User.objects.filter(id=test_user2_id).exists())
