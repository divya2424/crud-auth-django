from rest_framework import serializers

from crud.models import Credential


class TokenSerializer(serializers.Serializer):
    class Meta:
        model = Credential
        fields = ("client_key", "secret_key")
