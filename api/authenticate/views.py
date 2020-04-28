from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from crud.models import Credential
from .serializers import TokenSerializer
from django.conf import settings
import requests
import json
from django.shortcuts import HttpResponse
from .tasks import celery_task


headers = {
    "Content-Type": settings.CONTENT_TYPE,
    "Accept": settings.ACCEPT[0],
}


def login(request):
    if request.method == "POST":
        client_key = request.POST.get('client_key')
        secret_key = request.POST.get('secret_key')
        try:
            credential = Credential.objects.get(client_key=client_key, secret_key=secret_key)
            URL = (
                settings.TOKEN_URL
                + "&client_id="
                + client_key
                + "&client_secret="
                + secret_key
            )
            response = requests.request(
                "POST", URL, data=json.dumps({}), headers=headers,
            )
            if response.status_code == 200:
                response = json.loads(response.text)
                request.session['client_key'] = client_key
                request.session['secret_key'] = secret_key
                request.session['token'] =response["token_type"] + " " + response["access_token"]
                obj = {
                        "error": False,
                        "status_code": 200,
                        "msg": "Credentials Found! Token Saved Sucessfully",
                        "access_token": response["access_token"],
                        "token_type": response["token_type"],
                        "expires_in": response["expires_in"],
                        "scope": response["scope"],
                    }
            else:
                obj = {
                        "error": True,
                        "status_code": 400,
                        "access_token": "",
                        "msg": "Bad Credentials",
                    }
            return render(request, 'authenticate/login.html',obj)
                
        except Credential.DoesNotExist:
            obj = {
                            "error": True,
                            "access_token":"",
                            "status_code": 400,
                            "msg": "Credentials Not Found. Please Contact Adminstrator.",
                }
            return render(request, 'authenticate/login.html',obj)
                    
        except Exception as e:
            obj = {
                            "error": True,
                            "status_code": 500,
                            "msg": "Internal Server Error",
                }
            return render(request, 'authenticate/login.html',obj)
    else:
        obj = {
                "error": True,
            }
        return render(request, 'authenticate/login.html',obj)



def celery_view(request,*args, **kwargs):
    print('hello')
    # task_example.run()
    # # for counter in range(2):
    # #     print('counter',counter)
    # #     celery_task.delay(counter)
    # return HttpResponse("FINISH PAGE LOAD")


# def logged(func):
#     def with_logging(request,*args, **kwargs):
#         print('>>>>>>>>>',request.session)
#         request.session['zub'] = 123
#         print(request.session.get('zub'),'???')
#         print(func.__name__ + " was called")
#         # args('first')
#         # kwargs.append({'dude':'cool'})
#         kwargs['dude'] = 'cool'
#         return func(*args, **kwargs)
#     return with_logging


def hellocheck(*args, **kwargs):
   print('mathhhhhhhhhhhhhhhhhhh',kwargs,args)
   return HttpResponse("FINISH PAGE LOAD")


class TestFailed(Exception):
    def __init__(self, m):
        self.message = m
    def __str__(self):
        return self.message










