from django.shortcuts import render
from django.http import HttpResponse

def simple_view(request):
    return render(request, 'testapp/index.html') #.html

def hello_view(request):
    return HttpResponse("Hello, Django!")