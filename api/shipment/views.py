from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .models import ShipmentRetailer, ShipmentItem
from .serializers import ShipmentItemSerializer, ShipmentRetailerSerializer
from django.conf import settings
import requests
import json
from authenticate.views import getToken,TestFailed






@getToken
def fetchShipment(*args, **kwargs):
    URL = (settings.SHIPMENT_URL + "?fulfilment-method="+kwargs['fulfilment_method']+"&page="+ kwargs['pageNo'])
    headers = {
    "Accept": settings.ACCEPT[1],
    "Authorization": kwargs['token']
    }
    print('URL',URL)
    response = requests.request("GET", URL, headers=headers,)
    print('response',response.json())
    if response.status_code == 200:
        response = json.loads(response.text)
        i = 1
        if not len(response) == 0:
            for ship in response['shipments']:
                shipment_id = ship['shipmentId']
                shipment_date = ship['shipmentDate']
                transport_id = ship['transport']['transportId']
                try:
                    print('in shipmemt')
                    shipment = ShipmentRetailer.objects.get(shipment_id=shipment_id)
                    print('shio',shipment.id)
                    for item in ship['shipmentItems']:
                        shipment = shipment
                        order_id = item['orderId']
                        order_item_id = item['orderItemId']
                        try:
                            print('in try')
                            shipmentItem = ShipmentItem.objects.get(pk=shipment.id)
                            print('print',shipmentItem)
                        except ShipmentItem.DoesNotExist:
                            print('in except')
                            shipmentItem = ShipmentItem.objects.create(shipment=shipment,order_id=order_id,order_item_id=order_item_id,fulfilment_method=kwargs['fulfilment_method'])   
                        
                except ShipmentRetailer.DoesNotExist:
                    shipment = ShipmentRetailer.objects.create(shipment_id=shipment_id,shipment_date=shipment_date,transport_id=transport_id)                
                    for item in ship['shipmentItems']:
                        shipment = shipment
                        order_id = item['orderId']
                        order_item_id = item['orderItemId']
                        shipmentItem = ShipmentItem.objects.create(shipment=shipment,order_id=order_id,order_item_id=order_item_id,fulfilment_method=kwargs['fulfilment_method'])
            i = i + 1
            kwargs['pageNo'] = str(i)
            res = fetchShipment(*args, **kwargs)
            return {
                "status_code": 200,
                "data" : [],
            }
        else:
            return{
                "status_code": 201,
                "data" : {},
            }
    else:
        raise Exception("Something went wrong")

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
    

# FIFTEEN_MINUTES = 900

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
                



