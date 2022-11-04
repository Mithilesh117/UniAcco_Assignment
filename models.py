from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    comment = models.TextField(max_length=400)
    date = models.DateField()

class Sign(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.IntegerField(max_length=25)
    password2 = models.IntegerField(max_length=25)
    

def __str__(self):
 return self.name
