from django.db import models


class RegisterForm(models.Model):
    register_num = models.IntegerField()
    name = models.CharField(max_length=100)
    SECTION_CHOICE = (
        ('internist', '内科'),
        ('surgery', '外科'),
        (None, '请选择科室')
    )
    section = models.CharField(
        choices=SECTION_CHOICE,
        max_length=100,
    )
    cost = models.FloatField()
    operator = models.CharField(max_length=100)
