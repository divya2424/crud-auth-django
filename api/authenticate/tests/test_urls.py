from django.test import SimpleTestCase
from django.urls import reverse, resolve
from authenticate.views import login

class TestUrls(SimpleTestCase):

    def test_authetication_url_is_resolved(self):
        url = reverse('authenticate:login')
        self.assertEquals(resolve(url).func ,login)

