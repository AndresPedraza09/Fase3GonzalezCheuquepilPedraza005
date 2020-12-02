from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from login.models import Juego, Compañia, Producto

class JuegoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        number_of_juego = 9

        for juego_codigo in range(number_of_juego):
            Juego.objects.create(
                nombre=f' POULLO {juego_codigo}',
                juego=f'A {juego_codigo}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/login/juegos/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('juego_list'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('juego_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/juego_list.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('juego_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == False)
        self.assertTrue(len(response.context['juego_list']) == 9)

    

class CompañiaListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        number_of_compañia = 10
        for compañia_id_compañia in range(number_of_compañia):
            test_comp = Compañia.objects.create(
                nombre_compañia=f'MIHOYO {compañia_id_compañia}',
            )
            
            test_comp.save()

           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/login/compañia_list/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('compañia_list'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('compañia_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html', 'home.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('compañia_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == False)
        self.assertTrue(len(response.context['compañia_list']) == 10)

class ProductoListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        
        number_of_compañia = 10
        for producto_id_producto in range(number_of_compañia):
            test_pro = Producto.objects.create(
                nombre_producto=f'Monitor Asus {producto_id_producto}',
                precio=f'$300.000 {producto_id_producto}',
                marca=f'Asus {producto_id_producto}',

            )
            
            test_pro.save()

           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/login/producto_list/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('producto_list'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('producto_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html', 'home.html')
        
    def test_pagination_is_ten(self):
        response = self.client.get(reverse('producto_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == False)
        self.assertTrue(len(response.context['producto_list']) == 10)


        