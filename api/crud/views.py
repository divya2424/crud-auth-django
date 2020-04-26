# from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .serializers import CredentialSerializer

from .models import Credential


class CredentialView(APIView):
    def get(self, request):
        cred = Credential.objects.all()
        # the many param informs the serializer that it will be serializing more than a single credential.
        serializer = CredentialSerializer(cred, many=True)
        return Response({"cred": serializer.data})

    def post(self, request):
        client_key = request.data.get('client_key')
        secret_key = request.data.get('secret_key')

        # Create an credntial from the above data
        serializer = CredentialSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            cred_saved = serializer.save()
        return Response({"success": "Credential '{}' created successfully".format(cred_saved)})

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        saved_cred = get_object_or_404(Credential.objects.all(), pk=pk)
       
        serializer = CredentialSerializer(instance=saved_cred, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            cred_saved = serializer.save()
        return Response({"success": "Credential '{}' updated successfully".format(cred_saved.id)})

    def delete(self, request, *args, **kwargs):
        # Get object with this pk
        pk = self.kwargs.get('pk')
        cred = get_object_or_404(Credential.objects.all(), pk=pk)
        cred.delete()
        return Response({"message": "Credential with id `{}` has been deleted.".format(pk)},status=204)


