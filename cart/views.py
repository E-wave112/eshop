from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.
@require_POST
def cart_add(request, product_id):

    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],override_quantity=cd['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

@cache_page(CACHE_TTL)
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
        'quantity': item['quantity'],
        'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})
