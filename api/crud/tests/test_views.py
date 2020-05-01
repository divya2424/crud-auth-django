from django.test import TestCase,Client
from django.urls import reverse
from crud.models import Credential
import json
from rest_framework import status
from crud.serializers import CredentialSerializer

'''
Test Cases For CRUD Views
'''

# initialize the APIClient app
client = Client()


class GetAllCredentialTest(TestCase):
    """ Test module for GET all credential from API """

    def setUp(self):
        Credential.objects.create(
            secret_key='NfainCcmbafiCUiutV7IKmjn8NbOCbw6Xc16a-_MDVyC0jhfbekNIpQ3z3sNUHhNJJEhK3ORSbh8WWbf9zSGpQ', client_key='69bd83f1-1172-4b02-821a-b5a2af5a32da')
        Credential.objects.create(
            secret_key='NfainCcmbafiCUiutV7IKmjn8NbOCbw6Xc16a-_MDVyC0jhfbekNIpJ3z3sNUHhNJJEhK3ORSbh8WWbf9zSGpK', client_key='78bd83f1-1172-4b02-821a-b5a2af5a32da')
      

    def test_get_all_credential(self):
        # get API response
        response = client.get(reverse('crud:crud'))
        # get data from db
        credential = Credential.objects.all()
        serializer = CredentialSerializer(credential, many=True)
        data = {'cred': serializer.data}
        self.assertEqual(response.data,data)
        

class GetSingleCredentialTest(TestCase):
    """ Test module for GET single credential API """

    def setUp(self):
        self.first = Credential.objects.create(
            secret_key='NfainCcmbafiCUiutV7IKmjn8NbOCbw6Xc16a-_MDVyC0jhfbekNIpQ3z3sNUHhNJJEhK3ORSbh8WWbf9zSGpQ', client_key='69bd83f1-1172-4b02-821a-b5a2af5a32da')

    def test_get_valid_single_credential(self):
        response = client.get(
            reverse('crud:crud', kwargs={'pk': self.first.pk}))
        credential = Credential.objects.get(pk=self.first.pk)
        serializer = CredentialSerializer(credential)
        data = {'cred': serializer.data}
        self.assertEqual(response.data, data)

    def test_get_invalid_single_credential(self):
        response = client.get(
            reverse('crud:crud', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



class CreateNewCredentialTest(TestCase):

    """ Test module for inserting a new credential """

    def setUp(self):
        self.valid_payload = {
            'secret_key':'NfainCcmbafiCUiutV7IKmjn8NbOCbw6Xc16a-_MDVyC0jhfbekNIpQ3z3sNUHhNJJEhK3ORSbh8WWbf9zSGpQ', 'client_key':'69bd83f1-1172-4b02-821a-b5a2af5a32da'
        }

        self.invalid_payload = {
            'secret_key':'', 'client_key':'69bd83f1-1172-4b02-821a-b5a2af5a32da'
        }

    def test_create_valid_credential(self):
        response = client.post(
            reverse('crud:crud'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        print('response',response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_credential(self):
        response = client.post(
            reverse('crud:crud'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class UpdateCredentialCredentialTest(TestCase):
    """ Test module for updating an existing credential record """

    def setUp(self):
        self.first = Credential.objects.create(
            secret_key='NfainCcmbafiCUiutV7IKmjn8NbOCbw6Xc16a-_MDVyC0jhfbekNIpQ3z3sNUHhNJJEhK3ORSbh8WWbf9zSGpQ', client_key='69bd83f1-1172-4b02-821a-b5a2af5a32da')

        self.valid_payload = {
            'secret_key':'NfainCcmbafiCUiutV7IKmjn8NbOCbw6Xc16a-_MDVyC0jhfbekNIpQ3z3sNUHhNJJEhK3ORSbh8WWbf9zSGpQ', 'client_key':'69bd83f1-1172-4b02-821a-b5a2af5a32da'
        }

        self.invalid_payload = {
            'secret_key':'', 'client_key':'69bd83f1-1172-4b02-821a-b5a2af5a32da'
        }
    def test_valid_update_credential(self):
        response = client.put(
            reverse('crud:crud', kwargs={'pk': self.first.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_credential(self):
        response = client.put(
            reverse('crud:crud', kwargs={'pk': self.first.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class DeleteSingleCredentialTest(TestCase):
    """ Test module for deleting an existing credential record """

    def setUp(self):
         self.first = Credential.objects.create(
            secret_key='NfainCcmbafiCUiutV7IKmjn8NbOCbw6Xc16a-_MDVyC0jhfbekNIpQ3z3sNUHhNJJEhK3ORSbh8WWbf9zSGpQ', client_key='69bd83f1-1172-4b02-821a-b5a2af5a32da')

    def test_valid_delete_credential(self):
        response = client.delete(
            reverse('crud:crud', kwargs={'pk': self.first.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_credential(self):
        response = client.delete(
            reverse('crud:crud', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)