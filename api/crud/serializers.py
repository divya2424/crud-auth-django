from rest_framework import serializers
from .models import Credential
import requests
from django.conf import settings
import json
headers = {
    "Content-Type": settings.CONTENT_TYPE,
    "Accept": settings.ACCEPT[0],
}


'''
Credential Serializer class created
'''
class CredentialSerializer(serializers.Serializer):
    client_key = serializers.CharField(max_length=120)
    secret_key = serializers.CharField(max_length=120)
    # id = serializers.IntegerField()

    '''
    When post method is used it will take the parameters client_id & secret_id
    if client_id exists:
        update
    else:
        create the object
    '''
    def validate(self, data):
        URL = (settings.TOKEN_URL
                                + "&client_id="
                                + data['client_key']
                                + "&client_secret="
                                + data['secret_key']
                            )
        response = requests.request(
                                "POST", URL, data=json.dumps({}), headers=headers)
        if response.status_code == 200:
            return data
        else:
            raise serializers.ValidationError('Invalid Credentials')


    def create(self, validated_data):
        credential, created = Credential.objects.update_or_create(
        client_key=validated_data.get('client_key', None),
        defaults={'client_key': validated_data.get('client_key', None),'secret_key': validated_data.get('secret_key', None)})
        return credential,created
        # return Credential.objects.create(**validated_data)

    '''
    when put method is used and it recieves the pk from params
    client_id & secret_key will be updated
    '''

    def update(self, instance, validated_data):
        instance.client_key = validated_data.get('client_key', instance.client_key)
        instance.secret_key = validated_data.get('secret_key', instance.secret_key)
        instance.save()
        return instance

    