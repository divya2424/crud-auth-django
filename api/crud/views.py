# from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .serializers import CredentialSerializer

from .models import Credential


class CredentialView(APIView):
    '''
    METHOD : GET
    PARAMS : pk
    '''
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk is None:
            cred = Credential.objects.all()
            serializer = CredentialSerializer(cred, many=True)
            return Response({"cred": serializer.data})
        else:
            try:
               cred = Credential.objects.get(pk=pk)    
               serializer = CredentialSerializer(cred)
               return Response({"cred": serializer.data})
            except Credential.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
                
        # the many param informs the serializer that it will be serializing more than a single credential.
        
        
    '''
    METHOD : POST
    BODY : client_key , secret_key
    '''
    def post(self, request):
        client_key = request.data.get('client_key')
        secret_key = request.data.get('secret_key')

        # Create an credntial from the above data
        serializer = CredentialSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            cred_saved = serializer.save()
            credential,created = cred_saved
            return Response({'created': created},status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    '''
    METHOD : PUT
    PARAMS : pk
    '''
    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        saved_cred = get_object_or_404(Credential.objects.all(), pk=pk)
        serializer = CredentialSerializer(instance=saved_cred, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            cred_saved = serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    '''
    METHOD : DELETE
    PARAMS : pk
    '''
    def delete(self, request, *args, **kwargs):
        # Get object with this pk
        pk = self.kwargs.get('pk')
        cred = get_object_or_404(Credential.objects.all(), pk=pk)
        cred.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


