from django.shortcuts import render, redirect
from .models import Patient
from .forms import PatientForm, EditForm, EditToBeSaveForm, TesPForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import permission_required, login_required
from .decorator import perm_deco


def index(request):
    return render(request, 'polls/index.html')


@permission_required(perm='polls.add_patient', login_url='http://localhost:8000/polls/login/')
def patient(request):
    if request.user.has_perm('polls.add_patient'):
        all_patients = Patient.objects.order_by('id')
        return render(request, 'polls/patient.html', {'all_patients': all_patients})
    else:
        if request.user.is_anonymous():
            return redirect('http://localhost:8000/polls/login/')
        else:
            return render(request, 'polls/no_permission.html')



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


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['账号']
            password = form.cleaned_data['密码']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                print(user.user_permissions)
                return render(request, 'polls/patient_edit.html')
            else:
                pass
    else:
        form = LoginForm()
        return render(request, 'polls/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    message = '您已经登出'
    return render(request, 'polls/index.html', {'message': message})


