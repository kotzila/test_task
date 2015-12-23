from django.test import TestCase
from django.contrib.auth.models import User
from domains.models import Domain
from rest_framework.test import APIClient
from rest_framework import status


class NewDomainTest(TestCase):
    def setUp(self):
        self.custom_user = User.objects.create(username='admin', password='12345qwert')
        self.admin3 = User.objects.create(username='admin3', password='12345qwert')

    def test_anonymous(self):
        client = APIClient()
        response = client.post('/domains/', {'url': 'https:/google.com/'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_custom_user(self):
        client = APIClient()
        client.force_authenticate(user=self.custom_user)
        response = client.post('/domains/', {'url': 'https:/google.com/'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin3_user(self):
        client = APIClient()
        client.force_authenticate(user=self.admin3)

        # check if can add url starts with http
        response = client.post('/domains/', {'url': 'http://example.com/'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'url': [u'Enter url that starts with https']})

        # check if can add not existing url
        response = client.post('/domains/', {'url': 'https://exampletest.com/'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'url': [u'No answer from given url']})

        # check if can create an object
        response = client.post('/domains/', {'url': 'https://google.com/'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Domain.objects.all().count(), 1)