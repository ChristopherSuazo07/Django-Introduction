from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("brian", views.brian, name="brian"),
    path("gema", views.gema, name="gema"),
    # path("<str:name>", views.saludar, name="saludar"),
    path("<str:nombre>", views.saludo, name="html"),
]
