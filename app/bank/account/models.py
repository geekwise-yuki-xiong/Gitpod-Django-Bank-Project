from django.db import models

class Account(models.Model):
    holder = models.CharField(max_length=300)
    balance = models.DecimalField(max_digits=300, decimal_places=2)

    def __str__(self):
        return(f"Account Holder: {self.holder} | Balance: {self.balance}")