from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# this going to be the models for each product
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField
    category = models.CharField(max_length=200)
    description = models.TextField()
    qty = models.FloatField(default=0)
    image = models.CharField(max_length=300)
    image2= models.CharField(max_length=300, default='https://www.jta.org/wp-content/uploads/2017/06/bubble-gum-960x600.jpg')

class Customer(models.Model):
    class Meta:
        db_table = "customer"
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=18, default='')

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, default='')
    image = models.CharField(max_length=300, default='')

