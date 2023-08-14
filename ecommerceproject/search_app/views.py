from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

def Search_Result(request):
    products = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.filter(Q(name__contains=query) | Q(desc__contains=query))

    return render(request, 'search.html', {'query': query, 'products': products})
