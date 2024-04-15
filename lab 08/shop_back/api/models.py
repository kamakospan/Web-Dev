from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField(default = True)

    class Meta:
        app_label = 'api'

class Category(models.Model):
    name = models.CharField(max_length = 100)

    class Meta:
        app_label = 'api'
