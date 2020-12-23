from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView
from django.core.paginator import Paginator

class ShopsListApiView(ListAPIView):
    model = Shop
    serializer_class = Shopserializer
    queryset = Shop.objects.all()

def shop_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        shops = Shop.objects.filter(name__icontains=search_query)
    else:
        shops = Shop.objects.all()
    paginator = Paginator(shops, 6)
    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number)


    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page{}'.format(page.next_page_number())
    else:
        next_url = ''


    categories = Category.objects.all()
    context = {
        "shops": page,
        "is_paginated":is_paginated,
        "next_url":next_url,
        "prev_url":prev_url,
        "categories":categories,
    }

    return render(request, "index.html", context=context)


def ShopsByCategory(request, pk):

    search_query = request.GET.get('search', '')
    if search_query:
        shops = Shop.objects.filter(name__icontains=search_query)
    else:
        shops = Shop.objects.filter(category=pk)
    paginator = Paginator(shops, 6)
    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page{}'.format(page.next_page_number())
    else:
        next_url = ''


    categories = Category.objects.all()
    context = {
        "shops": page,
        "is_paginated":is_paginated,
        "next_url":next_url,
        "prev_url":prev_url,
        "categories":categories,
    }

    return render(request, "index.html", context=context)


def Catalog(request, pk):

    search_query = request.GET.get('search', '')
    if search_query:
        shops = Shop.objects.filter(name__icontains=search_query)
    else:
        shops = Shop.objects.all()
    shop = Shop.objects.get(id=pk)
    products = Product.objects.filter(shop=pk)
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number)


    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page{}'.format(page.next_page_number())
    else:
        next_url = ''


    categories = Category.objects.all()
    context = {
        "shop": shop,
        "products": page,
        "is_paginated":is_paginated,
        "next_url":next_url,
        "prev_url":prev_url,
        "categories":categories,
    }

    return render(request, "catalog.html", context=context)
