
from django.test import TestCase
from shipment.models import ShipmentItem,ShipmentRetailer

'''
Test Cases For Shipment Models
'''
class CredentialTestModels(TestCase):
    def test_verbose_name_plural_retailer(self):
        self.assertEqual(str(ShipmentRetailer._meta.verbose_name_plural), "shipment retailers")


    def test_verbose_name_plural_item(self):
        self.assertEqual(str(ShipmentItem._meta.verbose_name_plural), "shipment items")
