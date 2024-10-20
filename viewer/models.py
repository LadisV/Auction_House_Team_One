from django.core.exceptions import ValidationError
from django.db import models

from django.db.models import Model, CharField, DateTimeField, ForeignKey, SET_NULL, IntegerField, ImageField, TextField

import time

import datetime

import pytz
from django.utils import timezone

from accounts.models import Profile


class Cities(Model):
    name = CharField(max_length=20, null=False)

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['name']

    def clean(self):
        if not self.name[0].isupper():
            raise ValidationError({
                'name': ('Město je s velkým počátečním písmenem.')
            })

    def __repr__(self):
        return f"City(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class HouseType(Model):
    property_type = CharField(max_length=15, null=False)

    class Meta:
        ordering = ['property_type']

    def __repr__(self):
        return f"HouseType(name={self.property_type})"

    def __str__(self):
        return f"{self.property_type}"


class GroundType(Model):
    property_type = CharField(max_length=30, null=False)

    class Meta:
        ordering = ['property_type']

    def __repr__(self):
        return f"GroundType(name={self.property_type})"

    def __str__(self):
        return f"{self.property_type}"


class ApartmentType(Model):
    property_type = CharField(max_length=30, null=False)

    class Meta:
        ordering = ['property_type']

    def __repr__(self):
        return f"ApartmentType(name={self.property_type})"

    def __str__(self):
        return f"{self.property_type}"


