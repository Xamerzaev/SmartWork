from django.shortcuts import render, redirect

from . import getbarcode

import qrcode
import random

def showpushcart(request):
    return render(request,'index.html')

def get_qr_code(request):
    data = f"qr{random.randint(1,50000)}"
    filename = 'static/yourcode.png'

    img = qrcode.make(data)
    img.save(filename)
    return redirect('showpushcart')
