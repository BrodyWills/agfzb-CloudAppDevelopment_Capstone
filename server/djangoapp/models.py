from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(null=False, max_length=300)

    def __str__(self):
        return "Name:" + self.name + "\nDescription:" + self.description


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30)
    dealerId = models.IntegerField()
    choices = ('SEDAN', "Sedan"), ('SUV', "SUV"), ('WAGON', "Wagon"), ('TRUCK', "Truck")
    carType = models.CharField(null=False, choices=choices, max_length=20)
    year = models.DateField()

    def __str__(self):
        return "Name:" + self.name + "\Make:" + str(self.make)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
