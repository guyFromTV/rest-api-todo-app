from rest_framework.test import APITestCase

from authentication.models import User

# there was a problem while running tests, so I added these 2 lines (gpt suggested)
import sys
sys.path.insert(0, '/home/admin123/Projects/DRF ToDo list App/authentication')


class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('emin', 'howareyou@gmail.com', 'somepassword6')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'howareyou@gmail.com')
        self.assertFalse(user.is_staff)

    def test_creates_super_user(self):
        user = User.objects.create_user('emin', 'howareyou@gmail.com', 'somepassword6')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'howareyou@gmail.com')
        self.assertTrue(user.is_staff)

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user,username='', email='howareyou@gmail.com', password='somepassword6')

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user,username='john', email='', password='somepassword6')