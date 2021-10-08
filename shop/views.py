from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    """Список товаров, либо отфильтрованный список товаров"""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    # если в url указан category_slug, фильтруем товар по категории
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    """Страница каждого товара с подробным описанием

    slug в url позволяет генерировать хорошие с точки зрения SEO ссылки,
    что улучшает индексацию сайта поисковыми роботами
    """
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
