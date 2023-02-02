from django.db import models


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

