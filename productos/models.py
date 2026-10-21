
from django.db import models


class Producto(models.Model):
    # Campos base: no cambiar sus nombres.
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField("precio (Bs)", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    imagen = models.ImageField(
    upload_to="productos/",
    blank=True,
    null=True
)

    # Campos nuevos solicitados en el backlog.
    codigo = models.CharField(max_length=50, blank=True, default="")
    stock_minimo = models.PositiveIntegerField(default=5)




    class Meta:
        ordering = ["nombre"]
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.nombre
