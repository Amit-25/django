from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    context = {
        "error_code" : "200",
        "error_message" : "Success",
        "msg": "Hello World!!"
    }
    return render(request, 'hello.html', context)
