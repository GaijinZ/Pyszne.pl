from django.db import models


class TypeOfRestaurant(models.Model):
    type_of_restaurant = models.CharField(max_length=50, null=True, blank=True)


class Delivery(models.Model):
    delivery_option = models.BooleanField(default=False)
    price_to_deliver = models.IntegerField(null=True, blank=True)
    time_to_deliver = models.FloatField(null=True, blank=True)


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    restaurant_type = models.ManyToManyField(TypeOfRestaurant)
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='restaurant_picture')
