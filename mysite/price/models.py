from django.db import models


class Price(models.Model):
    划价编号 = models.IntegerField()
    病人编号 = models.IntegerField()
    操作人 = models.CharField(max_length=100)
    # 药品信息存储格式为： '药品1编号！药品1数量# 药品2编号！药品2数量'
    药品信息 = models.CharField(max_length=500, null=True)

    def __str__(self):
        return '划价编号' + ': ' + str(self.划价编号)

    def get_medicine_list(self):
        # 返回一个药品信息的list
        total = []
        l1 = self.药品信息.split('#')
        for item in l1[:-1]:
            l2 = item.split('!')
            m_name = l2[0]
            m_num = l2[1]
            m_price = Medicine.objects.get(name=m_name).price
            total.append([m_name, m_num, m_price])
        return total

    def get_total_price(self):
        # 返回该划价的总价
        total = 0
        l1 = self.药品信息.split('#')
        for item in l1[:-1]:
            l2 = item.split('!')
            # 名称
            m_name = l2[0]
            # 数量
            m_num = l2[1]
            m_price = Medicine.objects.get(name=m_name).price
            total += float(m_num) * m_price
        return total

class Medicine(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    unit = models.CharField(max_length=100)
    sort = models.CharField(max_length=100)




