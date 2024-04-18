from django.shortcuts import render
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .models import Flight
from rest_framework import status



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_flight(request):
    serializer = FlightSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print("Request Data:", request.data)
        print("Response Data:", serializer.data)
        return Response(e, status=500)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get(APIView):
    queryset = Flight.objects.all()
    serializer_data = FlightSerializer(queryset, many= True)
    return Response(serializer_data.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def search(request):
    source = request.data.get('source')
    destination = request.data.get('destination')
    date = request.data.get('departure_date')
    nop = request.data.get('no_of_passengers')
    queryset = Flight.objects.filter(source = source, destination = destination, departure_date = date, capacity__gt = nop)
    serializer_data = FlightSerializer(queryset, many= True)
    return Response(serializer_data.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_by_id(request, flight_id):
    res = Flight.objects.get(id = flight_id)
    serialize = FlightSerializer(res)
    return Response(serialize.data)

@api_view(['PUT'])
def update_id(request, flight_id):
    flight = Flight.objects.get(id = flight_id)
    flight.capacity = request.query_params.get('capacity')
    flight.save()
    return Response({'message': "Updated successfully"})
