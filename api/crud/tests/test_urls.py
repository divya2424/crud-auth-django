from django.test import SimpleTestCase
from django.urls import reverse, resolve
from crud.views import CredentialView

class CredentialTestUrls(SimpleTestCase):

    def test_credential_url_is_resolved(self):
        url = reverse('crud:crud')
        self.assertEquals(resolve(url).func.view_class ,CredentialView)

    def test_credential_url_with_param_is_resolved(self):
        url = reverse('crud:crud' ,kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class ,CredentialView)



