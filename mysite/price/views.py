from django.shortcuts import render
from .forms import AddForm, PriceForm


def index(request):
    has_add = [1,2,3,1,4]
    if request.method == 'POST':
        pass
    else:
        addform = AddForm()
        priceform = PriceForm()
        return render(request, 'price/index.html', {'addform': addform, 'priceform': priceform})

