from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    """Форма для добавления товаров в корзину"""
    # coerce=int - приводит значение к типу int
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    # update = True/False - Обновить (True) или Заменить (False) кол-во единиц для товара
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
