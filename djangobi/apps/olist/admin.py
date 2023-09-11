from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Geolocation)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderPayment)

