from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_flight, name='flight-add'),
    path('index/', get, name='show_fligts'),
    path('search/', search, name='search_flights'),
    path('get/<int:flight_id>/', get_by_id, name='get_flight_by_id'),
    path('update/<int:flight_id>/', update_id, name='update_flight_id'),
]