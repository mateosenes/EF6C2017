# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.


class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)


    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase

    Utilize este modelo ya que se debe saber por obligacion el distrito
    al que pertenece el candidato al que se votara
    """    

    distrito = models.ForeignKey(Distrito)


class Votos(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase

    por lo primero use una variable "valido" de tipo boolean ya que con esto
    se puede definir como se deben contar los votos. Tambien utilize esta 
    variable "candidato" ya que como se debe saber a que Candidato
    pertenece el voto se necesitaria una foreignkey de la misma, por eso
    use este tipo de modelo 
    """
    
    candidato = models.ForeignKey(Candidato)
    valido = models.BooleanField(null=False)
