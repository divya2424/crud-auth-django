from django.db import models

# Create your models here.

class Credential(models.Model):
    secret_key = models.CharField(max_length=120)
    client_key = models.CharField(max_length=120)