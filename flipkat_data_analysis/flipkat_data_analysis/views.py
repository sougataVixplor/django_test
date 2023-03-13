from django.http import HttpResponse
from django.shortcuts import render

data={
    'title':'home=page',
    'num':[1,2,3,4]
}




def mypage(request):
    return HttpResponse('<b>This is my page<b>')


def homepage(request):
    return render(request,"index.html",data)