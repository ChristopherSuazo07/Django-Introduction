from django.shortcuts import render

# Create your views here.

def index(request):
    personajes = ["Tanjiro", "Tomioka", "Inosuke", "Zenitsu", "Nezuko", "Tengen"]
    
    return render(request, "personajes/index.html", {
        "personajes": personajes
    })