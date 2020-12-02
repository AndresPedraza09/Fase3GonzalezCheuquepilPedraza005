from django.test import TestCase
from login.forms import JuegoForm, CompañiaForm, ProductoForm
from login.models import Juego, Compañia, Producto
from django.core.files.uploadedfile import SimpleUploadedFile

class JuegoFormsTest(TestCase):
    def test_valid_form(self):
        j = Juego.objects.create(nombre='Prueba1')
        data = {'nombre': j.nombre,}
        form = JuegoForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        j = Juego.objects.create(nombre='')
        data = {'nombre': j.nombre, 'compañia': j.compañia}
        form = JuegoForm(data=data)
        self.assertFalse(form.is_valid())

class CompañiaFormsTest(TestCase):
    def test_valid_form(self):
        Comp = Compañia.objects.create(nombre_compañia='Prueba')
        data = {'nombre_compañia': Comp.nombre_compañia}
        form = CompañiaForm(data=data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_form(self):
        c = Compañia.objects.create(nombre_compañia='Prueba')
        data = {'nombre compañia': c.nombre_compañia}
        form = CompañiaForm(data=data)
        self.assertFalse(form.is_valid())

class ProductoFormsTest(TestCase):
    def test_valid_form(self):
        pro = Producto.objects.create(nombre_producto='Prueba', precio='Prueba1', marca='prueba2')
        data = {'nombre_producto': pro.nombre_producto, 'precio': pro.precio, 'marca': pro.marca}
        form = ProductoForm(data=data)
        self.assertTrue(form.is_valid())
        
    def test_invalid_form(self):
        pro = Producto.objects.create(nombre_producto='Prueba1', precio='Prueb2a', marca='prueba3')
        data = {'nombre_producto': pro.nombre_producto, 'precio': pro.precio, 'marca': pro.marca}
        form = CompañiaForm(data=data)
        self.assertFalse(form.is_valid())