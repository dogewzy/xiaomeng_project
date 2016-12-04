from django.shortcuts import render
from .forms import MedicineForm
from .models import Medicine
from django.contrib.auth.decorators import permission_required


@permission_required(perm='medicine.add_medicine', login_url='http://localhost:8000/polls/login/')
def index(request):
    all_medicine = Medicine.objects.order_by('id')
    return render(request, 'medicine/index.html', {'all_medicine': all_medicine})


def add(request):
    form = MedicineForm()
    return render(request, 'medicine/add.html', {'form': form})
