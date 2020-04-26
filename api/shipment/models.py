from django.db import models

# Create your models here.

# Model for the Shipment Retailer
class ShipmentRetailer(models.Model):
    fulfilment_method = models.CharField(max_length=3)
    shipment_id = models.IntegerField()
    shipment_date = models.DateField()
    transport_id = models.IntegerField()

    def __str__(self):
        return "#" + str(self.pk)


# Model for the Shipment Item
class ShipmentItem(models.Model):
    shipment = models.ForeignKey(ShipmentRetailer, on_delete=models.CASCADE)
    order_id = models.IntegerField()
    order_item_id = models.IntegerField()
    title = models.TextField(blank=True, null=True)
    quantity = models.IntegerField()
    offer_price = models.FloatField()

    def __str__(self):
        return "#" + str(self.pk)
