from django.urls import path

from pushcart.views import showpushcart

urlpatterns = [
    path('', showpushcart, name='showpushcart'),
    ]
