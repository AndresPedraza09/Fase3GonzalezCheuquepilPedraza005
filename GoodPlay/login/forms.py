from django import forms
from . models import Juego, Compañia, Producto

class JuegoForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre',max_length=60, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    
    class Meta:
        model = Juego
        fields = ('nombre',)

class CompañiaForm(forms.ModelForm):
    nombre_compañia = forms.CharField(label='Nombre Compañia',max_length=60, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))    
    class Meta:
        model = Compañia
        fields = ('nombre_compañia',)

class ProductoForm(forms.ModelForm):

    nombre_producto = forms.CharField(label='Nombre Producto',max_length=60, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    precio = forms.CharField(label='Precio',max_length=60, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    marca = forms.CharField(label='Marca',max_length=60, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
        
    class Meta:
        model = Producto
        fields = ('nombre_producto', 'precio', 'marca',)