from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Features, Product
# Create your views here.

def index(request):
    features = Features.objects.all()
    products = Product.objects.all()

    return render(request, 'index.html', {'features': features, 'products': products})

def product(request, pk):
    product = Product.objects.get(ids=pk)

    return render(request, 'product.html', {'product': product})

def search(request):
    get = request.GET['searchquery']
    products = Product.objects.all()
    results = []
    if ' ' in get:
        search = get.split(' ')
        for f in search:
            for n in products:
                if f.lower() in n.name.lower():
                    if n not in results:
                        results.append(n)
    else:
        search = get
        for n in products:
            if search.lower() in n.name.lower():
                if n not in results:
                    results.append(n)


    return render(request, 'search.html', {'results': results, 'search': get})