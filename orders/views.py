from django.shortcuts import render, redirect
from django.urls import reverse

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created


def order_create(request):
    # Получаем объект корзины
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            # Записываем новый заказ в БД
            order = form.save()
            # Проходим по всем товарам корзины и создаем для каждого объект OrderItem
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # Очищаем корзину
            cart.clear()
            # Запуск асинхронной задачи
            order_created.delay(order.id)
            # Сохранение заказа в сессии
            request.session['order_id'] = order.id
            # Перенаправление на страницу оплаты
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
