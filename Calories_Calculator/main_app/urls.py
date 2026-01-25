from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('food',views.foods_index, name='foods_index'),
    
    path('meal',views.meals_index, name='meals_index'),
    path('meal/detail',views.meals_detail, name='meals_detail'),

    path('goal',views.goal_detail, name='goal_detail'),
    path('/accounts/signup/',views.signup, name='signup'),

]
