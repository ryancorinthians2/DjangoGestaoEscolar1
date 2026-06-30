from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'gestao/index.html')

def home(request):
    return render(request, 'gestao/home.html')
