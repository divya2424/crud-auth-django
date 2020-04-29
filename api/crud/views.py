# from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
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
        else:
            cred = Credential.objects.filter(pk=pk)        
        # the many param informs the serializer that it will be serializing more than a single credential.
        serializer = CredentialSerializer(cred, many=True)
        return Response({"cred": serializer.data})
        
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
            msg =  "created successfully" if created == True else "updated successfully"
        return Response({"success": "Credential '{}' ".format(credential) + msg })

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

        return Response({"success": "Credential '{}' updated successfully".format(cred_saved.id)})
    '''
    METHOD : DELETE
    PARAMS : pk
    '''
    def delete(self, request, *args, **kwargs):
        # Get object with this pk
        pk = self.kwargs.get('pk')
        cred = get_object_or_404(Credential.objects.all(), pk=pk)
        cred.delete()
        return Response({"message": "Credential with id `{}` has been deleted.".format(pk)},status=204)


