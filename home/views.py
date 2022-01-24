from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Features
# Create your views here.

def index(request):
    features = Features.objects.all()
    return render(request, 'index.html', {'features': features})

