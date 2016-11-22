from django import forms


class RegisterForm(forms.Form):
    挂号编号 = forms.IntegerField()
    姓名 = forms.CharField(max_length=100)
    section = (
        ('internist', '内科'),
        ('surgery', '外科'),
        (None, '请选择科室')
    )
    科室 = forms.ChoiceField(
        choices=section,
    )
    费用 = forms.FloatField()
    操作人 = forms.CharField(max_length=100)