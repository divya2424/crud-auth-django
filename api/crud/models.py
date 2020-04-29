from django.db import models

# Create your models here.

'''
CRUD MODELS
'''
class Credential(models.Model):
    secret_key = models.CharField(max_length=120)
    client_key = models.CharField(max_length=120)

    '''
    __str__ method is used to compute the "official" string reputation of an object
    '''
    def __str__(self):
        return "#" + str(self.pk)

