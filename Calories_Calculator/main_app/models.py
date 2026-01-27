from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


class Food(models.Model):
    food_name = models.CharField(max_length=50)
    calories = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    image = models.ImageField(upload_to="main_app/static/images", default="")

    def __str__(self):
        return self.food_name

    def get_absolute_url(self):
        return reverse("foods_detail", kwargs={"pk": self.id})


class Meal(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    foods = models.ManyToManyField(Food)

    def __str__(self):
        return self.name


class Goal(models.Model):
    calories = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.calories)
