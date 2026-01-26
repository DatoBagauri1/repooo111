from django.urls import path
from .views import get_all_products, get_product_detail

urlpatterns = [
    #
    path('api/products/', get_all_products, name='product-list'),
    
    
    path('api/products/<int:pk>/', get_product_detail, name='product-detail'),
]