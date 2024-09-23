from django.shortcuts import render
from django.template.context_processors import request

def main(request):
    return render(request, 'viewer/main.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def auctions(request):
    return render(request, 'auctions.html')