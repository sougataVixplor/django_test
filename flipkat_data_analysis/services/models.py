from django.db import models

class Service(models.Model):
    service_icon=models.CharField(max_length=100)
    service_address=models.TextField()


# Create your models here.
