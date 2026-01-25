from django.shortcuts import render,redirect
from .models import *
from django.views.generic.edit import *
from django.views.generic import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class FoodList(LoginRequiredMixin, ListView):
    model = Food
class FoodDetail(LoginRequiredMixin, DetailView):
    model = Food
class FoodCreate(LoginRequiredMixin, CreateView):
    model = Food
    fields = ["food_name", "calories", "fat", "protein","carbs", "image"]
class FoodUpdate(LoginRequiredMixin, UpdateView):
    model = Food
    fields = ["food_name", "calories", "fat", "protein","carbs", "image"]
class FoodDelete(LoginRequiredMixin, DeleteView):
    model = Food
    success_url = "/foods/"


@login_required
def meals_index(request):
    meals = Meal.objects.filter(user=request.user )
    return render(request, "meals/index.html", {"meals": meals})


@login_required
def meals_detail(request, meal_id):
    meal = Meal.objects.get(id=meal_id, user =request.user)
    foods_not_added = Food.objects.exclude(id__in= meal.foods.all().values_list("id"))
    return render(request,"meals/detail.html",
        {
            "meal": meal,
            "foods": foods_not_added,
        })

class MealCreate(LoginRequiredMixin, CreateView):
    model = Meal
    fields = ["name"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MealDelete(LoginRequiredMixin, DeleteView):
    model = Meal
    success_url = "/meals/"



@login_required
def assoc_food(request, meal_id, food_id):
    Meal.objects.get(id=meal_id, user=request.user).foods.add(food_id)
    return redirect("meals_detail", meal_id=meal_id)

@login_required
def unassoc_food(request, meal_id, food_id):
    Meal.objects.get(id=meal_id, user=request.user).foods.remove(food_id)
    return redirect("meals_detail", meal_id=meal_id)



@login_required
def goal_detail(request ):

    goal = Goal.objects.get(user=request.user)
    meals = Meal.objects.filter( user=request.user)
    total_calories = 0

    for meal in meals:
        for food in meal.foods.all():
            total_calories= total_calories+ food.calories


    return render(request ,"goals/detail.html",
        {
            "goal": goal,
            "total_calories": total_calories
        })

class GoalCreate(LoginRequiredMixin, CreateView):
    model = Goal
    fields = ["calories"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
