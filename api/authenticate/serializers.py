from rest_framework import serializers

from crud.models import Credential

'''
Token Serializer created to validate the fields of Credential Model
'''
class TokenSerializer(serializers.Serializer):
    class Meta:
        model = Credential
        fields = ("client_key", "secret_key")
