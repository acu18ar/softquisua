from django.shortcuts import render

from .models import Proveedor


def inicio(request):
    """Muestra la lista de proveedores"""
    proveedores = Proveedor.objects.all()
    return render(request, "proveedores/inicio.html", {"proveedores": proveedores})

def crear(request):
    """"Muestra y procesa el formulario para registrar proveedores."""
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        telefono = request.POST.get("telfono", "").strip()

        if nombre:
            Proveedor.objects.create(
                nombre=nombre,
                telefono=telefono,
            )
            return redirect("provedores:inicio")

        return render(request, "proveedores/crear.html", {
            "error": "El nombre o razón social es obligatorio.",
            "nombre": nombre,
            "telefono": telefono,
        })

    return render(request, "proveedores/crear.html")
