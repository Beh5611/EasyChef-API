from rest_framework import serializers

from Recipes.models import Recipe, Diet, Ingredient


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'owner', 'serving', 'step_list', 'prep_time', 'cook_time']


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'recipe_ID', 'amount', 'amount_type']


class DietSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diet
        fields = ['id', 'name', 'recipe_ID']
