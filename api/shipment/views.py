from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .models import ShipmentRetailer, ShipmentItem
from .serializers import ShipmentItemSerializer, ShipmentRetailerSerializer
from django.conf import settings
import requests
import json
from .tasks import fetchShipment,immediate_load




def getShipment():
    shipments = ShipmentRetailer.objects.all()
    shipmentArr = []           
    if len(shipments) > 0:                
        for shipment in shipments:
            shipmentObj = {}
            shipmentObj['id'] = shipment.id
            shipmentObj['shipment_id'] = shipment.shipment_id
            shipmentObj['shipment_date'] = shipment.shipment_date
            shipmentObj['transport_id'] = shipment.transport_id
            shipmentArr.append(shipmentObj)

    return shipmentArr
    
class ShipmentView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk is None:
            shipment = ShipmentRetailer.objects.all()
            if len(shipment) > 0:
                serializer = ShipmentRetailerSerializer(shipment, many=True)
                return Response({"error": False, "status_code": 200,"data": serializer.data,"msg": "Data Fetched Successfully"})

            else:
                token = request.session.get('token')
                if(token is not None):
                    try:
                        kwargs['pageNo'] = "1"
                        kwargs['token'] = request.session.get('token')
                        kwargs['client_key'] = request.session.get('client_key')
                        kwargs['secret_key'] = request.session.get('secret_key')
                        shipment_key = settings.SHIPMENT_ARR
                        if len(shipment_key) > 0:
                            for key in shipment_key:
                                kwargs['fulfilment_method'] = key
                                immediate_load.delay(*args, **kwargs)
                        shipmentArr = getShipment()
                        return Response(
                            {"error": False, "status_code": 200,"data": shipmentArr, "msg": "Data Fetched Successfully",})
                    except Exception as e:
                        print('e',e)
                        return Response(
                        {"error": True, "status_code": 400, "msg": "Internal Server Error",})
                else:
                    return Response(
                            {"error": True, "status_code": 400, "msg": "Token Not Found! Generate using Login.",}
                        )
                
            # the many param informs the serializer that it will be serializing more than a single ShipmentRetailer.
        else :
            shipment = ShipmentRetailer.objects.filter(pk=pk)
            serializer = ShipmentRetailerSerializer(shipment, many=True)
            return Response({"error": False, "status_code": 200,"data": serializer.data,"msg": "Data Fetched Successfully"})
            