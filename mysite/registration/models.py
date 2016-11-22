from django.db import models


class RegisterModel(models.Model):
    register_num = models.IntegerField()
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    cost = models.FloatField()
    operator = models.CharField(max_length=100)
