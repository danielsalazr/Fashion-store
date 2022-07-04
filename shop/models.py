from email.mime import image
from email.policy import default
from pyexpat import model
from unicodedata import name
from django.db import models
#from django.utils import timezone

# Create your models here.
class Productos(models.Model):
    sku =   models.CharField(max_length=50)
    name  = models.CharField( max_length=50)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    image = models.CharField( max_length=50)
    categoria = models.CharField( max_length=50)



