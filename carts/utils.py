from .models import Cart
from products.models import Product

from django.shortcuts import get_object_or_404

def  get_or_create_cart(request):
    # Para crear una sesion
    # Diccionario de la sesion
    # request.session['cart_id'] = '123'

    # Para obtener el valor de una sesion
    # valor = request.session.get('cart_id')
    # print(f'Valor de la sesion: {valor}')

    # Para eliminar una sesion
    # request.session['cart_id'] = None

    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    # print(cart_id)
    cart = Cart.objects.filter(cart_id=cart_id).first()

    if cart is None:
        cart = Cart.objects.create(user=user)

    if user and cart.user is None:
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id

    return cart

