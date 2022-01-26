from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Features, Product
# Create your views here.

def index(request):
    features = Features.objects.all()
    products = Product.objects.all()
    pagination = False

    if len(products) >= 30:
        pagination = True
    return render(request, 'index.html', {'features': features, 'products': products, 'pagination': pagination})