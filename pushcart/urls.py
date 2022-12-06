from django.urls import path

from pushcart.views import showpushcart, get_qr_code

urlpatterns = [
    path('', showpushcart, name='showpushcart'),
    path('getcode/', get_qr_code, name='get_qr_code'),
    ]
