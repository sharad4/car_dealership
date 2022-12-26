from django.db import models

# Create your models here.

class Listings(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    milage = models.IntegerField()
    price = models.IntegerField()
    #image

    def __str__(self):
        return self.name