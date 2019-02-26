from django.db import models

# Create your models here.
class House(models.Model):
    address = models.CharField(max_length=200, default="")
    buildDate = models.DateField(default="")
    numberOfBedrooms = models.IntegerField(default=0)

    def __str__(self):
        return self.address