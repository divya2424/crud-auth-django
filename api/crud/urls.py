from django.urls import path
from .views import CredentialView

app_name = "crud"

'''
crud urls file
'''
urlpatterns = [
    path('crud/', CredentialView.as_view(),name="crud"),
    path('crud/<int:pk>/',CredentialView.as_view(),name="crud")


]