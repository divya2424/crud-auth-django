from django.urls import path
from .views import ShipmentView,ShipmentListing

app_name = "shipment"

'''
URL for shipment
'''
urlpatterns = [
    path("list/", ShipmentView.as_view(), name="list"),
    path("list/<int:pk>/", ShipmentListing.as_view(),name="list"),
]
