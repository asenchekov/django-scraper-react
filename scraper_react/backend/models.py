from django.db import models


class Item(models.Model):
  url = models.URLField(max_length=200)
  name = models.CharField(max_length=200)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  sku = models.CharField(max_length=200)
  description = models.TextField()