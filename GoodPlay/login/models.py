from django.db import models
from django.urls import reverse  		#redirecciona una url de un libro al browser 
import uuid  							#se utiliza para definir atributos clave (pk)

# Create your models here.

class Juego(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Indique el Codigo del VideoJuego')
    nombre = models.CharField(max_length=60, help_text="Ingrese el Nombre del VideoJuego")
    compañia = models.ForeignKey('Compañia', on_delete=models.SET_NULL, null=True)
    fecha = models.DateField(null=True, blank=True)

    CLASIFICACION_JUEGO = (
        ('E','Todos'),
        ('E+10','Todos + 10'),
        ('T','Adolecentes'),
        ('M','Maduro +17'),
        ('A','Adultos +18'),
        ('RP','Clasificacion Pendiente'),
    )
    
    juego = models.CharField(
        max_length= 4,
        choices= CLASIFICACION_JUEGO,
        default='E',
        blank=True,
    )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.nombre},({self.compañia}),{self.codigo}'
    
    def get_absolute_url(self):
	    return reverse('juegos-detail', args=[str(self.codigo)])

    

class Compañia(models.Model):
    id_compañia = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Indique el Codigo de la Compañia')
    nombre_compañia = models.CharField(max_length=60, help_text="Ingrese el Nombre de la Compañia")

    def __str__(self):
        """String for representing the Model object."""
        return f' {self.nombre_compañia}'

    def get_absolute_url(self):
        return reverse('compañia-detail', args=[str(self.id_compañia)])

class Producto(models.Model):

    id_producto = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Indique el Codigo del producto')
    nombre_producto = models.CharField(max_length=60, help_text="Ingrese el Nombre del producto")
    precio = models.CharField(max_length=60, help_text="Ingrese el precio del producto")
    marca =  models.CharField(max_length=60, help_text="Ingrese la marca del producto")

    def __str__(self):
        """String for representing the Model object."""
        return f' {self.nombre_producto}, {self.precio}, {self.marca}'

    def get_absolute_url(self):
        return reverse('producto-detail', args=[str(self.id_producto)])