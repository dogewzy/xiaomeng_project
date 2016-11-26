from django.db import models


class Price(models.Model):
    划价编号 = models.IntegerField()
    病人编号 = models.IntegerField()
    操作人 = models.CharField(max_length=100)
    # 药品信息存储格式为： '药品1编号！药品1数量# 药品2编号！药品2数量'
    药品信息 = models.CharField(max_length=500, null=True)

    def __str__(self):
        return '划价编号' + ': ' + str(self.划价编号)


class Medicine(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    unit = models.CharField(max_length=100)
    sort = models.CharField(max_length=100)