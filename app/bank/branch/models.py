from django.db import models
import uuid

class Branch(models.Model):
    bank = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    location_id = str(uuid.uuid4())

    def __str__(self):
        return(f"{self.bank} | {self.location} | ID: {self.location_id}")
