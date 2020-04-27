from django.urls import path
from .views import FetchToken,celery_view

app_name = "authenticate"


urlpatterns = [
    path("token/", FetchToken.as_view(), name="token"),
    path('celerytask/', celery_view),

]
