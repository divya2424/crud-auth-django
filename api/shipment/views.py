from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .models import ShipmentRetailer, ShipmentItem
from .serializers import ShipmentItemSerializer, ShipmentRetailerSerializer
from django.conf import settings
import requests
import json




headers = {
    "Accept": settings.ACCEPT[1],
    "Authorization": "Bearer eyJraWQiOiJyc2EyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI2OWJkODNmMS0xMTcyLTRiMDItODIxYS1iNWEyYWY1YTMyZGEiLCJhenAiOiI2OWJkODNmMS0xMTcyLTRiMDItODIxYS1iNWEyYWY1YTMyZGEiLCJjbGllbnRuYW1lIjoiZGV2ZWxvcGVyLWhpcmUiLCJpc3MiOiJodHRwczpcL1wvbG9naW4uYm9sLmNvbSIsInNjb3BlcyI6IlJFVEFJTEVSIiwiZXhwIjoxNTg3OTQxOTkwLCJpYXQiOjE1ODc5NDE2OTAsImFpZCI6IkNMTlRDOmJlMmI3MDE2LTczNDYtYzM2ZS1kMTM4LTc3NzA4MTczZjdiYyBTTFI6MTM2Mzg1OCIsImp0aSI6IjA3ZDY4YmI2LTEwMTEtNDA0Ni1iNmIxLTczYjVjNmMyZjBlMSJ9.Byfw9rjTf-WNEqEOlSBYBPkJz1V6RPIf5K0CpauLM65VpyRn_OoSzZJWhLVyLkNufv1DEI1T4aWkWCxyZA-hKmkGvBvTnDDOQPgytCbdf3XFmCvZXNlZY1Fx4winBGJX6eqMsNh9Vq3U45SVEzHKHBWhmDSPbUBCsTEDrcxfpy24Rp123NPeXJl-3EEm6hILfGio_81lbMkn4OpGpenJE0xj5aYUL9wi3q9-eTPcZ-mxtYeM99BVDahEPJehf8OkDsnZani0sz-sbGiR3LW06BHSTOxRpu1wryLrJA74s1jl_SeAlgoa3GLO-sE2PN2eX_9oH9nwcxfvcJZVcdUDvw"
}

def fetchShipment(fulfilment_method,pageNo):
    URL = (settings.SHIPMENT_URL + "?fulfilment-method="+fulfilment_method+"&page="+ pageNo)
    response = requests.request("GET", URL, headers=headers,)
    if response.status_code == 200:
        response = json.loads(response.text)
        i = 1
        if not len(response) == 0:
            for ship in response['shipments']:
                shipment_id = ship['shipmentId']
                shipment_date = ship['shipmentDate']
                transport_id = ship['transport']['transportId']
                shipment = ShipmentRetailer.objects.create(shipment_id=shipment_id,shipment_date=shipment_date,transport_id=transport_id)
                for item in ship['shipmentItems']:
                    shipment = shipment
                    order_id = item['orderId']
                    order_item_id = item['orderItemId']
                    shipmentItem = ShipmentItem.objects.create(shipment=shipment,order_id=order_id,order_item_id=order_item_id,fulfilment_method=fulfilment_method)
            i = i + 1
            res = fetchShipment(fulfilment_method,str(i))
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
                type_fbr = fetchShipment('FBR',"1")
                type_fbb = fetchShipment('FBB',"1")
                shipmentArr = getShipment()
                return Response(
                {"error": False, "status_code": 200,"data": shipmentArr, "msg": "Data Fetched Successfully",})
        except Exception as e:
            print('e',e)
            return Response(
                {"error": True, "status_code": 400, "msg": "Internal Server Error",}
            )


