from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

#from django.contrib.auth.forms import UserCreationForm
#from accounts.forms import UserRegistrationForm
#from django.contrib.auth import get_user_model

class AccountCreationTest(TestCase):
    def test_signup_page_exist(self):
        response = self.client.get(reverse('signup_page'))

        self.assertEqual(response.status_code,HTTPStatus.OK)
        self.assertTemplateUsed('accounts/register.html')