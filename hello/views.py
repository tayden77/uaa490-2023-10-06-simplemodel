from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")

def marc0(request):
    return HttpResponse("Hello, Marc!")

def marc(request):
    return render(request, "hello/marc.html")

def uaa490(request):
    return HttpResponse("Hello, Class!")

def greet0(request, name):
    return HttpResponse(f'<h1>Greetings, {name.capitalize()}!!</h1><p>This space is available for a small fee</p>')

def greet(request, name):
    n = name.capitalize()
    return render(request, 'hello/greet.html', {"name": n})