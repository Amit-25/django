from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('product_detail/<int:pk>/', views.product_detail),
    path('collections/', views.collection_list),
    path('collection_detail/<int:pk>/', views.collection_detail)
]