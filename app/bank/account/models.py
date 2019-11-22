from django.db import models
from bank.branch.models import Branch
from bank.customer.models import Customer

class Account(models.Model):
    bank_partner = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE,
        related_name='bank_partner',
    )
    holder = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
    )
    balance = models.DecimalField(max_digits=300, decimal_places=2)

    def __str__(self):
        return(f"Account Holder: {self.holder} | Balance: {self.balance}")