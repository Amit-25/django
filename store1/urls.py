from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('product_details/<int:pk>/', views.product_detail)
]