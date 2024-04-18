from django.urls import path
from .views import *

urlpatterns = [
    path('new/', book_flight, name='book_flight'),
]