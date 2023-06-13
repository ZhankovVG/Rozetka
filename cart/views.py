from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from main.models import Category
import stripe
from django.conf import settings


@require_POST
def cart_add(request, product_id):
    # добавление продуктов в корзину
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    # удаление продуктов из корзины
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    # то что находится в корзине
    cart = Cart(request)
    categories = Category.objects.all()
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart, 'categories': categories})


def payment_view(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # Получение информации о платеже из формы
        token = request.POST.get('stripeToken')
        # Сумма оплаты в центах (в данном случае $10)
        amount = 1000

        try:
            # Создание платежа с использованием Stripe API
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                source=token,
                description='Оплата заказа'
            )

            # Оплата прошла успешно
            return render(request, 'payment_success.html')

        except stripe.error.CardError as e:
            # Ошибка при обработке платежа с карты
            error_message = e.error.message
            return render(request, 'payment_error.html', {'error_message': error_message})

    return render(request, 'cart/payment.html', {'publishable_key': settings.STRIPE_PUBLISHABLE_KEY})
