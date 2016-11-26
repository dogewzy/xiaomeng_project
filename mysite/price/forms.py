from django import forms


class AddForm(forms.Form):
    药品名称 = forms.CharField(max_length=100)
    数量 = forms.IntegerField()


class PriceForm(forms.Form):
    划价编号 = forms.IntegerField()
    病人编号 = forms.IntegerField()
    操作人 = forms.CharField(max_length=100)
