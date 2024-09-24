from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


def main(request):
    return render(request, 'viewer/main.html')

def login(request):
    return render(request, 'viewer/login.html')

def register(request):
    return render(request, 'viewer/register.html')

def auctions(request):
    return render(request, 'viewer/auctions.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Váš účet byl vytvořen, {username}! Nyní se můžete přihlásit.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'viewer/register.html', {'form': form})