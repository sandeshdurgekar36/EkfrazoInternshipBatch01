from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.core import mail

# Create your tests here.
class LoginTests(APITestCase):
    def setUp(self):
        # User who is verified on the site
        self.user_verified_email = 'user_verified@mail.com'
        self.user_verified_pw = 'user_verified'
        self.user_verified = get_user_model().objects.create_user(self.user_verified_email, self.user_verified_pw)
        self.user_verified.is_verified = True
        self.user_verified.save()

        # User who is not verified yet on the site
        self.user_not_verified_email = 'user_not_verified@mail.com'
        self.user_not_verified_pw = 'user_not_verified'
        self.user_not_verified = get_user_model().objects.create_user(self.user_not_verified_email, 'pw')
        self.user_not_verified.save()

        # User who is not active on the site
        self.user_not_active_email = 'user_not_active@mail.com'
        self.user_not_active_pw = 'user_not_active'
        self.user_not_active = get_user_model().objects.create_user(self.user_not_active_email, self.user_not_active_pw)
        self.user_not_active.is_verified = True
        self.user_not_active.is_active = False
        self.user_not_active.save()

    def test_login_serializer_errors(self):
        error_dicts = [
            # Email required
            {'payload': {'email': '',
                         'password': self.user_verified_pw},
             'status_code': status.HTTP_400_BAD_REQUEST,
             'error': ('email', 'This field may not be blank.')
             },
            # Password required
            {'payload': {'email': self.user_verified_email,
                         'password': ''},
             'status_code': status.HTTP_400_BAD_REQUEST,
             'error': ('password', 'This field may not be blank.')
             },
            # Invalid email
            {'payload': {'email': 'XXX',
                         'password': self.user_verified_pw},
             'status_code': status.HTTP_400_BAD_REQUEST,
             'error': ('email', 'Enter a valid email address.')
             },
        ]

        url = reverse('authemail-login')
        for error_dict in error_dicts:
            response = self.client.post(url, error_dict['payload'])

            self.assertEqual(response.status_code, error_dict['status_code'])
            self.assertEqual(response.data[error_dict['error'][0]][0],
                             error_dict['error'][1])

    def test_login_invalid_credentials(self):
        # Invalid email address
        url = reverse('authemail-login')
        payload = {
            'email': 'XXX@mail.com',
            'password': self.user_verified_pw,
        }
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'],
                         'Unable to login with provided credentials.')

        # Invalid password for user
        url = reverse('authemail-login')
        payload = {
            'email': self.user_verified_email,
            'password': 'XXX',
        }
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'],
                         'Unable to login with provided credentials.')

    def test_logout_no_auth_token(self):
        url = reverse('authemail-logout')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'],
                         'Authentication credentials were not provided.')

    def test_logout_invalid_auth_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + 'XXX')
        url = reverse('authemail-logout')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Invalid token.')

    def test_login_logout(self):
        # Log in as the user
        url = reverse('authemail-login')
        payload = {
            'email': self.user_verified_email,
            'password': self.user_verified_pw,
        }
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

        token = response.data['token']

        # Log out as the user
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        url = reverse('authemail-logout')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], 'User logged out.')

    def test_login_not_verified_not_active_no_login(self):
        # Not verified user can't login
        url = reverse('authemail-login')
        payload = {
            'email': self.user_not_verified_email,
            'password': self.user_not_verified_pw,
        }
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'],
                         'Unable to login with provided credentials.')

        # Not active user can't login
        url = reverse('authemail-login')
        payload = {
            'email': self.user_not_active_email,
            'password': self.user_not_active_pw,
        }
        response = self.client.post(url, payload)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'],
                         'Unable to login with provided credentials.')


    