from django.urls import path
from .views import ShipmentView

app_name = "shipment"


urlpatterns = [
    path("list/", ShipmentView.as_view(), name="list"),
    path("list/<int:pk>/", ShipmentView.as_view(), name="list"),
]
