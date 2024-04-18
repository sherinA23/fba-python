from django.db import models

# class Aircraft(models.Model):
#     name = models.CharField(max_length=4, unique=True, default='')

class Flight(models.Model):
    # airline = models.ForeignKey(Aircraft, on_delete=models.CASCADE, to_field='name')
    airline = models.CharField(max_length=4, unique=True, default='')
    flight_number = models.CharField(max_length=10)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    departure_date = models.DateField()
    duration = models.TextField()
    capacity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
