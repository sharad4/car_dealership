from django.db import models

# Create your models here.

class Listings(models.Model):
    name = models.CharField(max_length=100)