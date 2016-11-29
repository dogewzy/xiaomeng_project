from django import forms


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
