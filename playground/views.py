from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# A view takes in a request and returns a response (Reqeust handler)

def say_hello(request):
    return HttpResponse('Hello World')