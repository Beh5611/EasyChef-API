# from django.http import JsonResponse, QueryDict
# from django.shortcuts import render
#
# # Create your views here.
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.generics import CreateAPIView, ListAPIView, get_object_or_404, RetrieveAPIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.utils import json
# from rest_framework.views import APIView
#
# from Recipes.models import Recipe, Ingredient
# from ShoppingCart.models import ShoppingCart
# from ShoppingCart.serializers import ShoppingSerializer
#
# #
# class CreateShoppingCartView(CreateAPIView):
#     # authentication_classes = [authentication.SessionAuthentication]
#     # permission_classes = [permissions.IsAuthenticated]
#     serializer_class = ShoppingSerializer
#
#     def create(self, request, *args, **kwargs):
#         data = QueryDict('', mutable=True)
#         data['owner'] = self.request.user.id
#         data.update(request.data)
#         serializer = self.get_serializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED,
#                         headers=headers)
#
#
#
#
# @csrf_exempt
# @api_view(['POST'])
# # @authentication_classes([SessionAuthentication])
# # @permission_classes([IsAuthenticated])
# def RetrieveShoppingCartView(request, *args, **kwargs):
#
#     r = Recipe.objects.filter(owner=kwargs['id'])
#
#     totRecipe = {}
#     lst_recipe = []
#
#     for i in r:
#         Re = {}
#         Re["name"] = i.name
#         Re["cuisine"] = i.cuisine
#         Re["serving"] = i.serving
#         # Re["step_list"] = list(i.step_list.all())
#         lst_steps = []
#         for k in list(i.step_list.all()):
#             st = {}
#             st["number"] = k.number
#             # st["image"] = k.image
#             st["description"] = k.description
#             lst_steps.append(st)
#         Re["prep_time"] = i.prep_time
#
#         Re["cook_time"] = i.cook_time
#
#         ing = Ingredient.objects.filter(recipe_ID=i.id)
#         lst_ing = []
#         for j in ing:
#             Ingredients = {}
#             Ingredients["name"] = j.name
#             Ingredients["amount"] = j.amount
#             Ingredients["amount_type"] = j.amount_type
#             lst_ing.append(Ingredients)
#         Re["ingredients"] = lst_ing
#         Re["step_list"] = lst_steps
#         lst_recipe.append(Re)
#
#     totRecipe["Recipes"] = lst_recipe
#     print(totRecipe)
#     return JsonResponse(totRecipe,
#                         safe=False
#     )
#
#
#
#     # if request.method == 'POST':
#
#             # if name := request.POST.get('name', None):
#             #     r.name = name
#             #     jresponse['name'] = name
#             # if cuisine := request.POST.get('cuisine', None):
#             #     r.cuisine = cuisine
#             #     jresponse['cuisine'] = cuisine
#             # if serving := request.POST.get('serving', None):
#             #     r.serving = serving
#             #     jresponse['serving'] = serving
#             # if step_list := request.POST.get('step_list', None):
#             #     r.step_list = step_list
#             #     jresponse['step_list'] = step_list
#             # if prep_time := request.POST.get('prep_time', None):
#             #     r.prep_time = prep_time
#             #     jresponse['prep_time'] = prep_time
#             # if cook_time := request.POST.get('cook_time', None):
#             #     r.cook_time = cook_time
#             #     jresponse['cook_time'] = cook_time
#
#     # r.save()
#
