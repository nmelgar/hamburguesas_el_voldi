from django.shortcuts import render
from django.http import HttpResponse
from .models import Meal


def menu(request):
    #this line will take all the meals from DB
    meals = Meal.objects
    return render(request, 'menu.html', {'meals':meals})
