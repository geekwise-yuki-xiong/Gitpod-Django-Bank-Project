from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=300)
    address = models.CharField(max_length=300)

    def __str__(self):
        return(f"{self.name} | {self.email}")