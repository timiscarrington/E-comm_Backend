from django.db import models

# Create your models here.
# this going to be the models for each product
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()