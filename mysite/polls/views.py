from django.shortcuts import render
from .models import Patient
from .forms import PatientForm, EditForm, EditToBeSaveForm, TesPForm


def index(request):
    print('222222222222222')
    return render(request, 'polls/index.html')


def patient(request):
    all_patients = Patient.objects.order_by('id')
    return render(request, 'polls/patient.html', {'all_patients': all_patients})


def patient_log(request):
    is_ok = False
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            new_p = Patient()
            new_p.p_name = form.cleaned_data['姓名']
            new_p.p_sex = form.cleaned_data['性别']
            new_p.p_age = form.cleaned_data['年龄']
            new_p.p_number = form.cleaned_data['病人编号']
            new_p.p_tel_number = form.cleaned_data['电话号码']
            new_p.p_address = form.cleaned_data['住址']
            new_p.p_marriage = form.cleaned_data['婚姻状况']
            new_p.p_id_num = form.cleaned_data['身份证号码']
            new_p.save()
            is_ok = True
            return render(request, 'polls/patient_log.html', {'form': form, 'isok': is_ok})
    else:
        form = TesPForm()
    return render(request, 'polls/patient_log.html', {'form': form, 'isok': is_ok})


def patient_num(request):
    if request.method == 'POST':
        form = EditToBeSaveForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data['病人编号']
            new_p = Patient.objects.get(p_number=num)
            if new_p:
                new_p.p_name = form.cleaned_data['姓名']
                new_p.p_sex = form.cleaned_data['性别']
                new_p.p_age = form.cleaned_data['年龄']
                new_p.p_tel_number = form.cleaned_data['电话号码']
                new_p.save()
                return render(request, 'polls/patient_edit.html')
    else:
        form = EditToBeSaveForm()
        return render(request, 'polls/patient_num.html', {'form': form})


def patient_edit(request):
    return render(request, 'polls/patient_edit.html')









def patient_search(request):
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['病人编号']
            patient_s = Patient.objects.filter(p_number=number)[0]
            return render(request, 'polls/patient_display.html', {'patient': patient_s})
    else:
        form = EditForm()
        return render(request, 'polls/patient_search.html', {'form': form})

