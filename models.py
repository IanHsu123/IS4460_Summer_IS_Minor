from django.db import models

# Create your models here.

class Driver(models.Model):
    driver_first_name = models.CharField(max_length=100)
    driver_middle_name = models.CharField(max_length=100)
    driver_last_name = models.CharField(max_length=100)
    driver_type = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def _str_(self):
        return f"Driver {self.id} by {self.driver_first_name} and {self.driver_last_name}"
    
class Vehicle(models.Model):
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
    license_plate_number = models.CharField(max_length=100)
    vehicle_make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.CharField(max_length=100)

    def _str_(self):
        return f"Vehicle {self.id} by {self.driver}"

class Permit(models.Model):
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    purchase_date = models.DateField()
    expiry_date = models.DateField()
    cost = models.IntegerField()
    permit_type = models.CharField(max_length=100)

    def _str_(self):
        return f"Permit {self.id} by {self.vehicle}"