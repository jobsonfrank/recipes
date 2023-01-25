from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
# HTTP RESPONSE

def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Jobson Frank'})

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request,'contato.html')

def receitas(request):
    return render(request, 'recipes/pages/receitas.html', context={'name': 'Jobson Frank'})
# Create your views here.
