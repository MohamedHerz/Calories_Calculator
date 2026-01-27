from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("foods/", views.FoodList.as_view(), name="foods_index"),
    path("foods/<int:pk>/", views.FoodDetail.as_view(), name="foods_detail"),
    path("foods/create/", views.FoodCreate.as_view(), name="foods_create"),
    path("foods/<int:pk>/update/", views.FoodUpdate.as_view(), name="foods_update"),
    path("foods/<int:pk>/delete/", views.FoodDelete.as_view(), name="foods_delete"),
    path("meal", views.meals_index, name="meals_index"),
    path("meal/<int:meal_id>/", views.meals_detail, name="meals_detail"),
    path("meal/create/", views.MealCreate.as_view(), name="meal_create"),
    path("meal/<int:meal_id>/assoc/", views.assoc_food, name="assoc_food"),
    path(
        "meal/<int:meal_id>/unassoc/<int:food_id>/",
        views.unassoc_food,
        name="unassoc_food",
    ),
    path("goal", views.goal_log, name="goal_log"),
    path("/accounts/signup/", views.signup, name="signup"),
]
