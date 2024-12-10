from core.models import TimeStampedModel 
from django.db import models
from django.conf import settings
from core.models import City
from users.models import CustomUser

class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Make(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Model(TimeStampedModel):
    make = models.ForeignKey(Make, on_delete=models.CASCADE, related_name="models")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    make = models.ForeignKey(Make, on_delete=models.PROTECT)
    model = models.ForeignKey(Model, on_delete=models.PROTECT)
    model_date = models.DateField(auto_now_add=True)
    seats = models.PositiveIntegerField()
    color = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/images/')

    def __str__(self):
        return f"{self.make.name} {self.model.name}"


class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cars/images/')

    def __str__(self):
        return f"Image for {self.car.make.name} {self.car.model.name}"



class Reservation(TimeStampedModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pickup_location = models.ForeignKey(City, related_name='pickup_reservations', on_delete=models.CASCADE)
    drop_off_location = models.ForeignKey(City, related_name='dropoff_reservations', on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    passengers = models.PositiveIntegerField()
    car = models.ForeignKey(Car, related_name='car_reservations', on_delete=models.PROTECT, default=3)

    def __str__(self):
        return f"Reservation by {self.user}"

