'''
Test Cases For Autheticate Views
'''
from django.test import TestCase,Client
from django.urls import reverse

class TestPage(TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        url = reverse('authenticate:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authenticate/login.html')