from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

# from django.contrib.auth.models import User
from users.models import User

from .forms import RegisterForm

from products.models import Product

def index(request):

    products = Product.objects.all().order_by('-id')

    return render(request, './index.html', {
        'message': 'Listado de productos',
        'title': 'Productos',
        'products': products
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:
            login(request, user)
            messages.success(request, f'Bienvenido {user.username}')
            return redirect('index')
        else:
            messages.error(request, 'Usuario contraseña no validos')

    return render(request, 'users/login.html', {

    })


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')


def register(request):
    # Generamos un formulario con los datos que el 
    # usuario está enviando
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # Generamos un nuevo usuario
        user = form.save()

        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')


    return render(request, 'users/register.html', {
        'form': form
    })
