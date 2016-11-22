from django.shortcuts import render
from .forms import MedicineForm
from .models import Medicine


def index(request):
    all_medicine = Medicine.objects.order_by('id')
    return render(request, 'medicine/index.html', {'all_medicine': all_medicine})


def add(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            new = Medicine()
            new.name = form.cleaned_data['药品名称']
            new.price = form.cleaned_data['药品价格']
            new.number = form.cleaned_data['药品编号']
            new.sort = form.cleaned_data['药品分类']
            new.unit = form.cleaned_data['计价单位']
            new.save()
            return render(request, 'medicine/index.html')
    else:
        t = 1
        form = MedicineForm()
        return render(request, 'medicine/add.html', {'form': form, 't': t},)
