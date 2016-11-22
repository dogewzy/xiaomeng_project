from django.db import models


class Medicine(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    unit = models.CharField(max_length=100)
    sort = models.CharField(max_length=100)

