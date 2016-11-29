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
    p_name = models.CharField(max_length=100, default='template')
    p_age = models.IntegerField(default=0)
    p_number = models.IntegerField(default=0)
    p_tel_number = models.IntegerField(default=0)
    p_sex = models.CharField(choices=sex_choice, max_length=2, default='男')

    def change(self, name, num, tel, sex):
        self.p_name = name
        self.p_age = num
        self.p_tel_number = tel
        self.p_sex = sex
        self.save()


# Create your models here.
