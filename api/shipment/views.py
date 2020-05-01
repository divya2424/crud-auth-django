from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework import generics, pagination
from .models import ShipmentRetailer, ShipmentItem
from .serializers import ShipmentItemSerializer, ShipmentRetailerSerializer
from django.conf import settings
import requests
import json
from .tasks import fetchShipment,immediate_load
from rest_framework import status



# from django.core.paginator import Paginator
 # paginator = Paginator(shipment, 3)
# page = request.GET.get('page')
# posts = paginator.get_page(page)
# print('post',posts.paginator.num_pages)
# arr = []

# for post in posts:
#     obj = {}
#     print('post111',post)
#     obj['id'] = post.id
#     arr.append(obj)
                    



'''
PageNumberPagination help in getting the view to be rendered according to the page size defined 
and also the param in which the value needs to be passed with a max page size
'''
class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


'''
rest-framework have LISTAPIVIEW with the help of which we can display the pagination numbers on the screen
'''
class ShipmentView(generics.ListAPIView):
    queryset = ShipmentRetailer.objects.all()
    serializer_class = ShipmentRetailerSerializer
    pagination_class = StandardResultsSetPagination


class ShipmentListing(APIView):
    def get(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            shipment = ShipmentRetailer.objects.get(pk=pk)    
            serializer = ShipmentRetailerSerializer(shipment)
            return Response({"shipment": serializer.data})
        except ShipmentRetailer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
