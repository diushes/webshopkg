from django.urls import path
from .views import *

app_name = "mainpage"

urlpatterns = [
    path("shops/",  ShopsListApiView.as_view()),
    path("mainpage/", shop_list, name="shop_list"),
]