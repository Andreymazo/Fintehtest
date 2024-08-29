from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=0, max_digits=7)
    
    def __str__(self) -> str:
        return self.name 
