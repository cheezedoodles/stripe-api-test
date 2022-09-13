import stripe

from django.db import models
from django.conf import settings


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128, db_index=True)
    description = models.TextField()
    # using bigint in prod. instead of decimal when working
    # with currencies is, as i know, a better practice
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)
        stripe.Product.create(
            api_key=settings.STRIPE_API_KEY,
            id=self.id,
            name=self.name,
            description=self.description,
        )
        stripe.Price.create(
            api_key=settings.STRIPE_API_KEY,
            product=self.id,
            currency="usd",
            unit_amount=self.price * 100,
        )
