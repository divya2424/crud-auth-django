from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .models import ShipmentRetailer, ShipmentItem
from .serializers import ShipmentItemSerializer, ShipmentRetailerSerializer
from django.conf import settings
import requests
import json

headers = {
    "Content-Type": settings.CONTENT_TYPE,
    "Accept": settings.ACCEPT[1],
    "Authorization": "Bearer eyJraWQiOiJyc2EyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI2OWJkODNmMS0xMTcyLTRiMDItODIxYS1iNWEyYWY1YTMyZGEiLCJhenAiOiI2OWJkODNmMS0xMTcyLTRiMDItODIxYS1iNWEyYWY1YTMyZGEiLCJjbGllbnRuYW1lIjoiZGV2ZWxvcGVyLWhpcmUiLCJpc3MiOiJodHRwczpcL1wvbG9naW4uYm9sLmNvbSIsInNjb3BlcyI6IlJFVEFJTEVSIiwiZXhwIjoxNTg3OTMwMDc2LCJpYXQiOjE1ODc5Mjk3NzYsImFpZCI6IkNMTlRDOmJlMmI3MDE2LTczNDYtYzM2ZS1kMTM4LTc3NzA4MTczZjdiYyBTTFI6MTM2Mzg1OCIsImp0aSI6IjdlNzQyMGZmLTNlZjktNGZhMi1iYzc0LWU2NzZiZWUwNjEzZCJ9.EYVkfJxlLsftczm2RqDSQ2mnall-G_7ARqmjHqwrhEaAjJQtFc6YuWQJw82tLrerNlTWVsag5VdYT7RfvrX2oZWNYM1t7GgWIcohZcVeqGRO_QxyZmXvRaa_Jgdq3FdrDB1RdBQLHwSgcpLt9excee_ZF5uYhN4uZOzzNQzx0LU2lu0XNRnUfl9TN2KLhLTG24BgOG_IQABpUYtcmXC_H9h_U8U1ZqIXhcEFq2_emSifjndg48hCYBqC10xrmjy-FU_hRNnU1sQR4gsiM8aQOoemYRac5Kcdjl6tHT4octbXDeWt80BpCo8lZruAttaU52EIFaZLsFV7bTdCBC2nsw"
}


def fetchShipment(fulfilment_method,pageNo):
    URL = (settings.SHIPMENT_URL + "fulfilment-method="+fulfilment_method+"&page="+ pageNo)
    response = requests.request("POST", URL, data=json.dumps({}), headers=headers,)
    return response


def fulfilmentType(method):
    i = 1
    response = fetchShipment(method,i)
    if response.status_code == 200:
        response = json.loads(response.text)
        arr = []
        if not len(response) == 0:
            i = i + 1
            res = fetchShipment(method,i)

            return {
                "status_code": 201,
                "msg": "No Records Found"
            }
        else:
            return{
                "status_code": 200,
                "data" : arr,
            }
    else:
        raise Exception("Something went wrong")

# def CreateOrUpda
class ShipmentView(APIView):
    def get(self, request):
        try:
            shipments = ShipmentRetailer.objects.get.all()
            shipmentArr = []
            if len(shipments > 0):
                shipmentObj = {}
                for shipment in shipments:
                    shipmentObj['fulfilment_method'] = shipment.fulfilment_method
                    shipmentObj['shipment_id'] = shipment.shipment_id
                    shipmentObj['shipment_date'] = shipment.shipment_date
                    shipmentObj['transport_id'] = shipment.transport_id
                    shipmentArr.append(shipmentObj)
                return Response(
                {"error": False, "status_code": 200,"data": shipmentArr, "msg": "Data Fetched Successfully",})
            else:
                type_fbr = fulfilmentType('FBR')
                type_fbb = fulfilmentType('FBB')

        except Exception as e:
            return Response(
                {"error": True, "status_code": 400, "msg": "Internal Server Error",}
            )



        # shipment = ShipmentRetailer.objects.all()
        # # the many param informs the serializer that it will be serializing more than a single shipments.
        # serializer = ShipmentRetailerSerializer(shipment, many=True)
        # return Response({"shipment": serializer.data})

