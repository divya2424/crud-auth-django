from rest_framework import serializers

from .models import ShipmentItem, ShipmentRetailer


class ShipmentRetailerSerializer(serializers.Serializer):
    class Meta:
        model = ShipmentRetailer
        fields = ("shipment_id", "shipment_date", "transport_id")

    # def create(self, validated_data):
    #     answer, created = ShipmentRetailer.objects.update_or_create(
    #     question=validated_data.get('question', None),
    #     defaults={'answer': validated_data.get('answer', None)})
    #     return answer
    def create(self, validated_data):
            return ShipmentRetailer.objects.create(**validated_data)


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
