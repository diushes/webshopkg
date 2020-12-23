from django.urls import path
from .views import *

app_name = "mainpage"

urlpatterns = [
    path("shops/",  ShopsListApiView.as_view()),
    path("mainpage/shops/<int:pk>/", Catalog, name="catalog"),
    path("mainpage/", shop_list, name="shop_list"),
    path('mainpage/<int:pk>', ShopsByCategory, name="bycategory")
]