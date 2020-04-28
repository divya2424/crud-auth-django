from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .models import ShipmentRetailer, ShipmentItem
from .serializers import ShipmentItemSerializer, ShipmentRetailerSerializer
from django.conf import settings
import requests
import json
from .tasks import fetchShipment




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
    def get(self, request):
        try:
            shipmentArr = getShipment()
            if len(shipmentArr) > 0:                
                return Response(
                {"error": False, "status_code": 200,"data": shipmentArr, "msg": "Data Fetched Successfully",})
            else:
                shipmentArr = []
                return Response(
                {"error": False, "status_code": 200,"data": shipmentArr, "msg": "No Data Found",})
        except Exception as e:
            print('e',e)
            return Response(
                {"error": True, "status_code": 400, "msg": "Internal Server Error",}
            )

    def post(self,request,*args, **kwargs):
        token = request.session.get('token')
        if(token is not None):
            try:
                kwargs['fulfilment_method'] = 'FBR'
                kwargs['pageNo'] = "1"
                kwargs['token'] = request.session.get('token')
                kwargs['client_key'] = request.session.get('client_key')
                kwargs['secret_key'] = request.session.get('secret_key')
                type_fbr = fetchShipment(*args, **kwargs)
                
                kwargs['fulfilment_method'] = 'FBB'
                type_fbb = fetchShipment(*args, **kwargs)
                shipmentArr = getShipment()
                return Response(
                    {"error": False, "status_code": 200,"data": shipmentArr, "msg": "Data Fetched Successfully",})
            except Exception as e:
                print('e',e)
                return Response(
                {"error": True, "status_code": 400, "msg": "Internal Server Error",}
            )
        else:
            return Response(
                    {"error": True, "status_code": 400, "msg": "Token Not Found! Generate using Login.",}
                )
                



