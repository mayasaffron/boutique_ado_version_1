from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "the bag is empty, keep shopping!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IFjjIIPA0UV9eVp4bqR4o9gSIiRfGDzBpzMvO3JC0oKyyKa3gfDF34xcuIQCtRGwDIh5AAg2ms6iM0Ny1O4cxxg00iwEX8n1h',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
