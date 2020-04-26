from django.db import models

# Create your models here.

# Model for the Shipment Retailer
class ShipmentRetailer(models.Model):
    shipment_id = models.IntegerField()
    shipment_date = models.DateTimeField()
    transport_id = models.IntegerField()

    def __str__(self):
        return "#" + str(self.pk)


# Model for the Shipment Item
class ShipmentItem(models.Model):
    shipment = models.ForeignKey(ShipmentRetailer, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=30)
    order_item_id = models.CharField(max_length=30)
    title = models.TextField(blank=True, null=True)
    quantity = models.CharField(null=True,blank=True,max_length=30)
    offer_price = models.CharField(null=True,blank=True,max_length=30)
    fulfilment_method = models.CharField(max_length=3)

    def __str__(self):
        return "#" + str(self.pk)
