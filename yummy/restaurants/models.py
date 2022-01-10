from django.db import models


class Address(models.Model):
    city = models.CharField(max_length=250)
    post_code = models.CharField(max_length=10)
    street_name = models.CharField(max_length=250)
    building_number = models.IntegerField()

    def __str__(self):
        return f'{self.city} {self.post_code}, {self.street_name}'


class TypeOfRestaurant(models.Model):
    type_of_restaurant = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.type_of_restaurant}'


class Delivery(models.Model):
    delivery_option = models.BooleanField(default=False)
    price_to_deliver = models.IntegerField(null=True, blank=True)
    time_to_deliver = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'{self.delivery_option}'


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    restaurant_type = models.ManyToManyField(TypeOfRestaurant)
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='restaurant_picture', blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
