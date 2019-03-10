from django.db import models

# Create your models here.

class Pen(models.Model):
    brand = models.CharField(max_length=200) # change this to a search box
    name = models.CharField(max_length=200)
    stock_image = ''

    def __str__(self):
        return self.name


class Ink(models.Model):
    brand = models.CharField(max_length=200) # change this to a search box
    name = models.CharField(max_length=200)
    stock_image = ''
    colors = []

    def __str__(self):
        return self.name