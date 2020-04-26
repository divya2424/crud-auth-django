from django.db import models

# Create your models here.


class ShipmentRetailer(models.Model):
    fulfilment_method = models.CharField(max_length=3)
    shipment_id = models.IntegerField()
    shipment_date = models.DateField()
    transport_id = models.IntegerField()


class ShipmentItem(models.Model):
    shipment = models.ForeignKey(ShipmentRetailer, on_delete=models.CASCADE)
    order_id = models.IntegerField()
    order_item_id = models.IntegerField()
    title = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    offer_price = models.FloatField()
