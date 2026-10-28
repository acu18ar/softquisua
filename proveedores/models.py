from django.db import models


class Proveedor(models.Model):
    # ── CAMPOS BASE ─────────────────────────────────────────────────────────
    nombre = models.CharField("nombre o razón social", max_length=150)
    telefono = models.CharField("teléfono", max_length=30, blank=True)

        # Nuevos datos del proveedor.
    nit = models.CharField("NIT", max_length=20, blank=True, default="")
    correo = models.EmailField("correo electrónico", blank=True, default="")

    # Relación con los productos que suministra.
    productos = models.ManyToManyField(
        "productos.Producto",
        blank=True,
        related_name="proveedores",
        verbose_name="productos que suministra",
    )
    class Meta:
        ordering = ["nombre"]
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"

    def __str__(self):
        return self.nombre
