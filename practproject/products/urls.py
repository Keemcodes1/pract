from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),
    # path('products', views.product_list_view, name='product_list'),
    path('products/<int:pk>/', views.product_detail_view, name='products'),
    path('api/products/<int:id>/', views.product_api_detail_view, name='products_api'),
    path('products/', views.product_list_view, name='product_list')
]