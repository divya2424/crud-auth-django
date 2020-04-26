from rest_framework import serializers

from .models import ShipmentItem, ShipmentRetailer


class ShipmentRetailerSerializer(serializers.Serializer):
    class Meta:
        model = ShipmentRetailer
        fields = ("fulfilment_method", "shipment_id", "shipment_date", "transport_id")


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
        )
