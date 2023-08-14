from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def All_ProdCat(request, c_slug=None):
    c_page = None
    products_list = None
    categories = Category.objects.all()

    if c_slug:
        c_page = get_object_or_404(Category, slug=c_slug)
        products_list = Product.objects.filter(category=c_page, available=True)
    else:
        products_list = Product.objects.filter(available=True)

    paginator = Paginator(products_list, 8)
    page_number = request.GET.get('page', 1)

    try:
        products = paginator.page(page_number)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, "category.html", {'category': c_page, 'products': products, 'categories': categories})

def Pro_Detail(request, c_slug, product_slug):
    product = get_object_or_404(Product, category__slug=c_slug, slug=product_slug)
    return render(request, 'product.html', {'product': product})
