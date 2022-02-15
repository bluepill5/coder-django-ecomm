from unicodedata import name
from django.urls import path

from . import views

# Al hacer esto indicamos que las rutas le corresponde a 
# 'products'
app_name = 'products'

urlpatterns = [
    path('search', views.ProductSearchListView.as_view(), name='search'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product'), # id -> llave primaria
]


