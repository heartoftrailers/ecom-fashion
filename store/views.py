

from django.core import paginator
from django.shortcuts import get_object_or_404, render, get_list_or_404
import carts.models
from category.models import Category
from .models import Product
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def store(request, category_slug=None):
    categories = None 
    products = None

    if category_slug != None: # if there are no categories will return error
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category = categories, is_available = True)
        paginator = Paginator(products, 1 ) # number of items on page
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available= True).order_by('id')
        paginator = Paginator(products, 6 ) # number of items on page
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {
        'products': paged_products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
        in_cart = carts.models.CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists() # __ is for get the cart_id from Cart/models/ class Cart

    except Exception as e:
        raise e
    context = {
        'single_product' : single_product,
        'in_cart' : in_cart,
        }
    return render(request, 'store/product_detail.html', context)