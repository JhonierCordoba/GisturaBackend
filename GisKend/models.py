from django.db import models

class Evento(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    imageUrls = models.BooleanField(default=False)
    minAge = models.IntegerField()
    location = models.CharField(max_length=30)
    price = models.IntegerField()
    sponsor = models.CharField(max_length=100)
    schedule = models.BooleanField()
    category = models.CharField(max_length=100)


    def __str__(self):
        return self.name

