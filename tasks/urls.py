from django.urls import path
from . import views

app_name = "tasks" #esto ayuda a identificar de forma única todas las URLS, para evitar colisiones de espacio

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
