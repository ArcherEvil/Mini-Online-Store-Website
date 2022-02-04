from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Features, Product
import random, unidecode
# Create your views here.

def index(request):
    features = Features.objects.all()
    products = Product.objects.all()

    list_to_random = []
    for n in products:
        list_to_random.append(n)


    random_list = random.sample(list_to_random, len(products))
    random_list[:20]

    return render(request, 'index.html', {'features': features, 'products': products, 'random': random_list})

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
                if unidecode.unidecode(f.lower()) in unidecode.unidecode(n.name.lower()):
                    if n not in results:
                        results.append(n)
    else:
        search = get
        for n in products:
            if unidecode.unidecode(search.lower()) in unidecode.unidecode(n.name.lower()):
                if n not in results:
                    results.append(n)

    if len(results) == 0:
        return render(request, 'search.html', {'results': results, 'search': get, 'length': 0})
    else:
        return render(request, 'search.html', {'results': results, 'search': get, 'length': len(results)})