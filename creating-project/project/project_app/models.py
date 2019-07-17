from django.db import models


# Create your models here.
class Station(models.Model):
    latitude = models.FloatField()
    longtitude = models.FloatField()
    routes = models.ManyToManyField('Route', related_name='stations')
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
