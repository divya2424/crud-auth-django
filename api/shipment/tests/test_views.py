'''
Test Cases For Shipment Views
'''

from django.test import TestCase,Client
from django.urls import reverse
from shipment.models import ShipmentRetailer
import json
from rest_framework import status
from shipment.serializers import ShipmentRetailerSerializer
import datetime

# initialize the APIClient app
client = Client()

class GetSingleShipmentTest(TestCase):
    """ Test module for GET single shipment API """

    def setUp(self):
        self.first = ShipmentRetailer.objects.create(
            shipment_id=1234, 
            transport_id=2749,
            shipment_date=datetime.datetime.now()
            )

    def test_get_valid_single_shipment(self):
        response = client.get(
            reverse('shipment:list', kwargs={'pk': self.first.pk}))
        shipment = ShipmentRetailer.objects.get(pk=self.first.pk)
        serializer = ShipmentRetailerSerializer(shipment)
        data = {'shipment': serializer.data}
        self.assertEqual(response.data, data)

    def test_get_invalid_single_shipment(self):
        response = client.get(
            reverse('shipment:list', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)