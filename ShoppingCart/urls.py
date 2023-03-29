from django.urls import path

from ShoppingCart.views import AddItemView, RemoveItemView, \
    RetrieveShoppingCartView, \
    CreateShoppingCartView

urlpatterns = [

    path('get-cart/', RetrieveShoppingCartView),
    path('create-cart/', CreateShoppingCartView.as_view()),
    path('remove/', RemoveItemView),
    path('add/', AddItemView),
]
