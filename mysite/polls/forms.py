from django import forms
from .models import Patient
from django.utils.translation import ugettext_lazy as _

class PatientForm(forms.Form):
    sex_choice = (
        ('male', '男'),
        ('female', '女'),
    )
    姓名 = forms.CharField(max_length=100)
    年龄 = forms.IntegerField()
    病人编号 = forms.IntegerField()
    电话号码 = forms.IntegerField()
    性别 = forms.ChoiceField(choices=sex_choice)


class TesPForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        labels = {
            'p_name': _('姓名'),
            'p_age': _('年龄'),
            'p_number': _('病人编号'),
            'p_tel_number': _('电话号码'),
            'p_sex': _('性别'),
            'p_marriage': _('婚姻状况'),
            'p_address': _('住址'),
            'p_id_num': _('身份证号码'),
        }


class EditForm(forms.Form):
    病人编号 = forms.IntegerField()


class EditToBeSaveForm(forms.Form):
    sex_choice = (
        ('male', '男'),
        ('female', '女'),
    )
    病人编号 = forms.IntegerField(label='你要修改的病人编号')
    姓名 = forms.CharField(max_length=100)
    年龄 = forms.IntegerField()
    电话号码 = forms.IntegerField()
    性别 = forms.ChoiceField(choices=sex_choice)


class LoginForm(forms.Form):
    账号 = forms.CharField(max_length=100)
    密码 = forms.CharField(max_length=100)