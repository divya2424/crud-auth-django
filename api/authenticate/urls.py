from django.urls import path
from .views import celery_view,hellocheck,login
from django.views.generic import TemplateView


app_name = "authenticate"


urlpatterns = [
    path('celerytask/', celery_view),
    path('check/',hellocheck),
    path('login/',login, name='login'),
]
