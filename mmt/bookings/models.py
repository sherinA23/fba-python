from django.db import models
from users.models import Users
from flights.models import Flight

class Bookings(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    no_of_passengers = models.IntegerField()
