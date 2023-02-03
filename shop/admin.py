from django.contrib import admin
from .models import Products, Customer, Cart

# Register your models here.

admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Cart)

