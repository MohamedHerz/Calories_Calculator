from django.shortcuts import render, redirect
from .models import *
from django.views.generic.edit import *
from django.views.generic import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from django.core.paginator import Paginator
from datetime import date

# Create your views here.


def home(request):
    return render(request, "home.html")


class FoodList(LoginRequiredMixin, ListView):
    model = Food
    paginate_by = 4

class FoodDetail(LoginRequiredMixin, DetailView):
    model = Food
class FoodCreate(LoginRequiredMixin, CreateView):
    model = Food
    fields = ["food_name", "calories", "fat", "protein", "carbs", "image"]
class FoodUpdate(LoginRequiredMixin, UpdateView):
    model = Food
    fields = ["food_name", "calories", "fat", "protein", "carbs", "image"]
class FoodDelete(LoginRequiredMixin, DeleteView):
    model = Food
    success_url = "/foods/"


@login_required
def meals_index(request):
    today = date.today()
    meals = Meal.objects.filter(user=request.user, date=today)
    return render(request, "meals/meals_index.html", {"meals": meals})


@login_required
def meals_detail(request, meal_id):
    meal = Meal.objects.get(id=meal_id, user=request.user)

    current_foods = []
    total_calories = 0
    for food in meal.foods.all():
        weight = 100
        cal = food.calories * weight / 100
        total_calories= total_calories + cal
        current_foods.append({"food": food, "weight": weight, "calories": cal})
# weight is defaulted to 100 need to provide option to submit weight later
    foods_not_added = Food.objects.exclude(id__in=meal.foods.all().values_list("id"))
    return render(
        request,
        "meals/meals_detail.html",
        {
            "meal": meal,
            "current_foods": current_foods,
            "total_calories": total_calories,
            "foods_not_added": foods_not_added,
        },
    )


class MealCreate(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ["name"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.date = date.today()
        return super().form_valid(form)

    success_url = "/meal"


class MealDelete(LoginRequiredMixin, DeleteView):
    model = Meal
    success_url = "/meals/"


@login_required
def assoc_food(request, meal_id):
    food_id = request.POST["food_id"]
    Meal.objects.get(id=meal_id, user=request.user).foods.add(food_id)
    return redirect("meals_detail", meal_id=meal_id)


@login_required
def unassoc_food(request, meal_id, food_id):
    Meal.objects.get(id=meal_id, user=request.user).foods.remove(food_id)
    return redirect("meals_detail", meal_id=meal_id)


@login_required
def goal_log(request):
    goal = Goal.objects.get(user=request.user)

    if request.method == "POST":
        goal.calories =(request.POST["calories"])
        goal.save()

    meals = Meal.objects.filter(user=request.user).order_by('-date')

    daily_total = {}
    for meal in meals:
        total_cal = 0
        for food in meal.foods.all():
            total_cal = total_cal + food.calories
        daily_total[meal.date] = total_cal

    return render(request, "goal/goal_log.html",
                {
        "goal": goal,
        "daily_total": daily_total})


def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
        else:
            error_message = "Invalid sign up - try again"
    form = UserCreationForm()
    context = {"form": form, "error_message": error_message}
    return render(request, "registration/signup.html", context)
