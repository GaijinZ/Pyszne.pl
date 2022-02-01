from django.contrib import admin

from .models import Restaurant, TypeOfRestaurant, Delivery, Address, Menu


admin.site.register(Restaurant)
admin.site.register(TypeOfRestaurant)
admin.site.register(Delivery)
admin.site.register(Address)
admin.site.register(Menu)
