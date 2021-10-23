from django.db import models


class TypeOfRestaurant(models.Model):
    pass


class Delivery(models.Model):
    pass


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    restaurant_type = models.ManyToManyField(TypeOfRestaurant)
    delivery = models.ManyToManyField(Delivery)
    picture = models.ImageField(upload_to='restaurant_picture')
