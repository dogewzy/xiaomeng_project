from django.shortcuts import render
from .forms import AddForm, PriceForm, SearchForm
from .models import Price, Medicine
from django.contrib.auth.decorators import permission_required


@permission_required(perm='price.add_price',
                     login_url='http://localhost:8000/polls/login/')
def index(request):
    # 显示划价信息表单
    priceform = PriceForm()
    return render(request, 'price/index.html', {'priceform': priceform})


def main_information(request):
    # 接收基本划价信息
    if request.method == 'POST':
        form = PriceForm(request.POST)
        if form.is_valid():
            new = Price()
            new.划价编号 = form.cleaned_data['划价编号']
            new.病人编号 = form.cleaned_data['病人编号']
            new.操作人 = form.cleaned_data['操作人']
            new.药品信息 = ''
            new.save()
            addform = AddForm()
            return render(request, 'price/medicine.html', {'number': new.划价编号, 'addform': addform})


def medicine_information(request):
    # 显示药品划价信息表单,以及已经添加的药品
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            number = request.POST['number']
            the_price = Price.objects.filter(划价编号=number)[0]
            the_price.药品信息 += form.cleaned_data['药品名称'] + '!' + str(form.cleaned_data['数量']) + '#'
            the_price.save()
            # 提取药品信息
            medicine_list = (the_price.药品信息.split('#'))
            all_m = []
            if len(medicine_list) > 1:
                for i in medicine_list:
                    if i:
                        name = i.split('!')[0]
                        num = i.split('!')[1]
                        cost = Medicine.objects.filter(name=name)[0].price
                        m = (name, num, cost)
                        all_m.append(m)
            addform = AddForm()
            return render(request, 'price/medicine.html', {'all_m': all_m, 'number': number, 'addform': addform})


def result(request):
    return render(request, 'price/result.html')


def display(request):

    '''查询单个划价信息'''

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # context中需要num，p_num，total_cost,man,一个药品信息的list
            num = form.cleaned_data['划价编号']
            price = Price.objects.get(划价编号=num)
            p_num = price.病人编号
            man = price.操作人
            li = price.get_medicine_list()
            total_cost = price.get_total_price()
            return render(request, 'price/display.html', {
                'num': num,
                'p_num': p_num,
                'man': man,
                'li': li,
                'total_cost': total_cost,
            })

    else:
        form = SearchForm()
        return render(request, 'price/search.html', {'form': form})