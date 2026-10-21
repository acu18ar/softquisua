
from django.urls import path

from . import views

app_name = "productos"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("nuevo/", views.crear, name="crear"),
    path("<int:pk>/editar/", views.editar, name="editar"),
]
