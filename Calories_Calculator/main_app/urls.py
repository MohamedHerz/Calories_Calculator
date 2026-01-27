from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('foods/', views.FoodList.as_view(), name='foods_index'),
    path('foods/<int:pk>/', views.FoodDetail.as_view(),name='foods_detail'),
    path('foods/create/',views.FoodCreate.as_view(), name='foods_create'),
    path('foods/<int:pk>/update/', views.FoodUpdate.as_view(),name='foods_update'),
    path('foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'),

    path('meal',views.meals_index, name='meals_index'),
    path('meal/detail',views.meals_detail, name='meals_detail'),

    path('goal',views.goal_detail, name='goal_detail'),
    path('/accounts/signup/',views.signup, name='signup'),

]
