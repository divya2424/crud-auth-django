from django.test import TestCase
from crud.models import Credential


'''
Test Cases For CRUD Models
'''

class CredentialTestModels(TestCase):
    def test_verbose_name_plural(self):
        self.assertEqual(str(Credential._meta.verbose_name_plural), "credentials")

