from django.db import models
import uuid

class Branch(models.Model):
    class Meta:
        verbose_name_plural = 'branches'
    bank = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    location_id = str(uuid.uuid4())

    def __str__(self):
        return(f"{self.bank} | {self.location}")
