from django.contrib import admin

from.models import Meal

@admin.register(Meal)
class mealAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']