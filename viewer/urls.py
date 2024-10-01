from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import InsertAuction
from .views import InsertPropertyType


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('auctions/', views.auctions, name='auctions'),
    path('insert_auction/', InsertAuction.as_view(), name='insert_auction'),
    path('insert_property_type/', InsertPropertyType.as_view(), name='insert_property_type'),

]