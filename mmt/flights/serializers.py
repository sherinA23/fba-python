from rest_framework import serializers
from .models import Flight#, Aircraft

# class AircraftSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Aircraft
#         fields = ['id', 'name']

class FlightSerializer(serializers.ModelSerializer):
    # airline = AircraftSerializer()
    class Meta:
        model = Flight
        fields = ['id', 'airline', 'flight_number', 'source', 'destination', 'departure_date', 'duration', 'capacity', 'price']
    
