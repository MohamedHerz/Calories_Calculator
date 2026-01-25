from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('food',views.home, name='food_index'),
    path('/accounts/signup/',views.signup, name='signup'),

]
