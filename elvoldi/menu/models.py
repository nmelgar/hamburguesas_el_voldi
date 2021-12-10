from django.db import models
from django.db.models.fields import CharField

class Meal(models.Model):
    CATEGORY_CHOICES = [('H', 'Hamburguesa'), ('P', 'Papas'), ('B', 'Bebida')]
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, blank=False)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    cost = models.IntegerField()
