from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.authentication import TokenAuthentication
from .models import Bookings
from flights.models import Flight
from rest_framework.response import Response
import requests

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def book_flight(request):
    nop = request.query_params.get('no_of_passengers')
    flight = Flight.objects.get(id = request.query_params.get('flight_id'))
    book = Bookings.objects.create(user = request.user, flight = flight, no_of_passengers = nop)
    # url = "http://localhost:8000/flights/get/" + str(flight.id) +"/"
    # response = requests.get(url)
    capacity_new = int(flight.capacity) - int(nop)
    url = "http://localhost:8000/flights/update/" + str(flight.id) +"/"
    data = {
        'capacity' : capacity_new,
    }
    response_new = requests.put(url, params = data)
    return Response({'message': 'Booking successful'})
