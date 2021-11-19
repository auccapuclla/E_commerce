from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Product(models.Model):
    name_product = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    number_stars = models.IntegerField()