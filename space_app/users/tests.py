from django.urls import reverse_lazy
from django.test import TestCase
from .models import User


class TestCreateUser(TestCase):

    def test_open_create_user(self):
        response = self.client.get(reverse_lazy('create_user'))
        self.assertEqual(response.status_code, 200)

    def test_redirect_user(self):
        user = User.objects.create(first_name='Valentina',
                                   last_name="Tereshkova",
                                   email="tereshkova@mail.ru",
                                   username="tereshkova")
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, "tereshkova")
        self.assertEqual(User.objects.all().count(), 1)
