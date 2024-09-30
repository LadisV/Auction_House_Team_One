from django.forms import Form, CharField, ModelChoiceField, IntegerField, DateField, ModelForm, NumberInput

from viewer.models import House, HouseType, GroundType, ApartmentType, Cities, PropertyType, House, Ground, Apartment, Auction, \
    Image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class HouseModelForm(ModelForm):
    class Meta:
        model = House
        fields = '__all__'

class ApartmentModelForm(ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'

class GroundModelForm(ModelForm):
    class Meta:
        model = Ground
        fields = '__all__'

class PropertyTypeModelForm(ModelForm):
    class Meta:
        model = PropertyType
        fields = '__all__'

class AuctionModelForm(ModelForm):
    class Meta:
        model = Auction
        fields = '__all__'

    #date_auction = DateField(required=False, widget=NumberInput(attrs={'type': 'date'}))

class ImageModelForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']