from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.

def index(request):
    data = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    context = {
        'data': data
    }
    return render(request, 'index.html', context)
