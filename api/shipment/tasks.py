from celery import shared_task,task
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
import time
# from shipment.views import fetchShipment
from crud.models import Credential
from shipment.models import ShipmentRetailer, ShipmentItem
import requests
import json
from django.conf import settings




headers = {
    "Content-Type": settings.CONTENT_TYPE,
    "Accept": settings.ACCEPT[0],
}


logger = get_task_logger(__name__)



def getToken(func):
    def get_token(*args, **kwargs):
        print(func.__name__ + " was called")
        if kwargs['token'] is not None:
            try:
                client_id = kwargs['client_key']
                secret_key = kwargs['secret_key']
                print('client_id',client_id)
                print('session',secret_key)
                credential = Credential.objects.get(
                            client_key=client_id, 
                            secret_key=secret_key)
                URL = (settings.TOKEN_URL
                            + "&client_id="
                            + client_id
                            + "&client_secret="
                            + secret_key
                        )
                response = requests.request(
                            "POST", URL, data=json.dumps({}), headers=headers)
                if response.status_code == 200:
                    response = json.loads(response.text)
                    print('response',response)
                    kwargs['token'] = response["token_type"] + " " + response["access_token"]
                    kwargs['status_code'] = 200
                else:
                    kwargs['status_code'] = response.status_code
            except :
                TestFailed("Credential Doesn't exist in the system")
        else:
            TestFailed("Token Not Found! Try Login With Your credentials")
        return func(*args, **kwargs)

    return get_token


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
                            shipmentItem = ShipmentItem.objects.get(shipment=shipment)
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
            return "Data added"
        else:
            return "No Data Founf"
    else:
        return "Something went wrong"

    




@periodic_task(run_every=(crontab(minute=0,hour='*/5')),name="load_shipment")
def load_shipment(*args, **kwargs):
    credential =  Credential.objects.all()[:1].get()
    kwargs['client_key'] = credential.client_key
    kwargs['secret_key'] = credential.secret_key
    URL = (settings.TOKEN_URL
                            + "&client_id="
                            + kwargs['client_key']
                            + "&client_secret="
                            + kwargs['secret_key']
                        )
    response = requests.request(
                            "POST", URL, data=json.dumps({}), headers=headers)
    if response.status_code == 200:
        response = json.loads(response.text)
        kwargs['token'] = response["token_type"] + " " + response["access_token"]
        logger.info("Task started",'eifiueshfieu')
        shipmentArr = settings.SHIPMENT_ARR
        if len(shipmentArr) > 0:
            for key in shipmentArr:
                kwargs['pageNo'] = "1"
                kwargs['fulfilment_method'] = key
                fetchShipment(*args, **kwargs)
        logger.info('Task Ended')
        return '{}No occured Done!'

    else:
        return '{}Error occured Done!'



@shared_task(name="immediate_loads", max_retries=9)
def immediate_load(*args,**kwargs):
    shipment = ShipmentRetailer.objects.all()
    if len(shipment) > 0:
        return;
    else:
        load_shipment(*args, **kwargs)

immediate_load.apply_async(expires=60,queue='priority.high')