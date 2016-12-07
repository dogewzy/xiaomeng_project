from django.shortcuts import render
from .forms import DiagnoseForm
from .models import Diagnose
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required


@permission_required(perm='diagnose.add_diagnose',
                     login_url='http://localhost:8000/polls/login/')
def index(request):
    if request.method == 'POST':
        form = DiagnoseForm(request.POST)
        if form.is_valid():
            d = Diagnose()
            d.prescription = form.cleaned_data['处方']
            d.man = form.cleaned_data['操作人']
            d.d_num = form.cleaned_data['诊断编号']
            d.patient.p_number = form.cleaned_data['病人编号']
            d.result = form.cleaned_data['诊断结果']
            d.time = form.cleaned_data['诊断时间']
            d.save()
        return render(request, 'diagnose/index.html',)
    form = DiagnoseForm()
    return render(request, 'diagnose/index.html', {'form': form, 'name': request.user.username})



