from django.shortcuts import render


def register(request):
    return render(request, 'registration/register.html')


def search(request):
    return render(request, 'registration/search.html')
