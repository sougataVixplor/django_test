from statistics import mode
from unicodedata import category
from django.db import models


class User(models.Model):
    siteName=models.CharField(max_length=255)
    sector=models.CharField(max_length=255)
    url=models.CharField(max_length=255)
    status=models.BooleanField()
    
class Product(models.Model):
    productName=models.CharField(max_length=255)
    productCategory=models.CharField(max_length=255)
    poductUrl=models.CharField(max_length=255)
    status=models.BooleanField()
    sites=models.ForeignKey(User, on_delete=models.CASCADE)

class Item(models.Model):
    itemName=models.CharField(max_length=255)
    rating=models.DecimalField(max_digits=6,decimal_places=3)
    price=models.DecimalField(max_digits=6,decimal_places=3)
    link=models.CharField(max_length=255)
    status=models.BooleanField()
    product=models.ForeignKey(Product, on_delete=models.CASCADE)


# Create your models here.
