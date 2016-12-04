from django.db import models
from django.utils import timezone


class Diagnose(models.Model):
    d_num = models.IntegerField(default=0)
    prescription = models.TextField(default='')
    result = models.TextField(default='')
    time = models.TimeField(default=timezone.now)
    man = models.CharField(default='临时', max_length=10)
    patient = models.ForeignKey('polls.Patient', on_delete=models.CASCADE, related_name='+', null=True)

    def __str__(self):
        return str(self.d_num)