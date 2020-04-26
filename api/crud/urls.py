from django.urls import path
from .views import CredentialView

app_name = "crud"


urlpatterns = [
    # path('crud/', name="crud")
    path('crud/', CredentialView.as_view(),name="crud"),
    path('crud/<int:pk>/',CredentialView.as_view())


]