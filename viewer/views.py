import self
from django.contrib import messages
from datetime import datetime, tzinfo
from lib2to3.fixes.fix_input import context

import pytz
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Model, ImageField
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView

from . import models
from .forms import UserRegisterForm
from viewer.forms import ApartmentModelForm, AuctionModelForm, ImageModelForm, PropertyTypeModelForm, GroundModelForm, \
    HouseModelForm

from accounts.models import Profile
from viewer.forms import ImageModelForm, BidModelForm
from viewer.models import House, Apartment, Ground, Auction, Image, Bid, PropertyType
#from viewer.forms import ImageModelForm
from viewer.forms import ImageModelForm, ApartmentModelForm, GroundModelForm, HouseModelForm, AuctionModelForm, PropertyTypeModelForm

from viewer.models import House, Apartment, Ground, Auction, Image
from viewer.forms import ImageModelForm
from logging import getLogger
from .forms import ApartmentModelForm

LOGGER = getLogger()


def home(request):
    auctions = Auction.objects.all()
    context = {
        'auctions': auctions
    }
    return render(request, 'home.html', context)


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


class HousesView(View):
    def get(self, request):
        houses_ = House.objects.all()
        context = {'houses': houses_}
        return render(request, "houses.html", context)


class HousesTemplateView(TemplateView):
    template_name = "houses.html"
    extra_context = {'houses': House.objects.all()}


class HousesListView(ListView):
    template_name = "houses.html"
    model = House
    context_object_name = 'houses'

def apartments(request):
    apartments_ = Apartment.objects.all()
    context = {'apartments': apartments_}
    return render(request, 'apartments.html', context)


def insert_data(request):
    return render(request, "insert_data.html")


class InsertHouse(CreateView):
    template_name = 'form.html'
    form_class = HouseModelForm
    success_url = reverse_lazy('insert_property_type')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)


class UpdateHouse(UpdateView):
    template_name = 'form.html'
    form_class = HouseModelForm
    success_url = reverse_lazy('houses')
    model = House

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class DeleteHouse(DeleteView):
    template_name = 'creator_confirm_delete.html'
    model = House
    success_url = reverse_lazy('houses')


class InsertApartments(CreateView):
    template_name = "form.html"
    form_class = ApartmentModelForm
    success_url = reverse_lazy('insert_property_type')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class UpdateApartments(UpdateView):
    template_name = 'form.html'
    form_class = ApartmentModelForm
    success_url = reverse_lazy('apartments')
    model = Apartment

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class DeleteApartments(DeleteView):
    template_name = 'creator_confirm_delete.html'
    model = Apartment
    success_url = reverse_lazy('apartments')


class InsertGrounds(CreateView):
    template_name = "form.html"
    form_class = GroundModelForm
    success_url = reverse_lazy('insert_property_type')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class UpdateGrounds(UpdateView):
    template_name = 'form.html'
    form_class = GroundModelForm
    success_url = reverse_lazy('grounds')
    model = Ground

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class DeleteGrounds(DeleteView):
    template_name = 'creator_confirm_delete.html'
    model = Ground
    success_url = reverse_lazy('grounds')


class InsertPropertytype(CreateView):
    template_name = "form.html"
    form_class = PropertyTypeModelForm
    success_url = reverse_lazy('insert_auction')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)


class InsertAuction(CreateView):
    template_name = "form.html"
    form_class = AuctionModelForm
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class UpdateAuction(UpdateView):
    template_name = 'form.html'
    form_class = AuctionModelForm
    success_url = reverse_lazy('auctions')
    model = Auction

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

class DeleteAuction(DeleteView):
    template_name = 'creator_confirm_delete.html'
    model = Auction
    success_url = reverse_lazy('auctions')

class InsertBid(CreateView):
    template_name = "auction.html"
    form_class = BidModelForm
    success_url = reverse_lazy('auction')

    def form_invalid(self, form):
        LOGGER.warning('User providet invalit data updating.')
        return super().form_invalid(form)

def apartment(request, pk):
    if Apartment.objects.filter(id=pk).exists():
        apartment_ = Apartment.objects.get(id=pk)
        context = {'apartment': apartment_}
        return render(request, 'apartment.html', context)
    return grounds(request)


class ApartmentsView(View):
    def get(self, request):
        apartments_ = Apartment.objects.all()
        context = {'apartments': apartments_}
        return render(request, "apartments.html", context)


class ApartmentsTemplateView(TemplateView):
    template_name = "apartments.html"
    extra_context = {'apartments': Apartment.objects.all()}


class ApartmentsListView(ListView):
    template_name = "apartments.html"
    model = Apartment
    context_object_name = 'apartments'


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


class GroundsView(View):
    def get(self, request):
        grounds_ = Ground.objects.all()
        context = {'grounds': grounds_}
        return render(request, "grounds.html", context)


class GroundsTemplateView(TemplateView):
    template_name = "grounds.html"
    extra_context = {'grounds': Ground.objects.all()}


class GroundsListView(ListView):
    template_name = "grounds.html"
    model = Ground
    context_object_name = 'grounds'


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


class AuctionView(View):
    def get(self, request):
        auctions_ = Auction.objects.all()
        context = {'auctions': auctions_}
        return render(request, "auctions.html", context)


class AuctionsTemplateView(TemplateView):
    template_name = "auctions.html"
    extra_context = {'auctions': Auction.objects.all()}


class AuctionsListView(ListView):
    template_name = "auctions.html"
    model = Auction
    context_object_name = 'auctions'

class AuctionTemplateView(TemplateView):
    template_name = 'auction.html'



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Toto uživatelské jméno již existuje, zvolte prosím jiné.')
            else:
                form.save()
                messages.success(request, f'Váš účet byl vytvořen, {username}! Nyní se můžete přihlásit.')
                return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})



    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class ImageUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form_image.html'
    form_class = ImageModelForm
    success_url = reverse_lazy('images')
    model = Image
    permission_required = 'viewer.change_image'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating a creator.')
        return super().form_invalid(form)


class ImageDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Image
    success_url = reverse_lazy('images')
    permission_required = 'viewer.delete_image'


class ImageDetailView(DetailView):
    model = Image
    template_name = 'image.html'


class ImagesListView(ListView):
    template_name = "images.html"
    model = Image
    context_object_name = 'images'


class ImageCreateView(CreateView):
    template_name = 'form_image.html'
    form_class = ImageModelForm
    model = Image

    def success_url(self):
        reverse_lazy('image_detail', kwargs={'pk': self.object.pk})


class InsertPropertyType(CreateView):
    model = PropertyType
    template_name = 'insert_property_type.html'
    fields = '__all__'
    success_url = '/'

def insert_auction_view(request):
    form = AuctionModelForm()
    if request.method == 'POST':
        form = AuctionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'insert_auction.html', {'form': form})


def auction_detail(request, pk):
    auction = get_object_or_404(Auction, pk=pk)

    context = {
        'auction': auction
    }

    return render(request, 'auction_detail.html', context)