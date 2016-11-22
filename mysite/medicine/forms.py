from django import forms


class MedicineForm(forms.Form):
    药品编号 = forms.IntegerField()
    药品名称 = forms.CharField(max_length=100)
    药品价格 = forms.IntegerField()
    jj_choice = {
        '瓶': '瓶',
        '包': '包',
        '盒': '盒',
    }
    计价单位 = forms.ChoiceField(
        choices=jj_choice
    )
    药品分类 = forms.CharField(max_length=100)
