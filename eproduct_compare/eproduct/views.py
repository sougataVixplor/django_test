from django.shortcuts import render
from django.http import HttpResponse
from eproduct.models import User,Product,Item

def homepage(request):
    return HttpResponse("Hi, You r in Home Page")
# Create your views here.

def insertCompanyData(request):
    data=User(siteName='ebay',sector='Ecommers',url='www.ebay.com',status=False)
    data.save()
    return HttpResponse("Data Inserted")

    
def viewCompanyData(request):
    cdata=User.objects.all().values()
    return HttpResponse(cdata)
