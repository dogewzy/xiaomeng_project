from django import forms
from django.utils import timezone


class DiagnoseForm(forms.Form):
    处方 = forms.CharField(widget=forms.Textarea)
    诊断结果 = forms.CharField(widget=forms.Textarea)
    病人编号 = forms.IntegerField()
    诊断编号 = forms.IntegerField()
    诊断时间 = forms.TimeField(initial=timezone.now())
    操作人 = forms.CharField()
