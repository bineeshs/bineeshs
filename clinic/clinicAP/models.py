from django.db import models

# Create your models here.
from django.db import models

class Booked(models.Model):
    name=models.CharField(max_length=250)
    contact = models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return  self.name