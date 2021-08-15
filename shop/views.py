from django.shortcuts import render, get_object_or_404
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings
from .models import Product, Category
from cart.forms import CartAddProductForm

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here and use the cache decorate in specific views
@cache_page(CACHE_TTL)
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        if len(products) == 0:
            products = 'no products found in this category'
    return render(request,
        'shop/product/list.html',
        {'category': category,
        'categories': categories,
        'products': products})


@cache_page(CACHE_TTL)
def product_detail(request, id, slug):

    product = get_object_or_404(Product,
    id=id,
    slug=slug,
    available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
    'shop/product/detail.html',
    {'product': product,'cart_product_form':cart_product_form})