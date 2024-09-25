from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.core.checks import messages
from django.db.models import Model, ImageField
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from .forms import UserRegisterForm
from django.contrib import messages
from viewer.models import House, Apartment, Ground, Auction, Image
from logging import getLogger

LOGGER = getLogger()

# Home page view with current and future auctions
def home(request):
    current_auctions = Auction.objects.filter(status='current')
    future_auctions = Auction.objects.filter(status='future')

    context = {
        'current_auctions': current_auctions,
        'future_auctions': future_auctions
    }

    return render(request, "home.html", context)

# House views
def houses(request):
    houses_ = House.objects.all()
    context = {'houses': houses_}
    return render(request, 'houses.html', context)

def house(request, pk):
    if House.objects.filter(id=pk).exists():
        house_ = House.objects.get(id=pk)
        context = {'house': house_}
        return render(request, 'house.html', context)
    return grounds(request)

class HousesListView(ListView):
    template_name = "houses.html"
    model = House
    context_object_name = 'houses'

# Apartment views
def apartments(request):
    apartments_ = Apartment.objects.all()
    context = {'apartments': apartments_}
    return render(request, 'apartments.html', context)

def apartment(request, pk):
    if Apartment.objects.filter(id=pk).exists():
        apartment_ = Apartment.objects.get(id=pk)
        context = {'apartment': apartment_}
        return render(request, 'apartment.html', context)
    return grounds(request)

class ApartmentsListView(ListView):
    template_name = "apartments.html"
    model = Apartment
    context_object_name = 'apartments'

# Ground views
def grounds(request):
    grounds_ = Ground.objects.all()
    context = {'grounds': grounds_}
    return render(request, 'grounds.html', context)

def ground(request, pk):
    if Ground.objects.filter(id=pk).exists():
        ground_ = Ground.objects.get(id=pk)
        context = {'ground': ground_}
        return render(request, 'ground.html', context)
    return grounds(request)

class GroundsListView(ListView):
    template_name = "grounds.html"
    model = Ground
    context_object_name = 'grounds'

# Auction views
def auctions(request):
    auctions_ = Auction.objects.all()
    context = {'auctions': auctions_}
    return render(request, 'auctions.html', context)

def auction(request, pk):
    if Auction.objects.filter(id=pk).exists():
        auction_ = Auction.objects.get(id=pk)
        context = {'auction': auction_}
        return render(request, 'auction.html', context)
    return grounds(request)

class AuctionsListView(ListView):
    template_name = "auctions.html"
    model = Auction
    context_object_name = 'auctions'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Toto uživatelské jméno již existuje, zvolte prosím jiné.')
                return redirect('register')  # Zpět na stránku registrace
            form.save()
            messages.success(request, f'Váš účet byl vytvořen, {username}! Nyní se můžete přihlásit.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})



def login(request):
    return render(request, 'login.html')

