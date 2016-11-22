from django.shortcuts import render
from .forms import RegisterForm
from .models import RegisterModel


def register(request):
    return render(request, 'registration/register.html')


def search(request):
    return render(request, 'registration/search.html')


def index(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_d = RegisterModel()
            new_d.cost = form.cleaned_data['费用']
            new_d.name = form.cleaned_data['姓名']
            new_d.operator = form.cleaned_data['操作人']
            new_d.section = form.cleaned_data['科室']
            new_d.register_num = form.cleaned_data['挂号编号']
            new_d.save()
            return render(request, 'registration/display.html')
    else:
        form = RegisterForm()
        return render(request, 'registration/index.html', {'form': form})


def display(request):
    return render(request, 'registration/display.html')