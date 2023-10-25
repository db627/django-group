from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def pageone(request):
    return render(request, 'pageone.html')

def pagetwo(request):
    return render(request, 'pagetwo.html')