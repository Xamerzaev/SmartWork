from django.shortcuts import render

from . import getbarcode

def showpushcart(request):
    return render(request,'index.html')