from rest_framework import serializers

from .models import ShipmentItem, ShipmentRetailer


class ShipmentRetailerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    shipment_id = serializers.IntegerField()
    shipment_date = serializers.DateTimeField()
    transport_id = serializers.IntegerField()



class ShipmentItemSerializer(serializers.Serializer):
    ordered_meals = ShipmentRetailerSerializer(many=True)

    class Meta:
        shipment_id = ShipmentItem
        fields = (
            "id",
            "shipment_id",
            "order_id",
            "order_item_id",
            "title",
            "quantity",
            "offer_price",
            "fulfilment_method"
        )
