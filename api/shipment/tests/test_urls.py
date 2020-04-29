from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shipment.views import ShipmentListing, ShipmentView

class TestUrls(SimpleTestCase):

    def test_shipment_url_is_resolved(self):
        url = reverse('shipment:list')
        self.assertEquals(resolve(url).func.view_class ,ShipmentView)

    def test_shipment_url_with_param_is_resolved(self):
        url = reverse('shipment:list' ,kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class ,ShipmentListing)