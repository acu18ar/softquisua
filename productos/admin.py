
from django.contrib import admin

from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["codigo", "nombre", "precio", "stock", "stock_minimo"]
    search_fields = ["nombre", "codigo"]
    list_filter = ["stock_minimo"]
