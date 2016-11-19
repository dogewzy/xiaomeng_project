from django.shortcuts import render
from .models import Patient
from .forms import PatientForm, EditForm, EditToBeSaveForm


def index(request):
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
            new_p.save()
            is_ok = True
            return render(request, 'polls/patient_log.html', {'form': form, 'isok': is_ok})
    else:
        form = PatientForm()
    return render(request, 'polls/patient_log.html', {'form': form, 'isok': is_ok})


def patient_num(request):
    if request.method == 'POST':
        form1 = EditForm(request.POST)
        if form1.is_valid():
            to_be_save = EditToBeSaveForm()
            target_number = form1.cleaned_data['病人编号']
            context = {
                'form': to_be_save,
                'num': target_number,
            }
            return render(request, 'polls/patient_edit.html', {'context': context,})
    else:
        form1 = EditForm()
        return render(request, 'polls/patient_num.html', {'form1': form1})


def patient_edit(request):
    if request.method == 'POST':
        form2 = EditToBeSaveForm(request.POST)
        if form2.is_valid():
            target_number = form2.cleaned_data['病人编号']
            target_patient = Patient.objects.filter(p_number=target_number)[0]
            target_patient.p_name = form2.cleaned_data['姓名']
            target_patient.p_sex = form2.cleaned_data['性别']
            target_patient.p_age = form2.cleaned_data['年龄']
            target_patient.p_tel_number = form2.cleaned_data['电话号码']
            target_patient.save()
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

