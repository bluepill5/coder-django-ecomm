from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# El ultima instanci para crear nuestro propio modelo podemos sobreescribir
# AbstractUser o AbstractBaseUser -> difieren en atributos

# AbstractUser
# username
# first_name
# last_name
# email
# password
# groups
# user_permissions
# is_staff
# is_active
# is_superuser
# last_login
# date_joined

# AbstractBaseUser
# id
# password
# last_login

class User(AbstractUser):
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


# Proxy model: Un modelo que hereda de otro
# el modelo no generara una nueva tabla
class Customer(User):
    class Meta:
        proxy = True

    def get_products(self):
        # Retornara los productos del cliente
        return []


# Para agregar nuevas propiedades a nuestro modelo
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()





