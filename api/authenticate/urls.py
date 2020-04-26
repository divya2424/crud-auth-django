from django.urls import path
from .views import FetchToken

app_name = "authenticate"


urlpatterns = [
    path("token/", FetchToken.as_view(), name="token"),
]
