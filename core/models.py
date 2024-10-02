from django.db import models

# Create your models here.
from django.db import models

class VehiclePlate(models.Model):
    plate = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    dirrecion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.plate} - {self.nombre}"