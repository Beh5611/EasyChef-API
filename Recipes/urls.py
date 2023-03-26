from django.urls import path

from Recipes.views import AccessRecipeView, CreateDietView, \
    CreateIngredientView, \
    CreateRecipeView, \
    DeleteIngredient, DeleteRecipe, DietsView, IngredientsView, RecipesView, \
    UpdateIngredientView, \
    UpdateRecipeView

urlpatterns = [
    path('all/', RecipesView.as_view()),
    path('create/', CreateRecipeView.as_view()),
    path('<int:recipe_id>/ingredients/', IngredientsView.as_view()),
    path('<int:recipe_id>/diets/', DietsView.as_view()),
    path('<int:recipe_id>/add-ingredient/', CreateIngredientView.as_view()),
    path('<int:recipe_id>/add-diet/', CreateDietView.as_view()),
    path('<int:recipe_id>/', AccessRecipeView.as_view()),
    path('<int:recipe_id>/update/', UpdateRecipeView),
    path('<int:id>/update-ingredient/', UpdateIngredientView),
    path('<int:recipe_id>/delete/', DeleteRecipe),
    path('<int:id>/delete-ingredient/', DeleteIngredient)
]
