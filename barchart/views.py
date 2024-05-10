from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
# Create your views here.

def index(request):
    data = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'index.html', context)

def linechart(request):
    data = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('linechart')
    else:
        form = ProductForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'linechart.html', context)

def piechart(request):
    data = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('piechart')
    else:
        form = ProductForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'piechart.html', context)
