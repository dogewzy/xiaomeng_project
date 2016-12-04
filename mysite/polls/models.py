import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now()
    datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question,
                                 on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Patient(models.Model):
    sex_choice = (
        ('男', '男'),
        ('女', '女'),
    )
    m_choice = (
        ('已婚', '已婚'),
        ('未婚', '未婚')
    )
    p_name = models.CharField(max_length=100, default=' ')
    p_age = models.IntegerField(default='')
    p_number = models.IntegerField(default='')
    p_tel_number = models.IntegerField(default='')
    p_sex = models.CharField(choices=sex_choice, max_length=2, default='男')
    p_marriage = models.CharField(choices=m_choice, max_length=2, default=' ')
    p_address = models.CharField(max_length=100, default=' ', null=True)
    p_id_num = models.CharField(max_length=100, default=' ', null=True)

    def __str__(self):
        return str(self.p_name)





