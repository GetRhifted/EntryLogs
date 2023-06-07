from django.db import models
from django.contrib.auth.models import User
from datetime import time

# Modelo para el registro de la Mora.

class Registro(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=False)   
    Canasta = models.CharField(max_length=100)
    Fecha = models.DateField()

    Contenido_Total = models.FloatField(default=0.0)
    Azucar = models.FloatField(default=0.0)
    Sorbato = models.FloatField(default=0.0)
    Producto_no_Conforme = models.FloatField(default=0.0)
    Fruta_Seleccionada = models.FloatField(default=0.0)
    
    Inicio_Jornada = models.TimeField()
    Seleccion_del_Producto = models.TimeField()
    Mora_Entra_a_la_Olla = models.TimeField()
    Hervor_Inicio = models.TimeField()
    Hervor_Final = models.TimeField()
    Enfriamiento_Inicio = models.TimeField()
    Enfriamiento_Final = models.TimeField()
    Inicio_Despulpado = models.TimeField()
    Final_Despulpado = models.TimeField()
    Segunda_Coccion = models.TimeField()
    Hora_Final_Mora = models.TimeField()
    Inicio_de_Empaque = models.TimeField()
    Finalizacion_de_la_Canasta = models.TimeField()
    	
    Semilla = models.FloatField(default=0.0)
    Pulpa = models.FloatField(default=0.0)

    Valor_Primer_Brix = models.FloatField(default=0.0)
    Hora_Primer_Brix = models.TimeField()
    Valor_Brix_Final = models.FloatField(default=0.0)
    Hora_Brix_Final = models.TimeField()

    Producto_Terminado = models.IntegerField(default=0) 
    Media_Libra = models.IntegerField(default=0)
    Libra = models.IntegerField(default=0)
    Bolsa_Seis_kg = models.IntegerField(default=0)
    Otro = models.IntegerField(default=0, null=True)
    Observaciones = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.Canasta


# Modelo para el registro de la Fresa.

class RegistroFresa(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=False) 
    Canasta = models.CharField(max_length=100)
    Fecha = models.DateField()

    Contenido_Total = models.FloatField(default=0.0)
    Azucar = models.FloatField(default=0.0)
    Limon = models.FloatField(default=0.0)
    Producto_no_Conforme = models.FloatField(default=0.0)
    Fruta_Seleccionada = models.FloatField(default=0.0)
    
    Inicio_Jornada = models.TimeField()
    Seleccion_del_Producto = models.TimeField()
    Fresa_Entra_a_la_Olla = models.TimeField()
    Hervor_Inicio = models.TimeField()
    Introduccion_Azucar = models.TimeField()
    Introduccion_Limon = models.TimeField()
    Hervor_Final = models.TimeField()
    Hora_Licuado = models.TimeField()
    Hora_Final_Fresa = models.TimeField()
    Inicio_de_Empaque = models.TimeField()
    Finalizacion_de_la_Canasta = models.TimeField()
    	
    Valor_Primer_Brix = models.FloatField(default=0.0)
    Hora_Primer_Brix = models.TimeField()
    Valor_Brix_Final = models.FloatField(default=0.0)
    Hora_Brix_Final = models.TimeField()

    Producto_Terminado = models.IntegerField(default=0) 
    Media_Libra = models.IntegerField(default=0)
    Libra = models.IntegerField(default=0)
    Bolsa_Seis_kg = models.IntegerField(default=0)
    Otro = models.IntegerField(default=0, null=True)
    Observaciones = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Canasta
