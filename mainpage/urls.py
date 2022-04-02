from django.urls import path
from .views import *

app_name = "mainpage"

urlpatterns = [
    path("api/shops/", ShopsListApiView.as_view()),
    path("", shop_list, name="shop_list"),
    path("shops/<int:pk>/", Catalog, name="catalog"),
    path("<int:pk>/", ShopsByCategory, name="bycategory"),
]
