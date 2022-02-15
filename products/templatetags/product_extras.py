from django import template

# Para registrar nuestras funciones
register = template.Library()

@register.filter()
def price_format(value):
    return '${0:.2f}'.format(value)