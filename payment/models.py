from unicodedata import decimal
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    description = models.TextField()
    # using bigint in prod. instead of decimal when working 
    # with currencies is, as i know, a better practice
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name