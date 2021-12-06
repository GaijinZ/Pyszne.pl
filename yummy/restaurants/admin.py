from django.contrib import admin

from .models import Restaurant, TypeOfRestaurant, Delivery


admin.site.register(Restaurant)
admin.site.register(TypeOfRestaurant)
admin.site.register(Delivery)
