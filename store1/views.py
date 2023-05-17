from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Collection
from .serializers import ProductSerializer
# Create your views here.

@api_view()
def product_list(request):
    query_set = Product.objects.select_related('collection').all()[:4]
    serializer = ProductSerializer(query_set, many=True)
    context = {
        "data": serializer.data,
        "error_code": 1
    }
    return Response(context)


@api_view()
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
