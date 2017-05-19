from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    factory_name = models.CharField(max_length=30)
    bar_code = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    amount = models.IntegerField()
    picture = models.FileField(upload_to="product_", blank=False, null=True)

    def __str__(self):
        return self.product_name
    
