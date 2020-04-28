from rest_framework import serializers

from .models import Credential


class CredentialSerializer(serializers.Serializer):
    client_key = serializers.CharField(max_length=120)
    secret_key = serializers.CharField(max_length=120)
    id = serializers.IntegerField()

    def create(self, validated_data):
        credential, created = Credential.objects.update_or_create(
        client_key=validated_data.get('client_key', None),
        defaults={'client_key': validated_data.get('client_key', None),'secret_key': validated_data.get('secret_key', None)})
        return credential,created
        # return Credential.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.client_key = validated_data.get('client_key', instance.client_key)
        instance.secret_key = validated_data.get('secret_key', instance.secret_key)
        instance.save()
        return instance

    