# from django.test import TestCase
# from django.contrib.auth.models import User
#
#
# class AnimalTestCase(TestCase):
#     def setUp(self):
#         User.objects.create(name="lion", sound="roar")
#         User.objects.create(name="cat", sound="meow")
#
#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         lion = User.objects.get(name="lion")
#         cat = User.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')
#
