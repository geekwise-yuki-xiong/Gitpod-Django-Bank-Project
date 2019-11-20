from django.contrib import admin
from bank.product.models import Product
from bank.customer.models import Customer
from bank.branch.models import Branch
from bank.account.models import Account
# Register your models here.

admin.site.register(
    (
        Product,
        Customer,
        Branch,
        Account,
    )
)
