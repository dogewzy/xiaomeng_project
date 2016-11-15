from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Patient
from django.urls import reverse


def index(request):
    return render(request, 'polls/index.html')


def detail(request):
    return render(request, 'polls/detail.html')


def vote(request):
    return render(request, 'polls/vote.html')


def results(request):
    return render(request, 'polls/results.html')


def patient(request):
    all_patients = Patient.objects.order_by('patient_information')
    return render(request, 'polls/patient.html', {'all_patient': all_patients})


def patient_log(request):
    return render(request, 'polls/patient_log.html')