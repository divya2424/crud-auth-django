from django.urls import path
from .views import celery_view,login
from django.views.generic import TemplateView


app_name = "authenticate"


urlpatterns = [
    path('login/',login, name='login'),
    # path('celerytask/', celery_view),   
]
