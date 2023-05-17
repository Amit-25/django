from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product, Collection
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        query_set = Product.objects.select_related('collection').all()[:4]
        serializer = ProductSerializer(query_set, many=True)
        context = {
            "data": serializer.data,
            "error_code": 1
        }
        return Response(context)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Data Save Successfully')


@api_view(['GET','PUT','DELETE'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        if serializer is None:
            errorCode, errorMessage = 0, "No Record Found."
        else:
            errorCode, errorMessage = 1, "Data Found"
        context = {
            "data": serializer.data,
            "error_code": errorCode,
            "error_message": errorMessage
        }
        return Response(context)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view()
def collection_detail(request, pk):
    pass

@api_view()
def collection_list(request,pk):
    pass
