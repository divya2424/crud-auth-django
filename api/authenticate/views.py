from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from crud.models import Credential
from .serializers import TokenSerializer
from django.conf import settings
import requests
import json
from django.shortcuts import HttpResponse
from .tasks import task_example



headers = {
    "Content-Type": settings.CONTENT_TYPE,
    "Accept": settings.ACCEPT[0],
}


class FetchToken(APIView):
    def post(self, request):
        # Create an shipment from the above data
        try:
            serializer = TokenSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                client_key = request.data["client_key"]
                secret_key = request.data["secret_key"]
                try:
                    check_credential = Credential.objects.get(
                        client_key=client_key, secret_key=secret_key
                    )
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
                        return Response(
                            {
                                "error": False,
                                "status_code": 200,
                                "msg": "Credentials Not Found",
                                "access_token": response["access_token"],
                                "token_type": response["token_type"],
                                "expires_in": response["expires_in"],
                                "scope": response["scope"],
                            }
                        )

                    else:
                        return Response(
                            {
                                "error": True,
                                "status_code": 400,
                                "msg": "Bad Credentials",
                            }
                        )

                except Credential.DoesNotExist:
                    return Response(
                        {
                            "error": True,
                            "status_code": 400,
                            "msg": "Credentials Not Found",
                        }
                    )

            else:
                return Response(
                    {"error": True, "status_code": 400, "msg": "Invalid Parameters",}
                )

        except Exception as e:
            print("e", e)
            return Response(
                {"error": True, "status_code": 400, "msg": "Internal Server Error",}
            )



def celery_view(request):
    print('hello')
    task_example()
    # for counter in range(2):
    #     print('counter',counter)
    #     task_example.delay(counter)
    return HttpResponse("FINISH PAGE LOAD")