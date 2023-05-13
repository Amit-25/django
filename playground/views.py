from django.shortcuts import render
from django.http import HttpResponse
from store1.models import Product

def hello(request):
    query_set = Product.objects.select_related('collection')[:2]
    print(query_set.query)
    context = {

        "error_code" : "200",
        "error_message" : "Success",
        "msg": "Hello World!!",
        "product":list(query_set)
    }
    # return render(request, 'hello.html', context)
