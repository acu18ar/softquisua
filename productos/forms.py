
from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["codigo", "nombre", "precio", "stock", "stock_minimo"]
        widgets = {
            "codigo": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ej. FER-001",
            }),
            "nombre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nombre del producto",
            }),
            "precio": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0.01",
                "step": "0.01",
            }),
            "stock": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0",
            }),
            "stock_minimo": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "0",
            }),
        }

    def clean_precio(self):
        precio = self.cleaned_data["precio"]
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que 0.")
        return precio
