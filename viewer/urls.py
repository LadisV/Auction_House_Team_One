from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('auctions/', views.auctions, name='auctions'),
]