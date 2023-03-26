from django.contrib import admin
from Recipes.models import Recipe, Ingredient, Diet

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Diet)
