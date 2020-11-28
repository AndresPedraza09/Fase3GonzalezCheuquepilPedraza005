from django import forms
from . models import Juego, Compañia

class JuegoForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre',max_length=60, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    compañia = forms.CharField(label='Compañia',max_length=60, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    
    class Meta:
        model = Juego
        fields = ('nombre', 'compañia')

class CompañiaForm(forms.ModelForm):
    nombre_compañia = forms.CharField(label='Nombre Compañia',max_length=60, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))    
    class Meta:
        model = Compañia
        fields = ('nombre_compañia',)