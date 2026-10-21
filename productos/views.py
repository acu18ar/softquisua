
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


def inicio(request):
    productos = Producto.objects.all()
    return render(request, "productos/inicio.html", {"productos": productos})


def crear(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto registrado correctamente.")
            return redirect("productos:inicio")
    else:
        form = ProductoForm()

    return render(request, "productos/formulario.html", {
        "form": form,
        "titulo": "Nuevo producto",
    })


def editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        form = ProductoForm(
            request.POST,
            request.FILES,
            instance=producto,
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado correctamente.")
            return redirect("productos:inicio")
    else:
        form = ProductoForm(instance=producto)

    return render(request, "productos/formulario.html", {
        "form": form,
        "titulo": "Editar producto",
    })
