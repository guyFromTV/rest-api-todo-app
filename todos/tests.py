from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from todos.models import Todo


class TodoAPITestCase(APITestCase):

    def create_todo(self):
        sample_todo = {
            'title': 'Sample todo',
            'description': 'Sample description'
        }
        response = self.client.post(reverse('todos'), sample_todo)

    def authenticate(self):
        self.client.post(reverse('register'), {
            'username': 'test_username',
            'email': 'test@gmail.com',
            'password': 'test_password'
        })

        response = self.client.post(reverse('login'), {
            'email': 'test@gmail.com',
            'password': 'test_password'
        })

        token = response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')


class TestListCreateTodo(TodoAPITestCase):

    def test_should_not_create_todo_with_no_auth(self):
        response = self.create_todo()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_should_create_todo(self):
        self.authenticate()
        response = self.create_todo()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestTodoDetailAPIView(TodoAPITestCase):

    def test_retrieves_one_todo(self):
        self.authenticate()
        response = self.create_todo()

        res = self.client.get(reverse('todo', kwargs={'id': response.data['id']}))

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_updates_one_todo(self):
        self.authenticate()
        response = self.create_todo()

        res = self.client.patch(reverse('todo', kwargs={'id': response.data['id']}), {
            'title': 'New title',
            'is_completed': True
        })

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_deletes_one_todo(self):
        self.authenticate()
        response = self.create_todo()

        res = self.client.delete(reverse('todo', kwargs={'id': response.data['id']}))

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        
