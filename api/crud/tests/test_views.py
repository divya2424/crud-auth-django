from django.test import TestCase,Client
from django.urls import reverse
from crud.models import Credential


class CrudTestViews(TestCase):
    def test_project_list_GET(self):
        client = Client()
        response =client.get(reverse('crud:crud'))
        self.assertEquals(response.status_code,200)
        # self.assertTemplateUsed(response,'')