class House(Model):
    name = CharField(max_length=150, null=False)
    area = IntegerField(null=True, blank=True)
    property_type = ForeignKey(HouseType, null=True, blank=True, on_delete=SET_NULL, related_name='houses')
    plot_area = IntegerField(null=True, blank=True)
    garden_area = IntegerField(null=True, blank=True)
    description = TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"House(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class Ground(Model):
    name = CharField(max_length=150)
    property_type = ForeignKey(GroundType, null=True, blank=True, on_delete=SET_NULL, related_name='grounds')
    property_area = IntegerField(null=False)
    description = TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Ground(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class Apartment(Model):
    name = CharField(max_length=150, null=False)
    property_type = ForeignKey(ApartmentType, null=True, blank=True, on_delete=SET_NULL, related_name='apartments')
    area = IntegerField(null=False)
    description = TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return f"Apartment(name={self.name})"

    def __str__(self):
        return f"{self.name}"


class PropertyType(Model):
    house = ForeignKey(House, null=True, blank=True, on_delete=SET_NULL, related_name='house')
    ground = ForeignKey(Ground, null=True, blank=True, on_delete=SET_NULL, related_name='ground')
    apartment = ForeignKey(Apartment, null=True, blank=True, on_delete=SET_NULL, related_name='apartment')

    def clean(self):
        if self.house == None and self.ground == None and self.apartment == None:
            raise ValidationError({
                'house': ('Nezadali jste nemovitost.'),
                'ground': ('Nezadali jste nemovitost.'),
                'apartment': ('Nezadali jste nemovitost.'),
            })
        if self.house == None and self.ground and self.apartment:
            raise ValidationError({
                'ground': ('Zadali jste více nemovitostí.'),
                'apartment': ('Zadali jste více nemovitostí.'),
            })
        if self.ground == None and self.apartment and self.house:
            raise ValidationError({
                'house': ('Zadali jste více nemovitostí.'),
                'apartment': ('Zadali jste více nemovitostí.'),
            })
        if self.apartment == None and self.house and self.ground:
            raise ValidationError({
                'ground': ('Zadali jste více nemovitostí.'),
                'house': ('Zadali jste více nemovitostí.'),
            })
        if self.apartment and self.house and self.ground:
            raise ValidationError({
                'ground': ('Zadali jste více nemovitostí.'),
                'house': ('Zadali jste více nemovitostí.'),
                'apartment': ('Zadali jste více nemovitostí.'),
            })
    def __str__(self):
        if self.house:
            return str(self.house)
        elif self.ground:
            return str(self.ground)
        elif self.apartment:
            return str(self.apartment)
        return "Nedefinováno"


class Auction(Model):
    property_type = ForeignKey(PropertyType, null=True, blank=True, on_delete=SET_NULL, related_name='auction')
    city = ForeignKey(Cities, null=True, blank=True, on_delete=SET_NULL, related_name='city')
    location = CharField(max_length=50, null=False)
    estimate_value = IntegerField(null=False)
    min_value = IntegerField(null=False)
    act_value = IntegerField(null=True, blank=True)
    auction_assurance = IntegerField(null=False)
    min_bid = IntegerField(null=True, blank=False)
    date_auction = DateTimeField(null=False)
    date_end_auction = DateTimeField(null=False)
    description = TextField(null=True, blank=True)
    image = ImageField(upload_to='images/', blank=True, null=True)

    def clean(self):
        if self.date_auction > self.date_end_auction:
            raise ValidationError({
                'date_auction': ('Začátek dražby nesmí být po jejím konci.'),
                'date_end_auction': ('Konec dražby nesmí být před začátkem.'),
            })
        if self.min_bid > self.estimate_value or self.min_bid > self.min_value:
            raise ValidationError({
                'min_bid': ('Hodnota je příliš velká.'),
            })
        if self.min_value > self.estimate_value:
            raise ValidationError({
                'min_value': ('Hodnota je příliš velká.'),
                'estimate_value': ('Hodnota je příliš velká.')
            })
        if self.auction_assurance > self.estimate_value:
            raise ValidationError({
                'auction_assurance': ('Hodnota je příliš velká.'),
                'estimate_value': ('Hodnota je příliš velká.')
            })

    def loc_time(self):
        local = time.localtime()
        return f"{local[2]}.{local[1]}.{local[0]} {local[3]}:{local[4]}"

    def time_to(self):
            then = self.date_auction.replace(tzinfo=pytz.utc)
            now = datetime.datetime.now().replace(tzinfo=pytz.utc)
            time_difference = then - now
            return time_difference

    def time_of(self):
        now = datetime.datetime.now().replace(tzinfo=pytz.utc)
        then = self.date_end_auction.replace(tzinfo=pytz.utc)
        result = then - now
        if now < then:
            return result
        else:
            return "Konec"

    def difference(self):
        now = datetime.datetime.now().replace(tzinfo=pytz.utc)
        then = self.date_end_auction.replace(tzinfo=pytz.utc)
        result = then - now
        if now < then:
            return result
        else:
            return "Konec"

    def in_progress(self):
        auction_start = self.date_auction.replace(tzinfo=pytz.utc)
        actual_time = timezone.now().replace(tzinfo=pytz.utc)
        auction_end = self.date_end_auction.replace(tzinfo=pytz.utc)
        if actual_time > auction_start and actual_time < auction_end:
            return True
        else:
            return False

    def isnot_start(self):
        auction_start = self.date_auction.replace(tzinfo=pytz.utc)
        actual_time = timezone.now().replace(tzinfo=pytz.utc)
        if actual_time < auction_start:
            return True
        else:
            return False

    def end(self):
        actual_time = timezone.now().replace(tzinfo=pytz.utc)
        auction_end = self.date_end_auction.replace(tzinfo=pytz.utc)
        if actual_time > auction_end:
            return True
        else:
            return False

    class Meta:
        verbose_name_plural = "Auctions"

    def __repr__(self):
        return f"Auction(name={self.property_type}, {self.location})"

    def __str__(self):
        return f"{self.property_type} ({self.location})"


class Bid(Model):
    auction = ForeignKey(Auction, null=True, blank=True, on_delete=models.CASCADE, related_name='bid')
    user = ForeignKey(Profile, null=True, blank=True, on_delete=SET_NULL, related_name='bid')
    bid_amount = IntegerField(null=False)
    created = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def save(self, *args, **kwargs):
        self.clean()
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if self.auction.act_value is None:
            self.auction.act_value = self.auction.min_value
            self.auction.save()
        if is_new:
            self.auction.act_value = int(self.auction.act_value) + int(self.bid_amount)
            self.auction.save()
            time = self.auction.date_end_auction.replace(tzinfo=pytz.utc) - datetime.datetime.now().replace(tzinfo=pytz.utc)
            if time.total_seconds() < 300 and time.total_seconds() >= 240:
                self.auction.date_end_auction = self.auction.date_end_auction + datetime.timedelta(minutes=1)
                self.auction.save()
            elif time.total_seconds() < 240 and time.total_seconds() >= 180:
                self.auction.date_end_auction = self.auction.date_end_auction + datetime.timedelta(minutes=2)
                self.auction.save()
            elif time.total_seconds() < 180 and time.total_seconds() >= 120:
                self.auction.date_end_auction = self.auction.date_end_auction + datetime.timedelta(minutes=3)
                self.auction.save()
            elif time.total_seconds() < 120 and time.total_seconds() >= 60:
                self.auction.date_end_auction = self.auction.date_end_auction + datetime.timedelta(minutes=4)
                self.auction.save()
            elif time.total_seconds() < 60 and time.total_seconds() >= 0:
                self.auction.date_end_auction = self.auction.date_end_auction + datetime.timedelta(minutes=5)
                self.auction.save()

    def __str__(self):
        return f"{self.user}"

    def anonymization_name(self):
        name = self.user.user.username
        if len(name) <= 2:
            return name
        else:
            return name[0] + '*' * (len(name) - 2) + name[-1]


class Image(Model):
    image = ImageField(upload_to='images/', default=None, null=False, blank=False)
    house = ForeignKey(House, on_delete=SET_NULL, null=True, blank=True, related_name='images')
    apartment = ForeignKey(Apartment, on_delete=SET_NULL, null=True, blank=True, related_name='images')
    ground = ForeignKey(Ground, on_delete=SET_NULL, null=True, blank=True, related_name='images')
    auctions = ForeignKey(Auction, on_delete=SET_NULL, null=True ,blank=True, related_name='images')
    description = TextField(null=True, blank=True)

    def __repr__(self):
        return f"Image(image={self.image}, auctions={self.auctions}, description={self.description})"

    def __str__(self):
        return f"Image: {self.image}, {self.description}"

