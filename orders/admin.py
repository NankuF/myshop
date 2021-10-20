from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """
    Мы используем класс ModelInline для модели OrderItem, чтобы добавить ее
    в виде списка связанных объектов на страницу заказа, зарегистрированную
    через OrderAdmin. Так администратор сможет редактировать данные
    по каждому товару напрямую со страницы заказа.
    """
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code',
                    'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]  # список связанных объектов
