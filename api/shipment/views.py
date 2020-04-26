from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .models import ShipmentRetailer, ShipmentItem
from .serializers import ShipmentItemSerializer, ShipmentRetailerSerializer


class ShipmentView(APIView):
    def get(self, request):
        shipment = ShipmentRetailer.objects.all()
        # the many param informs the serializer that it will be serializing more than a single shipments.
        serializer = ShipmentRetailerSerializer(shipment, many=True)
        return Response({"shipment": serializer.data})

    def post(self, request):
        # Create an shipment from the above data
        serializer = ShipmentItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
        return Response(
            {"success": "Credential '{}' created successfully".format(cred_saved)}
        )
