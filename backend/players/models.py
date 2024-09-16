from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    utr = models.FloatField()
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name
