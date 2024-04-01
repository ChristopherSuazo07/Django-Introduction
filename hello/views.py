from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, "hello/index.html")
    
def brian(request):
    return HttpResponse("Hello, Brian!")

def gema(request):
    return HttpResponse("Hi, Honey!")

# def saludar(request, name):
#     return HttpResponse(f"Hola, {name}!")

#renderizando html
def saludo(request, nombre):
    return render(request,"hello/index.html",{
        "name": nombre
    })
    