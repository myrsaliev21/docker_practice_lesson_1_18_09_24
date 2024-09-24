from django.db import models

# Create your models here.

class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    info = models.TextField()
