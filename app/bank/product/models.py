from django.db import models
from bank.branch.models import Branch

class Product(models.Model):
    provider = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name='provider',
    )
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
        return(f"Bank: {self.provider.bank} | Product: {self.product_options}")