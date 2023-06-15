from django.shortcuts import render
from django.conf import settings
import stripe
from cart.cart import Cart 


def payment_view(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        amount = 1000 

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                source=token,
                description='Оплата заказа'
            )

            cart = Cart(request)
            selected_products = cart.get_cart()

            return render(request, 'payment/payment_success.html', {'selected_products': selected_products})

        except stripe.error.CardError as e:
            error_message = e.error.message
            return render(request, 'payment/payment_error.html', {'error_message': error_message})

    return render(request, 'payment/process.html', {'publishable_key': settings.STRIPE_PUBLISHABLE_KEY})


def payment_success(request):
    return render(request, 'payment/payment_error.html')


def payment_error(request):
    return render(request, 'payment/payment_success.html')