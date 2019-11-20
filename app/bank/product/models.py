from django.db import models

class Product(models.Model):
    services = (
        ('checking', 'CHECKING'),
        ('savings', 'SAVINGS'),
        ('debit', 'DEBIT'),
        ('credit', 'CREDIT')
    )

    product_options = models.CharField(
        max_length=50,
        choices=services,
        default=services[0],
    )

    def __str__(self):
        return(f"Product: {self.product_options}")