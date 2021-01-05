__version__ = "1.0"
__author__ = "Dario Garcia"
__all__ = ['Organigrama']

import json
import os

from . import Area


class Organigrama:
    """
    Clase para manejo de un organigrama
    """

    def __init__(self, titulo, area_inicial):
        """
        Constructor organigrama
        :param nombre: nombre del organigrama
        """
        self.titulo = titulo
        self.area_inicial = area_inicial

    def imprimir_organigrama(self):
        print "*** Organigrama {titulo}***".format(titulo=self.titulo)
        self.area_inicial.imprimir()

    def get_area(self, codigo_area):
        return





